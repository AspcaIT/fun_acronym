'''
Created on Nov 20, 2018
@author: Lanie.Shannon
'''

import os
from xlsxwriter import Workbook
import combine2xlsx
import pyodbc


def finance_reports(report_name, start_date, end_date):
    credentials = database_library(report_name)
    conn = pyodbc.connect(credentials)
    crsr = conn.cursor()

    rep_path = reference_test_file(report_name)
    fd = open(rep_path, 'r')
    sql_stmt = fd.read()
    fd.close()

    # create data
    start_string = start_date.strftime('%Y-%m-%d')
    end_string = end_date.strftime( '%Y-%m-%d' )
    sql_param = str(sql_stmt).replace('$$start_date', start_string).replace('$$end_date', end_string)
    result = crsr.execute(sql_param)
    # Get all rows.
    rows = result.fetchall()

    ## New Method / Class called Report Generator
    # Create a workbook and add a worksheet.
    workbook = Workbook(reference_test_file('hold_data.xlsx'))
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
    sno_cust_hold = reference_test_file('hold_data.xlsx')
    sno_cust_test = reference_test_file('output_report.xlsx')
    combine2xlsx.combine([header_file, sno_cust_hold], sno_cust_test)


def reference_test_file(file_name):
    return os.path.join(os.path.dirname(__file__), "../test/"+file_name)


def database_library(reference):
    # Remove hardcoded passwords to ENV file
    dl = {
        "sno_cust_report.sql": r'DSN=Workday_EIB;UID=sqllocal;PWD=IhPCIcbts!',
        "apcc_cust_sql_table_test.sql": r'DSN=AnToxMRT_SQL;UID=db2admin;PWD=1pe567'
    }
    return dl[reference]

