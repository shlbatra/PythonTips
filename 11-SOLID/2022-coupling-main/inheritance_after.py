"""
Use methods instead of inheritance
easier to test this code
"""
from typing import Any

from elasticsearch import Elasticsearch
from requests_aws4auth import AWS4Auth

DEV_HOST = "localhost:8700"

#creating logic
def create_elastic_client(host: str = DEV_HOST) -> Elasticsearch:
    awsauth = AWS4Auth(
        service="elb",
    )
    return Elasticsearch(
        hosts=[host],
        http_auth=awsauth,
        verify_certs=True,
    )

#using logic
def find_hits(
    client: Elasticsearch,
    query: dict[str, Any],
    size: int,
    index: str,
    **kwargs: Any,
) -> list[dict[str, Any]]:
    response = client.search(
        query=query,
        size=size,
        index=index,
        **kwargs,
    )
    return response["hits"]["hits"]
