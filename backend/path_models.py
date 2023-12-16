from sqlalchemy import Column, Integer, String, DateTime, Sequence
from path_settings import ENGINE, Base
from datetime import datetime
import sys


class User(Base):
    """
    UserModel
    """
    __tablename__ = 'nmaa'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(255))
    age = Column(Integer)
    created_at = Column('created', DateTime, default=datetime.now, nullable=False)
    updated_at = Column('modified', DateTime, default=datetime.now, nullable=False)


def main(args):
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main(sys.argv)