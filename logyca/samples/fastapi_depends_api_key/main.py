from fastapi import FastAPI, Depends
import os
import uvicorn

# The name of the api key will be read from the environment variables or will be assigned by default with the value "x-api-key"
# os.environ["API_KEY_NAME"] = "x-api-key-other-value"
from logyca import APIKeyScheme, APIKey

API_KEY_VALUE=os.getenv('API_KEY_VALUE','password_key')

app = FastAPI()

settings_api_key=APIKeyScheme(key=API_KEY_VALUE, enable=True)
get_api_key = APIKey(settings_api_key)

@app.get("/data/")
def read_item(api_key: str = Depends(get_api_key)):
    return {"api_key checked ok: ": f"{api_key}"}

if __name__=='__main__':
    uvicorn.run('main:app',host="0.0.0.0",port=80,reload=True)

