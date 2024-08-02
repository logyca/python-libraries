from internal.config import settings
from utils.helpers.azure_openai_chatgpt import AzureOpenAIChatGPT
from utils.schemes.output.conversations import Conversation
from utils.schemes.input.conversations_content_types import ContentImage
from utils.constants.content import ContentRole
import asyncio
import json


print(ContentRole.find_by_key("ASK"))

async def main():
    chat=AzureOpenAIChatGPT(azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,api_key=settings.OPENAI_API_KEY,api_version=settings.OPENAI_API_VERSION)

    context="""
        Actua como un experto en venta de frutas.
        Se muy positivo.
        Trata a las personas de usted, nunca tutees sin importar como te escriban.
        """    

    messages = chat.build_conversation_message_list(context=context)
    http_status,respond=await chat.conversation_async(model=settings.AZURE_OPENAI_DEPLOYMENT,messages=messages)
    if isinstance(respond,Conversation):
        print(f"http_status={http_status}")
        print(f"respond={json.dumps(respond.to_dict(),indent=4)}")
        print(f"respond={respond.answer}")
        print(f"usage_data={json.dumps(respond.usage_data.to_dict(),indent=4)}")
    else:
        raise Exception(f"http_status={http_status},respond={respond}")
    
asyncio.run(main())

