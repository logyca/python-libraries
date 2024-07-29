from datetime import datetime
from logyca import HealthEnum, LogycaStatusEnum, APIResultDTO, ApiFilterExceptionDTO, HealthDTO, TokensDTO
from starlette.responses import JSONResponse
import json
import os

# Load environment variables
APP_REGISTRATION_CLIENT_ID=os.getenv('CLIENT_ID','0d71d9ad-f5b9-40f7-a575-e1aabedd1d00')
APP_REGISTRATION_CLIENT_SECRET_NAME=os.getenv('CLIENT_SECRET_NAME','connect_test')
APP_REGISTRATION_CLIENT_SECRET_VALUE=os.getenv('CLIENT_SECRET_VALUE','soksijsjuueje883j3j8djj3g44')
APP_REGISTRATION_CLIENT_SECRET_EXPIRES_VALUE=os.getenv('CLIENT_SECRET_EXPIRES','7/19/2026')
APP_REGISTRATION_CLIENT_SECRET_EXPIRES_FORMAT=os.getenv('CLIENT_SECRET_EXPIRES','%m/%d/%Y')

def days_between_dates(date_str:str='7/19/2026',date_format:str='%m/%d/%Y')->int:    
    future_date = datetime.strptime(date_str, date_format)
    today_date = datetime.today()
    difference_in_days = (future_date - today_date).days
    return difference_in_days

def simulate_service():
    tokensDTO=TokensDTO()
    tokensDTO.token='Token Example'

    listHealth=[]

    exist_alert=False

    # Test CPU
    listHealth.append(HealthDTO(name='Check CPU',status=HealthEnum.Ok,description='OK').to_dict())
    # Resource connection test
    listHealth.append(HealthDTO(name='Check Connect DB',status=HealthEnum.Warning,description='Warning').to_dict())
    exist_alert=True
    # Resource connection test
    listHealth.append(HealthDTO(name='Check Connect Storage',status=HealthEnum.Critical,description='Critical').to_dict())
    exist_alert=True
    # Credential expiration test
    difference_in_days = days_between_dates(APP_REGISTRATION_CLIENT_SECRET_EXPIRES_VALUE,APP_REGISTRATION_CLIENT_SECRET_EXPIRES_FORMAT)
    if difference_in_days <= 30:
        listHealth.append(HealthDTO(name=f'Expiration days for {APP_REGISTRATION_CLIENT_SECRET_NAME}: [{difference_in_days}]',status=HealthEnum.Critical,description='Critical').to_dict())
    elif difference_in_days <= 60:
        listHealth.append(HealthDTO(name=f'Expiration days for {APP_REGISTRATION_CLIENT_SECRET_NAME}: [{difference_in_days}]',status=HealthEnum.Warning,description='Warning').to_dict())
    else:
        listHealth.append(HealthDTO(name=f'Expiration days for {APP_REGISTRATION_CLIENT_SECRET_NAME}: [{difference_in_days}]',status=HealthEnum.Ok,description='Ok').to_dict())
    exist_alert=True

    apiResultDTO=APIResultDTO()
    apiResultDTO.resultMessage='Health check'
    apiResultDTO.resultObject=listHealth
    apiResultDTO.resultToken=tokensDTO
    apiResultDTO.dataError=exist_alert
    if exist_alert is True:
        apiFilterExceptionDTO=ApiFilterExceptionDTO()
        apiFilterExceptionDTO.message="Existing alert"
        apiFilterExceptionDTO.logycaStatus=LogycaStatusEnum.UnAvailable
        apiFilterExceptionDTO.status=LogycaStatusEnum.UnAvailable.mappingHttpStatusCode
        apiResultDTO.apiException=apiFilterExceptionDTO

    return apiResultDTO

def main():
    apiResultDTO:APIResultDTO = simulate_service()
    print((json.dumps(apiResultDTO.to_dict(),indent=4)))
    return JSONResponse(content=apiResultDTO.to_dict(),status_code=apiResultDTO.apiException.status)

if __name__ == "__main__":
    main()

