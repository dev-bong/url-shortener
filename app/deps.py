from typing import Annotated

from mypy_boto3_dynamodb.service_resource import Table
from fastapi import Depends

from app.core.db import db_resource
from app.core.config import settings


def get_table():
    # dynamodb 테이블 객체 생성
    return db_resource.Table(settings.DYNAMODB_TABLENAME)


DynamoTable = Annotated[Table, Depends(get_table)]
