from mypy_boto3_dynamodb.service_resource import Table


def create_short_url(table: Table, short_key: str, origin_url: str) -> None:
    item = {"key": short_key, "sort_key": "aa", "origin_url": origin_url}
    table.put_item(Item=item)


def read_origin_url(table: Table, short_key: str) -> dict:
    return table.get_item(Key={"key": short_key, "sort_key": "aa"}).get("Item", {})
