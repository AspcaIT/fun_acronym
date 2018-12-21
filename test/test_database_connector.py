from unittest import TestCase
from src.database_connector import *


class TestDatabaseConnector(TestCase):
    def test_database_library(self):
        self.assertTrue(True, "checks to see if test suite is running")

    def test_database_library_cust_report(self):
        self.assertEqual(database_library("sno_cust_report.sql"), 'DSN=Workday_EIB;UID=sqllocal;PWD=IhPCIcbts!', 'should return connection credentials')
        self.assertEqual(database_library("apcc_cust_sql_table_test.sql"), r'DSN=AnToxMRT_SQL;UID=db2admin;PWD=1pe567', 'should return connection credentials')
        # self.assertIsInstance(database_library("I don't exist"), KeyError, "this should return an error")

    def test_happy(self):
        finance_reports("sno_cust_report.sql","test","test")
