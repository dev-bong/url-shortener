from mypy_boto3_dynamodb.service_resource import Table


def key_dict(pk: str, sk: str) -> dict:
    # dictionary 형태의 키 조합 만들기 (pk + sk)
    key_name = ("key", "sort_key")
    return dict(zip(key_name, (pk, sk)))


def create_short_url(table: Table, pk: str, origin_url: str) -> None:
    # 단축 url 생성
    url_info = key_dict(pk, "info#")
    url_info["origin_url"] = origin_url

    table.put_item(Item=url_info)


def read_url_info(table: Table, pk: str) -> dict:
    # 단축 url 정보 조회
    info_key = key_dict(pk, "info#")
    return table.get_item(Key=info_key).get("Item", {})
