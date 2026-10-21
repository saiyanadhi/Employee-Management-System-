import pickle
def addemp():
    with open("C:\\Users\\Sai\\Downloads\\Employement Information System\\employeeproj.pick","ab") as fp:
        try:
            empno=int(input("Enter the Employee ID:"))
            name=input("Enter the Employee Name:")
            empsal=float(input("Enter the CTC:"))
            lst=list()
            lst.append(empno)
            lst.append(name)
            lst.append(empsal)
            pickle.dump(lst,fp)
            print("\tEmployee details saved Sucessfully")
        except ValueError:
            print("\tDon't Enter The Alnums,strs and Symbols in empsal")





