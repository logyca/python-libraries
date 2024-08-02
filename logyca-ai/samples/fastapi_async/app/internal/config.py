from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from logyca import APIKeyScheme, APIKey
from pathlib import Path
import os

env_path= Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    def __init__(self) -> None:
        self.AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
        self.OPENAI_API_VERSION: str = os.getenv("OPENAI_API_VERSION")
        self.AZURE_OPENAI_DEPLOYMENT: str = os.getenv("AZURE_OPENAI_DEPLOYMENT")
        self.API_KEY: str = os.getenv("API_KEY")

        self.mandatory_attribute_validation()

    def mandatory_attribute_validation(self):
        attributes = vars(self)
        self.none_attributes = [attr for attr, value in attributes.items() if value is None]

settings = Settings()

if len(settings.none_attributes)!=0:
    raise Exception(f"Missing required parameters: {settings.none_attributes}")

settings_api_key=APIKeyScheme(key=settings.API_KEY, enable=False)
get_api_key = APIKey(settings_api_key)