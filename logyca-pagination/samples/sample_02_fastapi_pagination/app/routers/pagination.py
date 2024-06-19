from app.internal.config import conn_sync_session
from app.models.pagination import Pagination
from app.schemes.output.pagination import PaginationOutput
from fastapi import HTTPException, Depends, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from logyca import APIResultDTO
from logyca_pagination import Page,PaginationManager,PaginationParameters
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.sql import between

pagination_mgr=PaginationManager()
router = APIRouter(prefix="/api/v1/pagination", tags={"Pagination"})

@router.get("/id/")
def get_data_by_id_custom_parameters(id:int=0,params:PaginationParameters = Depends(), connection_session: Session = Depends(conn_sync_session)):
    aPIResultDTO=APIResultDTO()
    try:
        if id==0:
            query = select(Pagination).order_by(Pagination.id)
        else:
            query = select(Pagination).where(Pagination.id==id).order_by(Pagination.id)
        aPIResultDTO.resultObject=pagination_mgr.query_pagination(query,connection_session,params,page_size_limit=100)
        return JSONResponse(content=jsonable_encoder(aPIResultDTO))
    except Exception as e:
        aPIResultDTO.dataError=True
        aPIResultDTO.resultMessage=str(e)
        raise HTTPException(status_code=500, detail=jsonable_encoder(aPIResultDTO))

@router.get("/id_with_type_without_count/")
def get_data_by_id_with_type_simularting_repository_layer_without_count(id:int=0,params:PaginationParameters = Depends(), connection_session: Session = Depends(conn_sync_session)):
    aPIResultDTO=APIResultDTO()
    try:
        if id==0:
            query = select(Pagination).order_by(Pagination.id)
            aPIResultDTO.resultObject=pagination_mgr.query_pagination(query,connection_session,params,return_dict=True,count_records=False)
        else:
            """Repository Layer
            To send the type as an object to the service and standardize the dictionary format
            """
            query = select(Pagination).where(Pagination.id==id).order_by(Pagination.id)
            result:Page=pagination_mgr.query_pagination(query,connection_session,params,return_dict=False)
            data = []
            for items in result.items:
                items["id"]=int(items["id"])
                items["created_at"]=str(items["created_at"])
                data.append(PaginationOutput(**items))
            result.items=data
            item:PaginationOutput=result.items[0]
            print(item)
            print(item.created_at)
            aPIResultDTO.resultObject=result
        
        return JSONResponse(content=jsonable_encoder(aPIResultDTO))
    except Exception as e:
        aPIResultDTO.dataError=True
        aPIResultDTO.resultMessage=str(e)
        raise HTTPException(status_code=500, detail=jsonable_encoder(aPIResultDTO))

@router.get("/purchaser/")
def get_data_by_purchaser(purchaser:str="",params:PaginationParameters = Depends(), connection_session: Session = Depends(conn_sync_session)):
    aPIResultDTO=APIResultDTO()
    try:
        if purchaser == "":
            query = select(Pagination)
        else:
            purchaser=f"%{purchaser.strip()}%"
            purchaser=purchaser.replace(" ","%")
            query = select(Pagination).filter(Pagination.purchaser.ilike(purchaser)).order_by(Pagination.id)
        aPIResultDTO.resultObject=pagination_mgr.query_pagination(query,connection_session,params)
        return JSONResponse(content=jsonable_encoder(aPIResultDTO))
    except Exception as e:
        aPIResultDTO.dataError=True
        aPIResultDTO.resultMessage=str(e)
        raise HTTPException(status_code=500, detail=jsonable_encoder(aPIResultDTO))

@router.get("/created_at/")
def get_data_by_created_at_date(start_date:str = "2021-06-18", end_date:str = "2021-06-18",params:PaginationParameters = Depends(), connection_session: Session = Depends(conn_sync_session)):
    aPIResultDTO=APIResultDTO()
    try:
        if start_date == "" or end_date == "":
            query = select(Pagination)
        else:
            start_date=f"{start_date.strip()} 00:00:00"
            end_date=f"{end_date.strip()} 23:59:59"
            query = select(Pagination).where(between(Pagination.created_at, start_date, end_date) )
        aPIResultDTO.resultObject=pagination_mgr.query_pagination(query,connection_session,params)
        return JSONResponse(content=jsonable_encoder(aPIResultDTO))
    except Exception as e:
        aPIResultDTO.dataError=True
        aPIResultDTO.resultMessage=str(e)
        raise HTTPException(status_code=500, detail=jsonable_encoder(aPIResultDTO))

