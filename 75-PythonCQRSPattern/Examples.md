In order to run a MongoDB instance locally, make sure you have docker installed on your machine and run:

```
docker compose up -d
```

Then run the FastAPI app as follows:

```
uv sync
source .venv/bin/activate
uvicorn before:app --reload # to run the before version of the code
```

Here are a few example requests you can use to test the FastAPI app:

# Create a ticket

curl -X POST http://localhost:8000/tickets \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "cust-123",
    "subject": "Login not working",
    "message": "I cannot log in after resetting my password."
  }'

# Update ticket status - Not work on Read - only on Write

curl -X POST http://localhost:8000/tickets/6993deb17cb051dc9f3bc672 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "triaged"
  }'

# Update ticket status (after version)

curl -X POST http://localhost:8000/tickets/6993deb17cb051dc9f3bc672/status \
  -H "Content-Type: application/json" \
  -d '{
    "new_status": "triaged"
  }'

# List all tickets
curl http://localhost:8000/tickets

# Add a note

curl -X POST http://localhost:8000/tickets/6993deb17cb051dc9f3bc672/agent-note \
  -H "Content-Type: application/json" \
  -d '{
    "note": "Customer reset their password twice; investigating auth service."
  }'

# Dashboard
curl http://localhost:8000/dashboard