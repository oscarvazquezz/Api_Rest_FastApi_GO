from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .Settings import settings

POSTGRES_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.DATABASE_PORT}/{settings.POSTGRES_DB}"

engine = create_engine(POSTGRES_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()