- Curl commands to test fastapi 
 
- Create a book (POST):
  curl -X POST http://localhost:8000/books/ \
    -H "Content-Type: application/json" \
    -d '{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": 180}'

- List all books (GET):
  curl http://localhost:8000/books/

- Get a specific book (GET): (use the ID returned from POST)
  curl http://localhost:8000/books/<book_id>