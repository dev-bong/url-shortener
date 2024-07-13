from mypy_boto3_dynamodb.service_resource import Table

from app.util import mytime


def key_dict(pk: str, sk: str) -> dict:
    # dictionary 형태의 키 조합 만들기 (pk + sk)
    key_name = ("key", "sort_key")
    return dict(zip(key_name, (pk, sk)))


def create_short_url(
    table: Table, pk: str, origin_url: str, duration: int | None
) -> None:
    # 단축 url 생성
    url_info = key_dict(pk, "info#")
    url_info["origin_url"] = origin_url
    # 만료시간 설정 ("expire_at"은 TTL 속성)
    if duration:
        now_ts = mytime.ts_now()
        url_info["expire_at"] = mytime.ts_after(now_ts, duration)

    table.put_item(Item=url_info)


def read_url_info(table: Table, pk: str) -> dict:
    # 단축 url 정보 조회
    info_key = key_dict(pk, "info#")
    return table.get_item(Key=info_key).get("Item", {})


def update_url_stat(table: Table, pk: str) -> None:
    # 단축 url 통계 업데이트
    stat_key = key_dict(pk, "stat#1")
    url_stat = table.get_item(Key=stat_key).get("Item", {})

    # count 값 증가
    if url_stat:
        url_stat["count"] = url_stat["count"] + 1
    else:
        url_stat = dict(**stat_key, count=1)
    # 최근 접속 timestamp
    url_stat["latest_at"] = mytime.ts_now()

    table.put_item(Item=url_stat)
