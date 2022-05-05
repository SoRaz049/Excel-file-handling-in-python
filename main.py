from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

acc_list=[]

wb= load_workbook ("D:\\Projects\\Python\\Excel file handling\\account_sheet.xlsx")

ws= wb.active

#s1= excel_sheet['Sheet1']



#eciver=input("Enter the account number of the reciptant: ")

for col in range (2,3):
    for row in range (2,11):
        char = get_column_letter( col )
        
        acc_no= ws [char + str(row)].value
        acc_list.append(acc_no)
        

print(acc_list)
        
sender=int(input("Enter the account number of the sender: "))

if sender in acc_list:
    print ("valid")

else:
    print("Invalid")
    