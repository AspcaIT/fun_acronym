from unittest import TestCase
from src.tables.user import User
from src.database_connector import create_session


class TestUser(TestCase):
  def test_create_new_user(self):
      u = User(USER_ID=999, NAME="Test User", EMAIL="Test@Test.com", PREFERRED_USERNAME="TEST@TEST.com")
      self.assertIsInstance(u, User)
      self.assertEqual(u.NAME, "Test User")

  def test_table_points_to_roar_schema(self):
      u = User(USER_ID=999, NAME="Test User", EMAIL="Test@Test.com", PREFERRED_USERNAME="TEST@TEST.com")
      self.assertEqual(u.__table__.schema, "ROAR")

  def test_query_for_user(self):
    session = create_session()
    x = session.query(User).filter_by(NAME="Mike Tener").first()
    self.assertEqual(x.NAME, "Mike Tener", "expecting default user in database NAME: Mike Tener")
    self.assertEqual(x.USER_ID, 1, "expecting default user in database USER_ID: 1")
    self.assertEqual(x.EMAIL, "michael.tener@aspca.org",
                     "expecting default user in database EMAIL: michael.tener@aspca.org")

  # Integration tests
  def test_add_new_user_delete_user(self):
    user = User(USER_ID=999, NAME="Test User", EMAIL="Test@Test.com", PREFERRED_USERNAME="TEST@TEST.com")
    session = create_session()
    session.add(user)
    session.commit()
    user_search = session.query(User).filter_by(USER_ID=999).first()
    self.assertEqual( user.NAME, user_search.NAME, "local user object matches database user object")

    session.delete(x)
    session.commit()
    user_does_not_exist = session.query(User).filter_by(USER_ID=999).first()
    self.assertEqual(user_does_not_exist, None, "remote user object deleted from database")




