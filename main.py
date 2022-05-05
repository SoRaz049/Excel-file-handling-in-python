from openpyxl import Workbook, load_workbook

excel_sheet= load_workbook ("D:\\Projects\\Python\\Excel file handling\\account_sheet.xlsx")

work_sheet= excel_sheet.active

sheet1= excel_sheet['Sheet1']

sender=input("Enter the account number of the sender: ")
reciver=input("Enter the account number of the reciptant: ")

