import pandas as pd
from pandas import ExcelWriter

xmlname="/Users/SUHAS/PycharmProjects/untitled/data/data.xls"

df = pd.DataFrame({'Name': ["Muni", "Kaali", "Rajesh", "Arul", "Raja"],
                   'Age': [35, 36, 36, 28, 41]})

df1 = pd.DataFrame({'Name': ["Muni", "Kaali", "Rajesh", "Arul", "Raja"],
                   'Salary': [35000, 36000, 36000, 28000, 41000]})

writer = ExcelWriter(xmlname)

df.to_excel(writer, 'emp', index=False)
df1.to_excel(writer, 'empfur', index=False)

writer.save()