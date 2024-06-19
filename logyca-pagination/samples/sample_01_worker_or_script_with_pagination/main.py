from app.models.pagination import Pagination
from app.schemes.output.pagination import PaginationOutput
from logyca_pagination import PaginationManager, PaginationParameters, Page
from logyca_postgres import check_connection_sync, SyncConnEngine
from sqlalchemy import select
from sqlalchemy.orm.session import Session
import os

DB_USER=os.getenv('DB_USER','postgres')
DB_PASS=os.getenv('DB_PASS','Psdbtowork')
DB_HOST=os.getenv('DB_HOST','localhost')
DB_PORT=os.getenv('DB_PORT',5432)
DB_NAME=os.getenv('DB_NAME','test')
ssl_enable_like_local_docker_container=False

conn_sync_session=SyncConnEngine(
    url_connection=SyncConnEngine.build_url_connection(user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT,database=DB_NAME,ssl_enable=ssl_enable_like_local_docker_container),
    server_settings=SyncConnEngine.server_settings(pool_size=5,max_overflow=1,pool_recycle=10800,application_name="MyApp - SyncConnEngine")
    )

def methods(sync_session: Session):
    status, date_time_check_conn = check_connection_sync(sync_session)
    if(status):
        pagination_mgr = PaginationManager()
        params=PaginationParameters(page=1,page_size=3)
        query = select(Pagination).order_by(Pagination.id)
        result=pagination_mgr.query_pagination(query,sync_session,params,page_size_limit=100)
        print(f"Dict: {result}")
        data = []
        result:Page=pagination_mgr.query_pagination(query,sync_session,return_dict=False)
        for item in result.items:
            item["created_at"]=str(item["created_at"])
            data.append(PaginationOutput(**item))
        result.items=data
        data_id:PaginationOutput=result.items[0]
        print(f"Object items[0]_id: {data_id.id}")
        print(f"Object items[0]_purchaser: {data_id.purchaser}")
        print(f"Object items[0]_created_at: {data_id.created_at}")
    else:
        print("sync_session connect db error...")
def main():
    for sync_session in conn_sync_session.get_sync_session():
        methods(sync_session)
    conn_sync_session.close_engine()            


if __name__ == "__main__":
    main()