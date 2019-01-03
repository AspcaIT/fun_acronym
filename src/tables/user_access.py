from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from src.tables.base import Base

# This file should only contain references to the table on the ROAR database.

class UserAccess(Base):
  __tablename__ = "USER_ACCESS_TEST"
  user_access_id = Column(Integer, Sequence('user_access_id'), primary_key=True)
  user_id = Column(String, ForeignKey("user_test.name"))
  user_access_group_type_id = Column(Integer, ForeignKey("user_access_group_type_test.user_access_group_type_id"))

