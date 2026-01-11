import asyncio
import time

import requests


async def counter(until: int = 10) -> None:
    now = time.perf_counter()
    print("Started counter")
    for i in range(0, until):
        last = now
        await asyncio.sleep(0.01)
        now = time.perf_counter()
        print(f"{i}: Was asleep for {now - last}s")


def send_request(url: str) -> int:
    print("Sending HTTP request")
    response = requests.get(url)
    return response.status_code


async def main() -> None:
    task = asyncio.create_task(counter()) # Schedule counter - just schedules, doesn't run yet

    status_code = send_request("https://www.arjancodes.com") # Blocking call! Synchronous blocking call - freezes the event loop  
    print(f"Got HTTP response with status {status_code}")

    await task # Run here 


asyncio.run(main())