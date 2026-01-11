import asyncio
from random import randint
from time import perf_counter
from typing import AsyncIterable

from req_http import JSONObject, http_get, http_get_sync

# The highest Pokemon id
MAX_POKEMON = 898

# Gather allows running multiple coroutines concurrently and collecting their results
# Better approach to use Generator Expressions to create tasks on the fly
# http_get is async based on asyncio.to_thread wrapping the sync version
async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])

async def next_pokemon(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        yield await get_random_pokemon_name()


async def main() -> None:

    
    # asynchronous call
    time_before = perf_counter()
    # tasks = [get_random_pokemon_name() for _ in range(20)] 
    # ans = await asyncio.gather(*tasks) # Gather runs tasks concurrently
    ans = [name async for name in next_pokemon(10)] # Gather run tasks as part of an async generator
    print(ans)
    print(f"Total time (asynchronous): {perf_counter() - time_before}")


asyncio.run(main())