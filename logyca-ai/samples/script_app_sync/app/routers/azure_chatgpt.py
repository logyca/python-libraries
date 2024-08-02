from app.internal.config import settings,get_api_key

from logyca_ai import (
    AzureOpenAIChatGPT,
    Content,
    get_content_image_sample,
    get_content_pdf_sample,
    get_content_simple_sample,
    ImageMessage,
    ImageResolution,
    PDFMessage,
    UserMessage,
)

from fastapi import Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from logyca import APIResultDTO, LogycaStatusEnum
from starlette import status

router = APIRouter(prefix="/api/v1/chatgpt/conversation", tags={"Azure ChatGPT4omni"})

@router.post("/",
    responses={200:{'model':APIResultDTO}},
    summary='To use this endpoint, be guided by the results of the example endpoints.',
    description=f'''
        Conversations:
        <ul>
            <li>system: Personality, context, purpose.</li>
            <li>user: type={UserMessage.get_supported_types()}.
                <ul>
                    <li>The type=text is optional for conversation without documents or images.</li>
                </ul>
            </li>
            <li>Definitions for image files
                <ul>
                    <li>Image resolutions: {ImageResolution.content_list()}</li>
                    <li>Image supported formats: {ImageMessage.get_supported_formats()}.
                </ul>
            </li>
            <li>Definitions for pdf files
                <ul>
                    <li>PDF supported formats: {PDFMessage.get_supported_formats()}.
                </ul>
            </li>
            <li>assistant: These messages contain the responses that the language model generates based on the previous messages in the conversation.</li>
        </ul>
    ''',
    status_code=status.HTTP_200_OK
    )
async def conversation(content:Content, api_key: str = Depends(get_api_key)):
    chat=AzureOpenAIChatGPT(azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,api_key=settings.OPENAI_API_KEY,api_version=settings.OPENAI_API_VERSION)
    messages = chat.build_conversation_message_list(content=content)
    http_status,respond=await chat.conversation_async(model=settings.AZURE_OPENAI_DEPLOYMENT,messages=messages)
    aPIResultDTO=APIResultDTO()
    if http_status == status.HTTP_200_OK:
        aPIResultDTO.resultObject=respond.to_dict()
        return JSONResponse(content=jsonable_encoder(aPIResultDTO.to_dict()),status_code=http_status)
    else:
        aPIResultDTO.dataError=True
        aPIResultDTO.resultMessage=respond
        aPIResultDTO.apiException.message=respond
        aPIResultDTO.apiException.status=http_status
        aPIResultDTO.apiException.logycaStatus=LogycaStatusEnum.from_http_status_code(http_status)
        return JSONResponse(content=jsonable_encoder(aPIResultDTO.to_dict()),status_code=http_status)

@router.get("/simple_sample/",
    responses={200:{'model':Content}},
    summary='Scheme example of conversation for endpoint',
    status_code=status.HTTP_200_OK
    )
def simple_sample(api_key: str = Depends(get_api_key)):
    return JSONResponse(content=jsonable_encoder(get_content_simple_sample().to_dict()),status_code=status.HTTP_200_OK)

@router.get("/image_sample/",
    responses={200:{'model':Content}},
    summary='Scheme example of conversation for endpoint',
    status_code=status.HTTP_200_OK
    )
def simple_sample(image_sample_base64:bool=False,api_key: str = Depends(get_api_key)):    
    return JSONResponse(content=jsonable_encoder(get_content_image_sample(image_sample_base64).to_dict()),status_code=status.HTTP_200_OK)

@router.get("/pdf_sample/",
    responses={200:{'model':Content}},
    summary='Scheme example of conversation for endpoint',
    status_code=status.HTTP_200_OK
    )
def pdf_sample(pdf_sample_base64:bool=False,api_key: str = Depends(get_api_key)):    
    return JSONResponse(content=jsonable_encoder(get_content_pdf_sample(pdf_sample_base64).to_dict()),status_code=status.HTTP_200_OK)

