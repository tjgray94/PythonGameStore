from sqlalchemy import Column, Integer, String, Float
from database import Base


class Game(Base):
    __tablename__ = "games"

    game_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    image = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    release_date = Column(String, unique=True, nullable=False)
    rating = Column(Float, nullable=False)

    def __init__(self, name, image, price, release_date, rating):
        self.name = name
        self.image = image
        self.price = price
        self.release_date = release_date
        self.rating = rating

    def __repr__(self):
        return f"<Game(name={self.name}, price={self.price}, rating={self.rating})>"
