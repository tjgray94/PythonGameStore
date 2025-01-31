from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from model.Game import Game
from schemas.GameSchema import GameCreate, GameResponse

router = APIRouter(prefix="/api/games", tags=["games"])


@router.get("/", response_model=List[GameResponse])
def get_all_games(db: Session = Depends(get_db)):
    return db.query(Game).all()


@router.get("/{game_id}", response_model=GameResponse)
def get_game_by_id(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.game_id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game


@router.post("/", response_model=GameResponse, status_code=201)
def create_game(game: GameCreate, db: Session = Depends(get_db)):
    new_game = Game(
        name=game.name,
        image=game.image,
        price=game.price,
        release_date=game.release_date,
        rating=game.rating
    )
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    return new_game


@router.put("/{game_id}", response_model=GameResponse)
def update_game(game_id: int, updated_game: GameCreate, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.game_id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    game.name = updated_game.name
    game.image = updated_game.image
    game.price = updated_game.price
    game.release_date = updated_game.release_date
    game.rating = updated_game.rating

    db.commit()
    db.refresh(game)
    return game


@router.delete("/{game_id}", status_code=204)
def delete_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.game_Id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    db.delete(game)
    db.commit()
    return


@router.delete("/", status_code=204)
def delete_all_games(db: Session = Depends(get_db)):
    db.query(Game).delete()
    db.commit()
    return
