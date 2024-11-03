# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./chess_game.db"  # Path to your SQLite database file

# Set up the SQLite database and the base class
Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the Game model


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    # Status can be 'ongoing', 'checkmate', etc.
    status = Column(String, default="ongoing")

# Define the Move model


class Move(Base):
    __tablename__ = "moves"

    id = Column(Integer, primary_key=True, index=True)
    game_id = Column(Integer, ForeignKey("games.id"))
    start_pos = Column(String)  # Store as "a2" or "e4"
    end_pos = Column(String)

    game = relationship("Game", back_populates="moves")


# Establish relationship back in Game
Game.moves = relationship("Move", back_populates="game")

# Create all tables in the database
Base.metadata.create_all(bind=engine)
