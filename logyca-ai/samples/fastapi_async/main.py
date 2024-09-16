from app.routers import azure_chatgpt, azure_chatgpt_utils
from fastapi import FastAPI
from fastapi.exceptions import HTTPException, RequestValidationError
from logyca import http_exception_handler_async, unhandled_exception_handler_async,validation_exception_handler_async
import uvicorn

app = FastAPI()

app.include_router(azure_chatgpt.router)
app.include_router(azure_chatgpt_utils.router)

app.add_exception_handler(Exception, unhandled_exception_handler_async)
app.add_exception_handler(HTTPException, http_exception_handler_async)
app.add_exception_handler(RequestValidationError, validation_exception_handler_async)

if __name__=='__main__':
    uvicorn.run('main:app',host="0.0.0.0",port=80,reload=True)