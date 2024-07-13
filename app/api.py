from typing import Any

from fastapi import APIRouter, HTTPException, Path
from fastapi.responses import RedirectResponse
from starlette import status

from app.schema import ShortenerInput, ShortURL, URLstats
from app.core import shortener
from app.core.config import settings
from app.deps import DynamoTable
from app import crud

router = APIRouter()


@router.post(
    "/shorten",
    response_model=ShortURL,
    status_code=status.HTTP_201_CREATED,
    summary="단축 URL 생성",
    description="입력받은 원본 URL을 고유 단축키로 변환",
)
def create_short_url(table: DynamoTable, s_in: ShortenerInput) -> Any:
    key = shortener.hash_function(s_in.url)

    crud.create_short_url(table, key, s_in.url, s_in.duration)

    return {"short_url": "/".join([settings.BASE_URL, key])}


@router.get(
    "/stats/{short_key}",
    response_model=URLstats,
    summary="단축키 통계 조회",
    description="단축키의 조회수 및 기타 통계 조회",
)
def get_url_stats(
    table: DynamoTable,
    short_key: str = Path(
        default=..., description="단축키", min_length=7, max_length=7
    ),
) -> Any:
    item = crud.read_url_stat(table, short_key)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 단축URL에 대한 통계가 존재하지 않습니다.",
        )

    return {"count": item["count"], "latest": item["latest_at"]}


@router.get(
    "/{short_key}",
    response_class=RedirectResponse,
    status_code=status.HTTP_301_MOVED_PERMANENTLY,
    summary="원본 URL 리디렉션",
    description="단축키를 통해 원본 URL 리디렉션",
)
def redirect_origin_url(
    table: DynamoTable,
    short_key: str = Path(
        default=..., description="단축키", min_length=7, max_length=7
    ),
) -> Any:
    item = crud.read_url_info(table, short_key)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="존재하지 않는 단축URL입니다."
        )

    crud.update_url_stat(table, short_key)
    return item["origin_url"]
