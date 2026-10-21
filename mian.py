from addemp import addemp
from EmpMenu import menu
from empview import viewAllEmployee,viewSingleEmployee
from empsearch import searchEmployee
from empdelete import empdelete
from empupdate import updateEmployee
while(True):
    try:
        menu()
        ch=int(input("Enter your choice:"))
        match(ch):
            case 1:
                addemp()
            case 2:
                empdelete()
            case 3:
                updateEmployee()
            case 4:
                viewSingleEmployee()
            case 5:
                viewAllEmployee()
            case 6:
                searchEmployee()
            case 7:
                print("\tThanks for Using")
                break
            case _:
                print("Inavlid Input Try again")
    except ValueError:
        print("\tDon't Enter Alnums,Strs and Symbols -Try Again")

