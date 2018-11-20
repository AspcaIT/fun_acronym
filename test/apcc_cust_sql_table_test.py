'''
Created on Oct 29, 2018
@author: Lanie.Shannon
'''
import pyodbc
from xlsxwriter import Workbook
import combine2xlsx

conn = pyodbc.connect(r'DSN=AnToxMRT_SQL;UID=db2admin;PWD=1pe567')
crsr = conn.cursor()

fd = open('apcc_cust_sql_table_test.sql', 'r')
sqlStmt = fd.read()
fd.close()

# create data
result = crsr.execute(sqlStmt)

# Get all rows.
rows = result.fetchall()

# Create a workbook and add a worksheet.
workbook = Workbook('apcc_cust_test_hold.xlsx')
worksheet = workbook.add_worksheet()

row = 1
col = 0

# Add SQL output to worksheet in the order of the SELECT statement
for row_data in rows:
    worksheet.write_row(row, col, row_data)
    row += 1

workbook.close()

combine2xlsx.combine(['put_customer_headers.xlsx', 'apcc_cust_test_hold.xlsx'], 'apcc_cust_test.xlsx')