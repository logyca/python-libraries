from logyca_postgres import SyncConnEngine
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