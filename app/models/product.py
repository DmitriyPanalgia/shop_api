from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base


class ProductModel(Base):
    __tablename__ = "products"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

