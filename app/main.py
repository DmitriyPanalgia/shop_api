from fastapi import FastAPI
from app.routers.products import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def main_page():
    return {"message": "Shop API"}