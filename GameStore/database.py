from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Fetch database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Setup the database engine and session
engine = create_engine(DATABASE_URL)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
