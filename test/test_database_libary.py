from unittest import TestCase
from fun_acronym.src.database_connector import database_libary

class TestDatabase_libary( TestCase ):
    def test_database_libary(self):
        self.assertTrue(True == True, "this works")

    def test_database_library_cust_report(self, database_library=None):
        database_library("sno_cust_report.sql")


