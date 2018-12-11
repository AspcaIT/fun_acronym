'''
Created on Aug 6, 2018
@author: Lanie.Shannon
'''
import pyodbc
from xlsxwriter import Workbook
import combine2xlsx

conn = pyodbc.connect(r'DSN=Workday_EIB;UID=sqllocal;PWD=IhPCIcbts!')
crsr = conn.cursor()

fd = open('sno_cust_report.sql', 'r')
sql_stmt = fd.read()
fd.close()

# create data
result = crsr.execute(sql_stmt(start_date))

# Get all rows.
rows = result.fetchall()

# Create a workbook and add a worksheet.
workbook = Workbook('sno_cust_test_hold.xlsx')
worksheet = workbook.add_worksheet()

row = 1
col = 0

# Add SQL output to worksheet in the order of the SELECT statement
for row_data in rows:
    worksheet.write_row(row, col, row_data)
    row += 1

workbook.close()

# Append data to headings
combine2xlsx.combine(['put_customer_headers.xlsx', 'sno_cust_test_hold.xlsx'], 'sno_cust_test.xlsx')