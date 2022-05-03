import openpyxl

excel_sheet= openpyxl.load_workbook ("D:\\Projects\\Python\\Excel file handling\\account_sheet.xlsx")

excel_sheet.active.title

sheet1= excel_sheet['Sheet1']
