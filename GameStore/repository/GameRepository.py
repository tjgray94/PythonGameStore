from sqlalchemy.orm import Session
from model import Game


def get_games_by_name(db: Session, name: str):
    return db.query(Game).filter(Game.name == name).all()
