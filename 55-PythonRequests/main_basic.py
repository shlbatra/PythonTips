import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Response Headers Content-Type:", response.headers.get('Content-Type'))
print("\n\n")

data = response.json()
print("Response JSON:", data)
print("\n\n")
print("Response Title:", data['title'])