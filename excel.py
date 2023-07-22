import pandas as pd
import xlrd

file = pd.ExcelFile("/Users/kalek/OneDrive/Desktop/sales.xlsx")
print(file.sheet_names)

sheet = file.parse('sales')
print(sheet)