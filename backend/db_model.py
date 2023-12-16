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
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    mail = Column(String(50),nullable=False,unique=True)
    sex = Column(String(3),nullable=True)
    created_at = Column(DateTime, server_default=current_timestamp())
    