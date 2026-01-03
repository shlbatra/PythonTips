import requests

# Using JSONPlaceholder - a free fake API for testing
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Hello from Sahil",
    "body": "Sahil is awesome!",
    "userId": 1
}

response = requests.post(url, json=payload)
print("Requested URL:", response.url)


response.raise_for_status() # raise an error for bad responses

print("Status Code:", response.status_code)
print("Response Headers Content-Type:", response.headers.get('Content-Type'))
print("\n\n")

data = response.json()
print(data)