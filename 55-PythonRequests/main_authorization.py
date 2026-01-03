import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("API_TOKEN")
if not TOKEN:
    raise ValueError("API_TOKEN not found in .env file")

url = "https://api.x.com/2/users/by/username/sbatra6" # Replace with the actual API

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(url, headers=headers)
print("Requested URL:", response.url)

response.raise_for_status()  # raise an error for bad responses

print("Status Code:", response.status_code)
print("Response Headers Content-Type:", response.headers.get('Content-Type'))

try:
    data = response.json()
    print("\n\n")
    print("Response JSON:", data)
except ValueError:
    print("Response content is not valid JSON")
    print("Response Text:", response.text)