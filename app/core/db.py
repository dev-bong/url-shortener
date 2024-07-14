import boto3

from app.core.config import settings


# dynamodb 리소스
db_resource = boto3.resource(
    "dynamodb",
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY,
    region_name=settings.AWS_REGION,
)

db_client = boto3.client(
    "dynamodb",
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY,
    region_name=settings.AWS_REGION,
)

table_recipe = {
    "TableName": settings.DYNAMODB_TABLENAME,
    "KeySchema": [
        {"AttributeName": "key", "KeyType": "HASH"},
        {"AttributeName": "sort_key", "KeyType": "RANGE"},
    ],
    "AttributeDefinitions": [
        {"AttributeName": "key", "AttributeType": "S"},
        {"AttributeName": "sort_key", "AttributeType": "S"},
    ],
    "BillingMode": "PROVISIONED",
    "ProvisionedThroughput": {  # 읽기, 쓰기 용량
        "ReadCapacityUnits": 10,
        "WriteCapacityUnits": 10,
    },
}


def init():
    try:
        # 테이블이 존재하는지 체크
        table = db_client.describe_table(TableName=settings.DYNAMODB_TABLENAME)
    except db_client.exceptions.ResourceNotFoundException:
        print("테이블이 존재하지 않습니다. 테이블을 생성합니다.")

        try:
            # 테이블 생성
            print("테이블 생성 중... 잠시 기다려 주세요.")
            db_client.create_table(**table_recipe)
            waiter = db_client.get_waiter("table_exists")
            waiter.wait(TableName=settings.DYNAMODB_TABLENAME)  # 테이블 생성까지 대기
        except:
            print("테이블 생성에 실패하였습니다. 다시 시도해주세요.")
        else:
            print("테이블 생성 완료")
            # 테이블 TTL 설정
            db_client.update_time_to_live(
                TableName=settings.DYNAMODB_TABLENAME,
                TimeToLiveSpecification={"Enabled": True, "AttributeName": "expire_at"},
            )
            print("TTL 설정 완료")

    else:
        print("테이블이 존재합니다. 테이블 생성 단계를 건너뜁니다.")
