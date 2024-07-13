import boto3
from boto3.dynamodb.conditions import Key

from app.core.config import settings


# dynamodb 리소스
db_resource = boto3.resource(
    "dynamodb",
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY,
    region_name=settings.AWS_REGION,
)
