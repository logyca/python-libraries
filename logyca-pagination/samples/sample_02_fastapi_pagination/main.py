from fastapi import FastAPI
from app.routers import pagination

app = FastAPI()

app.include_router(pagination.router)