from dependencies import get_db  # Assuming get_db is in dependencies.py
from models import Game, Move, Base, engine
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for communication with Next.js frontend
app.add_middleware(
    CORSMiddleware,
    # Change this to your frontend URL
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize the database (only needed if you're not using Alembic migrations)
Base.metadata.create_all(bind=engine)


@app.post("/games/")
def create_game(db: Session = Depends(get_db)):
    game = Game()  # Default status is "ongoing"
    db.add(game)
    db.commit()
    db.refresh(game)
    return {"game_id": game.id, "status": game.status}


@app.post("/games/{game_id}/move/")
def make_move(game_id: int, start_pos: str, end_pos: str, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    move = Move(game_id=game.id, start_pos=start_pos, end_pos=end_pos)
    db.add(move)
    db.commit()
    return {"status": "Move recorded"}


@app.get("/games/{game_id}")
def get_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    moves = db.query(Move).filter(Move.game_id == game_id).all()
    return {
        "game_id": game.id,
        "status": game.status,
        "moves": [{"start": move.start_pos, "end": move.end_pos} for move in moves],
    }
