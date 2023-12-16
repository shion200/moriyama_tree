# -*- coding: utf-8 -*-

# sqlalchemyライブラリから使用する型などをインポート
from sqlalchemy import Column, Integer, String,DateTime
# CURRENT_TIMESTAMP関数を利用するためにインポート
from sqlalchemy.sql.functions import current_timestamp
# Baseクラス作成用にインポート
from sqlalchemy.ext.declarative import declarative_base

# Baseクラスを作成
Base = declarative_base()

# Baseクラスを継承したモデルを作成
# usersテーブルのモデルUsers
class Users(Base):
    __tablename__ = 'users'
    name = Column(String(100), primary_key=True)
    password = Column(String(50),nullable=False,unique=True)
    url_num = Column(Integer, nullable=False, default=0)
    url = Column(String(1000),nullable=True)
    created_at = Column(DateTime, server_default=current_timestamp())

    # password = Column(String(20), nullable=False)
    # url_num = Column(String(3), nullable= False)
    