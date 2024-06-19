from pydantic import BaseModel,Field

class PaginationOutput(BaseModel):
    id:int=Field(default=0)
    purchaser:str=Field(default='')
    created_at:str=Field(default='')
