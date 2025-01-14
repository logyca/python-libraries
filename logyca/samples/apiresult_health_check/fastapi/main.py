from datetime import datetime
from fastapi import FastAPI, Depends, Security, HTTPException
from fastapi.security.api_key import APIKeyHeader
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
import os
from logyca import (
    ApiFilterExceptionDTO,
    APIResultDTO,
    HealthDTO,
    HealthEnum,
    LogycaStatusEnum,
    TokensDTO,
)

#   #############################################################################################################
#   Safety recommendation                                                                                   
#   It is recommended that the Api Key for monitoring support staff be personalized and not known to anyone else.
#   Likewise, other API Keys should not be known to support staff.
#   #############################################################################################################


#   #############################################################################################################
#   Load environment variables | static date values ​​to validate their expiration
API_KEY_MON                                     =   os.getenv('API_KEY_MON','key string')
APP_REGISTRATION_CLIENT_ID                      =   os.getenv('CLIENT_ID','0x71x9xx-x7x6-40f7-x575-xxxxxxxx')
APP_REGISTRATION_CLIENT_SECRET_NAME             =   os.getenv('CLIENT_SECRET_NAME','connect_test')
APP_REGISTRATION_CLIENT_SECRET_VALUE            =   os.getenv('CLIENT_SECRET_VALUE','soksijsjuueje883j3j8djj3g44')
APP_REGISTRATION_CLIENT_SECRET_EXPIRES_VALUE    =   os.getenv('CLIENT_SECRET_EXPIRES','7/19/2026')
APP_REGISTRATION_CLIENT_SECRET_EXPIRES_FORMAT   =   os.getenv('CLIENT_SECRET_EXPIRES','%m/%d/%Y')

#   #############################################################################################################
#   MAIN

def days_between_dates(date_str:str='7/19/2026',date_format:str='%m/%d/%Y')->int:    
    future_date = datetime.strptime(date_str, date_format)
    today_date = datetime.today()
    difference_in_days = (future_date - today_date).days
    return difference_in_days

app = FastAPI()

API_KEY_MON_NAME = "x-apimon-key"
get_api_key_mon = APIKeyHeader(
    name=API_KEY_MON_NAME,
    scheme_name="Monitoring system access key",
    auto_error=False
)
def verify_api_key_mon(api_key: str = Security(get_api_key_mon)):
    if api_key != API_KEY_MON:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail=f"Invalid or missing {API_KEY_MON_NAME} for monitoring access"
        )
    return api_key

@app.get("/health/check")
def check(api_key: str = Depends(verify_api_key_mon)):
    tokensDTO=TokensDTO()
    tokensDTO.token='Token Example'

    listHealth=[]

    exist_alert=False

    # Test CPU
    listHealth.append(HealthDTO(name='[Print Test] Check CPU',status=HealthEnum.Ok,description='OK').to_dict())
    # Resource connection test
    listHealth.append(HealthDTO(name='[Print Test] Check Connect DB',status=HealthEnum.Warning,description='Warning').to_dict())
    exist_alert=True
    # Resource connection test
    listHealth.append(HealthDTO(name='[Print Test] Check Connect Storage',status=HealthEnum.Critical,description='Critical').to_dict())
    exist_alert=True
    # Credential expiration test
    difference_in_days = days_between_dates(APP_REGISTRATION_CLIENT_SECRET_EXPIRES_VALUE,APP_REGISTRATION_CLIENT_SECRET_EXPIRES_FORMAT)
    if difference_in_days <= 30:
        listHealth.append(HealthDTO(name=f'[Live Test] Expiration days for {APP_REGISTRATION_CLIENT_SECRET_NAME}: [{difference_in_days}]',status=HealthEnum.Critical,description='Critical').to_dict())
        exist_alert=True
    elif difference_in_days <= 60:
        listHealth.append(HealthDTO(name=f'[Live Test] Expiration days for {APP_REGISTRATION_CLIENT_SECRET_NAME}: [{difference_in_days}]',status=HealthEnum.Warning,description='Warning').to_dict())
        exist_alert=True
    else:
        listHealth.append(HealthDTO(name=f'[Live Test] Expiration days for {APP_REGISTRATION_CLIENT_SECRET_NAME}: [{difference_in_days}]',status=HealthEnum.Ok,description='Ok').to_dict())
    # Simulate http request
    result_http_request = 501
    logyca_status_code = LogycaStatusEnum.from_http_status_code(result_http_request)
    listHealth.append(HealthDTO(name='[Print Test] Check Connect API',status=HealthEnum.Critical,description=f'Error - http status code: {result_http_request}, logyca_status_code: {logyca_status_code}').to_dict())

    apiResultDTO=APIResultDTO()
    apiResultDTO.resultMessage='Health check'
    apiResultDTO.resultObject=listHealth
    apiResultDTO.resultToken=tokensDTO
    apiResultDTO.dataError=exist_alert
    if exist_alert is True:
        apiFilterExceptionDTO=ApiFilterExceptionDTO()
        apiFilterExceptionDTO.message="Existing alert"
        apiFilterExceptionDTO.isError = True
        apiFilterExceptionDTO.logycaStatus=LogycaStatusEnum.UnAvailable
        apiFilterExceptionDTO.status=LogycaStatusEnum.UnAvailable.mappingHttpStatusCode
        apiResultDTO.apiException=apiFilterExceptionDTO
        apiResultDTO.dataError = True
    
    return JSONResponse(content=apiResultDTO.to_dict(),status_code=HTTP_200_OK)
