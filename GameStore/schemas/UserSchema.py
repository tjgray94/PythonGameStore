from pydantic import BaseModel


# Request schema for creating/updating a user
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True


# Response schema for a user
class UserResponse(BaseModel):
    userid: int
    name: str
    email: str

    class Config:
        from_attributes = True
