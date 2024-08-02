from fastapi import FastAPI
from app.routers import azure_chatgpt

app = FastAPI()

app.include_router(azure_chatgpt.router)