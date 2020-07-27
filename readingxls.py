import pandas as pd
from xlrd import sheet

xlsname="/Users/SUHAS/PycharmProjects/untitled/data/data.xls"

xls = pd.ExcelFile(xlsname)

trig_values = xls.parse('emp', index_col=None,na_values=['NA'])
print(trig_values)
trig_values = xls.parse('empfur', index_col=None,na_values=['NA'])
print(trig_values)
"""
row = sheet.row(1)# Selecting the second row
row.write(0,'2nd Row and 1st Column')
row.write(1,'1st Row and 2nd Column')

sheet = xlsname.sheet_by_name('emp')"""

