from sqlalchemy import Column, Integer, String, Sequence
from src.tables.base import Base

# This file should only contain references to the table on the ROAR database.

class User(Base):
  __tablename__ = "USER_TEST"
  user_id = Column(Integer, Sequence('user_id'), primary_key=True)
  name = Column(String)
  email = Column(String)
  preferred_username = Column(String)

