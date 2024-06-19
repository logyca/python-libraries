from datetime import datetime
from logyca_postgres import SyncDeclarativeBaseORM
from sqlalchemy import Column, Integer, String, DateTime

class Pagination(SyncDeclarativeBaseORM):
    __tablename__ = "pagination"

    id = Column(Integer, primary_key=True, index=True)
    purchaser = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.now())