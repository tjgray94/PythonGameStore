from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"

    userid = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
