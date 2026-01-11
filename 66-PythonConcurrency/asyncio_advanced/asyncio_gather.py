import asyncio
from random import randint
from time import perf_counter

from req_http import JSONObject, http_get, http_get_sync

# The highest Pokemon id
MAX_POKEMON = 898

def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get_sync(pokemon_url)
    return str(pokemon["name"])

# Gather allows running multiple coroutines concurrently and collecting their results
# Better approach to use Generator Expressions to create tasks on the fly
# http_get is async based on asyncio.to_thread wrapping the sync version
async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])

async def main() -> None:

    # synchronous call
    time_before = perf_counter()
    for _ in range(20):
        print(get_random_pokemon_name_sync())
    print(f"Total time (synchronous): {perf_counter() - time_before}")

    # asynchronous call
    time_before = perf_counter()
    tasks = [get_random_pokemon_name() for _ in range(20)] # Function needs to be async to be awaited
    ans = await asyncio.gather(*tasks) # Gather runs tasks concurrently
    print(ans)
    print(f"Total time (asynchronous): {perf_counter() - time_before}")


asyncio.run(main())