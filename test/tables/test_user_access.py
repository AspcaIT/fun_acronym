from unittest import TestCase
from src.tables.user_access import UserAccess
from src.database_connector import create_session


class TestUser(TestCase):
  def test_create_new_user_access(self):
      u = UserAccess(user_access_id=1234, user_id="Test User", user_access_group_type_id=4321)
      self.assertIsInstance(u, UserAccess)
      self.assertEqual(u.user_access_id, 1234)
      self.assertEqual(u.user_id, "Test User")
      self.assertEqual(u.user_access_group_type_id, 4321)

  def test_table_points_to_roar_schema(self):
      u = UserAccess(user_access_id=1234, user_id="Test User", user_access_group_type_id=4321)
      self.assertEqual(u.__table__.schema, "ROAR")

  def test_query_for_user(self):
    session = create_session()
    x = session.query(UserAccess).filter_by(user_id="michael.tener").first()
    self.assertEqual(x.user_access_id, 414, "expecting default user in database user_access_id: 414")
    self.assertEqual(x.user_id.strip(), 'michael.tener', "expecting default user in database user_id: michael.tener")
    self.assertEqual(x.user_access_group_type_id, 2,
                     "expecting default user in database user_access_group_type_id: 2")

  # Integration tests
  # def test_add_new_user_delete_user(self):
  #   user = User(user_id=999, name="Test User", email="Test@Test.com", preferred_username="TEST@TEST.com")
  #   session = create_session()
  #   session.add(user)
  #   session.commit()
  #   user_search = session.query(User).filter_by(user_id=999).first()
  #   self.assertEqual( user.name, user_search.name, "local user object matches database user object")
  #
  #   session.delete(user_search)
  #   session.commit()
  #   user_does_not_exist = session.query(User).filter_by(user_id=999).first()
  #   self.assertEqual(user_does_not_exist, None, "remote user object deleted from database")




