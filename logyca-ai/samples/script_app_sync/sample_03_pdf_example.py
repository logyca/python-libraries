from app.internal.config import settings
from logyca import APIResultDTO, LogycaStatusEnum
from logyca_ai import (
    AzureOpenAIChatGPT,
    get_content_pdf_sample,
)
from starlette import status
import json

if __name__ == "__main__":
    chat=AzureOpenAIChatGPT(azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,api_key=settings.OPENAI_API_KEY,api_version=settings.OPENAI_API_VERSION)
    is_base64=False # To obtain from example the content in base64
    content = get_content_pdf_sample(pdf_sample_base64=is_base64)
    print(json.dumps(content.to_dict(),indent=4))

    chat=AzureOpenAIChatGPT(azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,api_key=settings.OPENAI_API_KEY,api_version=settings.OPENAI_API_VERSION)
    messages = chat.build_conversation_message_list(content=content,advanced_image_recognition=False)
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
