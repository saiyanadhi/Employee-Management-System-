import pickle 
def updateEmployee():
    records=[]
    with open("C:\\Users\\Sai\\Downloads\\Employement Information System\\employeeproj.pick","rb") as fp:
        while (True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    res=False
    empno=int(input("Enter the Employee Number to update:"))
    for i in range(len(records)):
        if (records[i][0]==empno):
            recindex=i
            res=True
            break
    print("-"*50)
    if(res):
        print("\t\tEmployee Deatils exist-valid")
        newsal=float(input("Enter the new Salary:"))
        records[recindex][2]=newsal
        with open("C:\\Users\\Sai\\Downloads\\Employement Information System\\employeeproj.pick","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
    else:
        print("\t\tEmployee Details does not Exist-inavlid")
    print("-"*50)