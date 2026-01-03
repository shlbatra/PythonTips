import requests

# Using JSONPlaceholder - a free fake API for testing
url = "https://jsonplaceholder.typicode.com/users"
params = {
    "_limit": 3  # Limit to 3 users
}

response = requests.get(url, params=params)
print("Requested URL:", response.url)


response.raise_for_status() # raise an error for bad responses

print("Status Code:", response.status_code)
print("Response Headers Content-Type:", response.headers.get('Content-Type'))
print("\n\n")

data = response.json()
print(f"Found {len(data)} users")

for user in data:
    print("User ID:", user['id'], "Email:", user['email'])