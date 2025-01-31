from pydantic import BaseModel


# Request schema for creating/updating a game
class GameCreate(BaseModel):
    name: str
    image: str
    price: float
    release_date: str
    rating: float

    class Config:
        from_attributes = True


# Response schema for a user
class GameResponse(BaseModel):
    game_id: int
    name: str
    image: str
    price: float
    release_date: str
    rating: float

    class Config:
        from_attributes = True
