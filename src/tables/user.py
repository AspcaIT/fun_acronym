from sqlalchemy import MetaData,Column, Integer, String, create_engine, Sequence
from src.database_connector import sql_alchemy_connection_config
from src.tables.base import Base

class User(Base):
  __tablename__ = "USER_TEST"
  USER_ID = Column(Integer, Sequence('user_id'), primary_key=True)
  NAME = Column(String)
  EMAIL = Column(String)
  PREFERRED_USERNAME = Column(String)

