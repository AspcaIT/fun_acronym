from sqlalchemy import Column, Integer, String, Sequence
from src.tables.base import Base

# This file should only contain references to the table on the ROAR database.

class UserAccessGroupType(Base):
  __tablename__ = "USER_ACCESS_GROUP_TYPE_TEST"
  user_access_group_type_id = Column(String, Sequence('user_access_group_type_id'), primary_key=True)
  user_access_group_type_name = Column(String)

