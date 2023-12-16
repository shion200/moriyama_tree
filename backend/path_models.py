
# sqlalchemyライブラリから使用する型などをインポート
from sqlalchemy import Column, Integer, String,DateTime
# CURRENT_TIMESTAMP関数を利用するためにインポート
from sqlalchemy.sql.functions import current_timestamp
# Baseクラス作成用にインポート
from sqlalchemy.ext.declarative import declarative_base

# Baseクラスを作成
Base = declarative_base()


class Users(Base):
    __tablename__ = 'path'
    id = Column(Integer, primary_key=True, autoincrement = True)
    path = Column(String(255))
    name = Column(String(100))
    created_at = Column(DateTime, server_default=current_timestamp())