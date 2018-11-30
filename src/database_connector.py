'''
Created on Nov 20, 2018
@author: Lanie.Shannon
'''
import pyodbc
import os
from xlsxwriter import Workbook
import combine2xlsx


def finance_test(rep_name):
    conn = database_libary(rep_name)
    crsr = conn.cursor()
    print(rep_name)
    qwerasdf = reference_test_file(rep_name)
    fd = open(qwerasdf, 'r')
    sql_stmt = fd.read()
    fd.close()
    # create data
    result = crsr.execute(sql_stmt)
    # Get all rows.
    rows = result.fetchall()
    # Create a workbook and add a worksheet.
    workbook = Workbook(reference_test_file('cust_test_hold.xlsx'))
    worksheet = workbook.add_worksheet()
    row = 1
    col = 0
    # Add SQL output to worksheet in the order of the SELECT statement
    for row_data in rows:
        worksheet.write_row(row, col, row_data)
        row += 1
    workbook.close()
    # Append data to headings
    header_file = reference_test_file('put_customer_headers.xlsx')
    sno_cust_hold = reference_test_file('sno_cust_test_hold.xlsx')
    sno_cust_test = reference_test_file('output.xlsx')
    combine2xlsx.combine([header_file, sno_cust_hold], sno_cust_test)


def reference_test_file(file_name):
    return os.path.join(os.path.dirname(__file__), "../test/"+file_name)


def database_libary(reference):
    if reference == "sno_cust_report.sql":
        return pyodbc.connect(r'DSN=Workday_EIB;UID=sqllocal;PWD=IhPCIcbts!')
    elif reference == "apcc_cust_sql_table_test.sql":
        return pyodbc.connect(r'DSN=AnToxMRT_SQL;UID=db2admin;PWD=1pe567')
    else:
        print('no reference input, use workday or antox')

