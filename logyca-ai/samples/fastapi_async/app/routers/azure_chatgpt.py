from app.internal.config import settings, get_api_key
from app.schemes.output.model_capabilities_check import ModelCapabilitiesCheck
from logyca_ai import (
    AzureOpenAIChatGPT,
    Content,
    get_content_image_sample,
    get_content_microsoft_sample,
    get_content_pdf_sample,
    get_content_plain_text_sample,
    get_content_simple_sample,
    ImageFileMessage,
    ImageResolution,
    MicrosoftFileMessage,
    PdfFileMessage,
    PlainTextFileMessage,
    TokeniserHelper,
    UserMessage,
)
from fastapi import Depends, APIRouter, Query, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from logyca import APIResultDTO, LogycaStatusEnum
from starlette import status

router = APIRouter(prefix="/api/v1/chatgpt/conversation", tags={"Azure ChatGPT4omni"})

image_supported_formats = f"Image supported formats: {ImageFileMessage.get_supported_formats()}"
pdf_supported_formats = f"Supported formats: {PdfFileMessage.get_supported_formats()}"
plain_text_supported_formats = f"Supported formats: {PlainTextFileMessage.get_supported_formats()}"
microsoft_supported_formats = f"Supported formats: {MicrosoftFileMessage.get_supported_formats()}"

@router.post("/",
    responses={200:{'model':APIResultDTO}},
    summary='To use this endpoint, be guided by the results of the example endpoints.',
    description=f'''
        <ul>
            <h2>Parameters</h2>
            <li>advanced_image_recognition: Used to extract text from images contained within documents using an OCR library. It does not apply to some files such as plain_text. Note: This extraction may consume additional ram memory.</li>
            <li>just_count_tokens: Count the tokens of the messages that will be sent to ChatGPT and return if they meet the capacity of the current model and version.</li>
            <li>just_extract_images: It receives the same standard object but only extracts the images from the documents and returns them in base64, it does not carry out a conversation with chatgpt, therefore all the system and user parameters can be empty.<br>Microsoft and PDF files are supported.</li>
        </ul>
        <ul>
            <h2>Conversations</h2>            
            <li>system: Personality, context, purpose.</li>
            <li>user: type={UserMessage.get_supported_types()}.
                <ul>
                    <li>The type=text is optional for conversation without documents or images.</li>
                </ul>
            </li>
            <li>Definitions for image files
                <ul>
                    <li>Image resolutions: {ImageResolution.content_list()}</li>
                    <li>{image_supported_formats}.
                </ul>
            </li>
            <li>Definitions for pdf files
                <ul>
                    <li>{pdf_supported_formats}.
                </ul>
            </li>
            <li>Definitions for plain text files
                <ul>
                    <li>{plain_text_supported_formats}.
                </ul>
            </li>
            <li>Definitions for Microsoft files
                <ul>
                    <li>{microsoft_supported_formats}.
                </ul>
            </li>
            <li>assistant: These messages contain the responses that the language model generates based on the previous messages in the conversation.</li>
        </ul>
    ''',
    status_code=status.HTTP_200_OK
    )
async def conversation(content:Content, advanced_image_recognition:bool=False,just_count_tokens:bool=False, just_extract_images:bool=False, api_key: str = Depends(get_api_key)):
    chat=AzureOpenAIChatGPT(azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,api_key=settings.OPENAI_API_KEY,api_version=settings.OPENAI_API_VERSION)
    aPIResultDTO=APIResultDTO()

    if just_extract_images:
        messages = chat.build_conversation_message_list(content=content,just_extract_images=just_extract_images)
        aPIResultDTO.resultObject = messages
        return JSONResponse(content=jsonable_encoder(aPIResultDTO.to_dict()),status_code=status.HTTP_200_OK)

    messages = chat.build_conversation_message_list(content=content,advanced_image_recognition=advanced_image_recognition)
    if just_count_tokens is False:
        http_status,respond=await chat.conversation_async(model=settings.AZURE_OPENAI_DEPLOYMENT,messages=messages)
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
    else:
        messages_json = {}
        count=0
        for message in messages:
            messages_json[f"m_{count}"]=message
            count = count + 1
        model_capabilities_check = ModelCapabilitiesCheck(
            model = settings.AZURE_OPENAI_MODEL_NAME,
            version = settings.AZURE_OPENAI_MODEL_VERSION,
            model_capabilities = TokeniserHelper.calculate_tokens_with_model_capabilities(messages_json,settings.AZURE_OPENAI_MODEL_NAME,settings.AZURE_OPENAI_MODEL_VERSION)
        )
        aPIResultDTO.resultObject=model_capabilities_check
        return JSONResponse(content=jsonable_encoder(aPIResultDTO.to_dict()),status_code=status.HTTP_200_OK)

@router.get("/simple_example/",
    responses={200:{'model':Content}},
    summary=f'Scheme example of conversation for endpoint',
    status_code=status.HTTP_200_OK
    )
def simple_example(api_key: str = Depends(get_api_key)):
    return JSONResponse(content=jsonable_encoder(get_content_simple_sample().to_dict()),status_code=status.HTTP_200_OK)

@router.get("/image_example/",
    responses={200:{'model':Content}},
    summary=f'{image_supported_formats}',
    status_code=status.HTTP_200_OK
    )
def image_example(image_sample_base64:bool=False,api_key: str = Depends(get_api_key)):    
    return JSONResponse(content=jsonable_encoder(get_content_image_sample(image_sample_base64).to_dict()),status_code=status.HTTP_200_OK)

@router.get("/pdf_example/",
    responses={200:{'model':Content}},
    summary=f'{pdf_supported_formats}',
    status_code=status.HTTP_200_OK
    )
def pdf_example(pdf_sample_base64:bool=False,api_key: str = Depends(get_api_key)):    
    return JSONResponse(content=jsonable_encoder(get_content_pdf_sample(pdf_sample_base64).to_dict()),status_code=status.HTTP_200_OK)

@router.get("/plain_text_example/",
    responses={200:{'model':Content}},
    summary=f'{plain_text_supported_formats}',
    status_code=status.HTTP_200_OK
    )
def plain_text_example(file_sample_base64:bool=False,api_key: str = Depends(get_api_key)):    
    return JSONResponse(content=jsonable_encoder(get_content_plain_text_sample(file_sample_base64).to_dict()),status_code=status.HTTP_200_OK)

@router.get("/microsoft_file_example/",
    responses={200:{'model':Content}},
    summary=f'{microsoft_supported_formats}',
    status_code=status.HTTP_200_OK
    )
def microsoft_file_example(
    file_sample_base64:bool=False,
    extension: str = Query(..., description="Select one file supported extension", enum=list(MicrosoftFileMessage.get_supported_formats())),
    api_key: str = Depends(get_api_key)):
    return JSONResponse(content=jsonable_encoder(get_content_microsoft_sample(file_sample_base64,extension).to_dict()),status_code=status.HTTP_200_OK)

