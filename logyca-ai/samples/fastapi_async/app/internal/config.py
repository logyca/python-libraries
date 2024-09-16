from dotenv import load_dotenv
from logyca import APIKeyScheme, APIKey
from pathlib import Path
import os

env_path= Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    def __init__(self) -> None:
        self.API_KEY: str = os.getenv("API_KEY")
        self.AZURE_OPENAI_DEPLOYMENT: str = os.getenv("AZURE_OPENAI_DEPLOYMENT")
        self.AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.AZURE_OPENAI_MODEL_NAME: str = os.getenv("AZURE_OPENAI_MODEL_NAME")
        self.AZURE_OPENAI_MODEL_VERSION: str = os.getenv("AZURE_OPENAI_MODEL_VERSION")
        self.OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
        self.OPENAI_API_VERSION: str = os.getenv("OPENAI_API_VERSION")

        self.mandatory_attribute_validation()

    def mandatory_attribute_validation(self):
        attributes = vars(self)
        self.none_attributes = [attr for attr, value in attributes.items() if value is None]

settings = Settings()

if len(settings.none_attributes)!=0:
    raise Exception(f"Missing required parameters: {settings.none_attributes}")

settings_api_key=APIKeyScheme(key=settings.API_KEY, enable=True)
get_api_key = APIKey(settings_api_key)
