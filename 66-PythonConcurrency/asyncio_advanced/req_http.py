import asyncio

import requests

# A few handy JSON types

JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]

# Synchronous code uses requests library for simplicity
def http_get_sync(url: str) -> JSONObject:
    response = requests.get(url)
    return response.json()

# Asynchronous wrapper around the synchronous code to work with asyncio
async def http_get(url: str) -> JSONObject:
    return await asyncio.to_thread(http_get_sync, url)