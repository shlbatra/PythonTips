from fastapi import FastAPI

app = FastAPI() # Fast API


@app.get("/")
def hello(name: str = "World"):
    return f"Hello, {name}!"
