from app.database.database import engine, Base
from app.models.product import ProductModel




Base.metadata.create_all(engine)