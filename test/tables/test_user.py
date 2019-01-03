from unittest import TestCase
from src.tables.user import User
from src.database_connector import create_session


class TestUser(TestCase):
  def test_create_new_user(self):
      u = User(user_id=999, name="Test User", email="Test@Test.com", preferred_username="TEST@TEST.com")
      self.assertIsInstance(u, User)
      self.assertEqual(u.name, "Test User")
      self.assertEqual(u.user_id, 999)
      self.assertEqual(u.email, "Test@Test.com")
      self.assertEqual(u.preferred_username, "TEST@TEST.com")

  def test_table_points_to_roar_schema(self):
      u = User(user_id=999, name="Test User", email="Test@Test.com", preferred_username="TEST@TEST.com")
      self.assertEqual(u.__table__.schema, "ROAR")

  def test_query_for_user(self):
    session = create_session()
    x = session.query(User).filter_by(name="Mike Tener").first()
    self.assertEqual(x.name, "Mike Tener", "expecting default user in database NAME: Mike Tener")
    self.assertEqual(x.user_id, 1, "expecting default user in database USER_ID: 1")
    self.assertEqual(x.email, "michael.tener@aspca.org",
                     "expecting default user in database EMAIL: michael.tener@aspca.org")

  # Integration tests
  def test_add_new_user_delete_user(self):
    user = User(user_id=999, name="Test User", email="Test@Test.com", preferred_username="TEST@TEST.com")
    session = create_session()
    session.add(user)
    session.commit()
    user_search = session.query(User).filter_by(user_id=999).first()
    self.assertEqual( user.name, user_search.name, "local user object matches database user object")

    session.delete(user_search)
    session.commit()
    user_does_not_exist = session.query(User).filter_by(user_id=999).first()
    self.assertEqual(user_does_not_exist, None, "remote user object deleted from database")




