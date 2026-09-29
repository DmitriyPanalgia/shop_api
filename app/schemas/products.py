from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    quantity: int


class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    quantity: int | None = None