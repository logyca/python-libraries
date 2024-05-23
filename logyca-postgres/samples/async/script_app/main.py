from logyca_postgres import AsyncConnEngine, commit_rollback_async, check_connection_async
from sqlalchemy import text as text_to_sql
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
import os

DB_USER=os.getenv('DB_USER','postgres')
DB_PASS=os.getenv('DB_PASS','xxx')
DB_HOST=os.getenv('DB_HOST','localhost')
DB_PORT=os.getenv('DB_PORT',5432)
DB_NAME=os.getenv('DB_NAME','test')
ssl_enable_like_local_docker_container=False

conn_async_session=AsyncConnEngine(
    url_connection=AsyncConnEngine.build_url_connection(user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT,database=DB_NAME,ssl_enable=ssl_enable_like_local_docker_container),
    server_settings=AsyncConnEngine.server_settings(pool_size=5,max_overflow=1,pool_recycle=10800,application_name="MyApp - AsyncConnEngine")
            )

'''
The connection pool (pool_size) after the first query will remain open until the application is stopped or the engine is terminated: close_engine().
'''

async def methods(async_session:AsyncSession):
    status, date_time_check_conn = await check_connection_async(async_session)
    if(status):
        query = text_to_sql("SELECT now();")
        result = await async_session.execute(query)
        simulated_query = result.scalar_one_or_none()
        await commit_rollback_async(async_session)
        print(f"date_time_check_conn={date_time_check_conn},simulated_query={simulated_query}")
    else:
        print("async_session connect db error...")
async def main():
    async for async_session in conn_async_session.get_async_session():
        await methods(async_session)
    await conn_async_session.close_engine()

if __name__ == "__main__":
    asyncio.run(main())
