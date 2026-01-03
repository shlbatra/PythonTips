import requests

try:
    # httpbin /delay/3 waits for 3 seconds before responding
    response = requests.get("https://httpbin.org/delay/3", timeout=2)
    response.raise_for_status()  # Raise an error for bad responses
    print("Status Code:", response.status_code)
    print("Success:", response.json())
except requests.Timeout:
    print("The request timed out")
except requests.RequestException as e:
    print("Request Failed:", e)