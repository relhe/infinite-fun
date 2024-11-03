import os


class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
