from starlette.config import Config


class Settings:
    """
    각종 설정 및 상수 관리
    """

    config = Config(".env")  # .env 파일 불러오기

    AWS_ACCESS_KEY: str = config("AWS_ACCESS_KEY")
    AWS_SECRET_KEY: str = config("AWS_SECRET_ACCESS_KEY")
    AWS_REGION: str = "ap-northeast-2"  # 서울 region
    DYNAMODB_TABLENAME: str = "ShortenerURL"  # dynamodb 테이블 이름

    BASE_URL: str = "http://127.0.0.1:8000"


settings = Settings()
