from app.routers import azure_chatgpt
from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(azure_chatgpt.router)

if __name__=='__main__':
    uvicorn.run('main:app',host="0.0.0.0",port=80,reload=True)