from app.internal.config import settings
from logyca import APIResultDTO, LogycaStatusEnum
from logyca_ai import (
    AzureOpenAIChatGPT,
    get_content_simple_sample,
)
from starlette import status
import json

if __name__ == "__main__":
    chat=AzureOpenAIChatGPT(azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,api_key=settings.OPENAI_API_KEY,api_version=settings.OPENAI_API_VERSION)
    content = get_content_simple_sample()
    print(json.dumps(content.to_dict(),indent=4))

    chat=AzureOpenAIChatGPT(azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,api_key=settings.OPENAI_API_KEY,api_version=settings.OPENAI_API_VERSION)
    messages = chat.build_conversation_message_list(content=content)
    http_status,respond=chat.conversation_sync(model=settings.AZURE_OPENAI_DEPLOYMENT,messages=messages)
    aPIResultDTO=APIResultDTO()
    if http_status == status.HTTP_200_OK:
        aPIResultDTO.resultObject=respond.to_dict()
        print(json.dumps(aPIResultDTO.to_dict(),indent=4))
    else:
        aPIResultDTO.dataError=True
        aPIResultDTO.resultMessage=respond
        aPIResultDTO.apiException.message=respond
        aPIResultDTO.apiException.status=http_status
        aPIResultDTO.apiException.logycaStatus=LogycaStatusEnum.from_http_status_code(http_status)
        print(json.dumps(aPIResultDTO.to_dict(),indent=4))
