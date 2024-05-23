from fastapi import FastAPI, Depends
from logyca import OAuthTokenScheme, OAuthToken, ClaimsDTO
import os

ENPOINTAZUREB2C_APICRUDURL=os.getenv('APICRUD_URL','https://domain.ccc/')
ENPOINTAZUREB2C_APICRUDMETHODVALIDATELOGIN=os.getenv('METHOD_VALIDATE_LOGIN','api/method/')
LOGYCA_APIKEY=os.getenv('LOGYCA_APIKEY','...key...')

app = FastAPI()

settings_oauth_token=OAuthTokenScheme(
    endpoint_azure_b2c_apicrud=ENPOINTAZUREB2C_APICRUDURL,
    endpoint_azure_b2c_apicrud_method_validate_login=ENPOINTAZUREB2C_APICRUDMETHODVALIDATELOGIN,
    logyca_apikey=LOGYCA_APIKEY,
    enable=True)
get_oauth_token = OAuthToken(settings_oauth_token)

@app.get("/data/")
def read_item(claims_dto: ClaimsDTO = Depends(get_oauth_token)):
    return {"user checked ok: ": f"{claims_dto}"}
