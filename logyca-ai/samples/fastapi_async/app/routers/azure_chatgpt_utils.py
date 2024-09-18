from app.internal.config import settings, get_api_key
from app.schemes.output.model_capabilities_check import ModelCapabilitiesCheck
from logyca_ai import (
    Content,
    TokeniserHelper,
)
from fastapi import Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from logyca import APIResultDTO
from starlette import status
from typing import Union

router = APIRouter(prefix="/api/v1/chatgpt/utils", tags={"Azure ChatGPT Utils"})

@router.get("/get_model_capabilities/",
    responses={200:{'model':Content}},
    summary='Get the current supported capabilities of the models',
    description=f'''
    ''',
    status_code=status.HTTP_200_OK
    )
def get_model_capabilities(api_key: str = Depends(get_api_key)):
    aPIResultDTO=APIResultDTO()
    aPIResultDTO.resultObject=TokeniserHelper.get_model_capabilities()
    return JSONResponse(content=jsonable_encoder(aPIResultDTO.to_dict()),status_code=status.HTTP_200_OK)


@router.post("/get_tokens_with_model_capabilities/",
    responses={200:{'model':Content}},
    summary='Get tokens with model capabilities',
    description=f'''
        <ul>
            <h2>Parameters</h2>
            <li>message: Text string or json dictionary to count the tokens and validate if they meet the capacity of the model.</li>
        </ul>
    ''',
    status_code=status.HTTP_200_OK
    )
def get_tokens_with_model_capabilities(message: Union[str, dict], api_key: str = Depends(get_api_key)):
    aPIResultDTO=APIResultDTO()
    model_capabilities_check = ModelCapabilitiesCheck(
        model = settings.AZURE_OPENAI_MODEL_NAME,
        version = settings.AZURE_OPENAI_MODEL_VERSION,
        model_capabilities = TokeniserHelper.calculate_tokens_with_model_capabilities(message,settings.AZURE_OPENAI_MODEL_NAME,settings.AZURE_OPENAI_MODEL_VERSION)
    )
    aPIResultDTO.resultObject=model_capabilities_check.to_dict()
    return JSONResponse(content=jsonable_encoder(aPIResultDTO.to_dict()),status_code=status.HTTP_200_OK)

