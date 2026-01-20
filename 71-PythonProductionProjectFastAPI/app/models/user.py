from pydantic import BaseModel

# Pydantic schemas for request and response contracts
class UserCreate(BaseModel):
    name: str


class UserRead(BaseModel):
    id: int
    name: str
