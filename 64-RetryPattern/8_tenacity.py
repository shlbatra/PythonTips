import random

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

# Built-in retry decorator from tenacity library
# It stops after 3 total attempts (1 initial + 2 retries)
# multiplier=1 — scales the exponential value
# min=1 — minimum wait time (1 second)
# max=10 — maximum wait time (10 seconds)

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
def fetch_joke() -> str:
    """Fetch a random Chuck Norris joke with retry logic using tenacity."""
    # randomly raise an error to simulate failures
    if random.random() < 0.9:
        raise RuntimeError("simulated random failure")
    with httpx.Client() as client:
        response = client.get("https://api.chucknorris.io/jokes/random", timeout=2.0)
        response.raise_for_status()
        data: dict[str, str] = response.json()
        return data["value"]


def main() -> None:
    print(fetch_joke())


if __name__ == "__main__":
    main()