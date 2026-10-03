from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "postgresql://postgres:0000@localhost:5432/shop_db"

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

class Base(DeclarativeBase):
    pass







