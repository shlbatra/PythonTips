# Anatomy of a Scalable Python Project (FastAPI)

https://www.youtube.com/watch?v=Af6Zr0tNNdE

Starting the server:

uv run uvicorn app.main:app --reload

Example requests:

Here’s a set of simple curl examples you can use to interact with your FastAPI app once it’s running (default at http://localhost:8000):

1️⃣ Create a User

curl -X POST "http://localhost:8000/api/v1/users" \
     -H "Content-Type: application/json" \
     -d '{"name": "Ada Lovelace"}'


2️⃣ Get All Users

curl -X GET "http://localhost:8000/api/v1/users"


3️⃣ Get a User by ID

(Replace 1 with the actual ID from the create response)

curl -X GET "http://localhost:8000/api/v1/users/1"


4️⃣ Update a User

curl -X PUT "http://localhost:8000/api/v1/users/1" \
     -H "Content-Type: application/json" \
     -d '{"name": "Grace Hopper"}'


⸻

5️⃣ Delete a User

curl -X DELETE "http://localhost:8000/api/v1/users/1"


Code
app
v1 - first version of api
standard api routes defined here

core 
Include config settings for database and 

docker-compose
Works for local orchestration and passes required environment variables
uses dockerfile to run locally

docker compose up --build