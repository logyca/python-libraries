from fastapi import FastAPI, Depends
from logyca import APIKeyScheme, APIKey
import os
import uvicorn

API_KEY=os.getenv('API_KEY','password_key')

app = FastAPI()

settings_api_key=APIKeyScheme(key=API_KEY, enable=True)
get_api_key = APIKey(settings_api_key)

@app.get("/data/")
def read_item(api_key: str = Depends(get_api_key)):
    return {"api_key checked ok: ": f"{api_key}"}

if __name__=='__main__':
    uvicorn.run('main:app',host="0.0.0.0",port=80,reload=True)

