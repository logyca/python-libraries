from fastapi.encoders import jsonable_encoder
from logyca import HealthEnum, LogycaStatusEnum, APIResultDTO, ApiFilterExceptionDTO, HTTPExceptionDTO, HealthDTO, TokensDTO
from starlette.responses import JSONResponse
import json

def example_service():
    tokensDTO=TokensDTO()
    tokensDTO.token='Token Example'

    apiFilterExceptionDTO=ApiFilterExceptionDTO()
    apiFilterExceptionDTO.isError=False
    apiFilterExceptionDTO.logycaStatus=int(LogycaStatusEnum.Already_Exists)
    apiFilterExceptionDTO.status=int(LogycaStatusEnum.Already_Exists.mappingHttpStatusCode)

    httpExceptionDTO=HTTPExceptionDTO()
    httpExceptionDTO.detail='No Problem'

    listHealth=[]

    listHealth.append(HealthDTO(name='Check CPU',status=HealthEnum.Ok,description='OK').__dict__)
    listHealth.append(HealthDTO(name='Check Connect DB',status=HealthEnum.Warning,description='Warning').__dict__)
    listHealth.append(HealthDTO(name='Check Connect Storage',status=HealthEnum.Critical,description='Critical').__dict__)

    apiResultDTO=APIResultDTO()
    apiResultDTO.resultMessage=httpExceptionDTO.detail
    apiResultDTO.resultObject=listHealth
    apiResultDTO.dataError=False
    apiResultDTO.resultToken=tokensDTO
    apiResultDTO.apiException=apiFilterExceptionDTO

    return apiResultDTO

def simulator_api_return():
    apiResultDTO = example_service()
    content = jsonable_encoder(apiResultDTO)
    print((json.dumps(content,indent=4)))
    return JSONResponse(content=content,status_code=200)

simulator_api_return()

