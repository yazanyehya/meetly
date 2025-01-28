from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.auth.models import Base 

DATABASE_URL = "sqlite:///meetly.db"

engine = create_engine(DATABASE_URL,echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
