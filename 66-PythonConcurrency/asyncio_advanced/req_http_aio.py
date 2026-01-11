import aiohttp

# A few handy JSON types
JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]

# def http_get_sync(url: str) -> JSONObject:
#     response = requests.get(url)
#     return response.json()

async def http_get(url: str) -> JSONObject:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response: # session is a context manager
            return await response.json()