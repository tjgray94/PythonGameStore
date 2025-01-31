from sqlalchemy.orm import Session
from model import User


def get_users_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).all()