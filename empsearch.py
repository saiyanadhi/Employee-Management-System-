import pickle
def searchEmployee():
    records=[]
    with open("C:\\Users\\Sai\\Downloads\\Employement Information System\\employeeproj.pick","rb") as fp:
        while (True):
            try:
                records=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    res=False
    empno=int(input("Enter the Employee Number to search:"))
    for record in records:
        if (record[0]==empno):
            res=True
        print("-"*50)
        if(res):
            print("\t\tEmployee Details Exist-valid")
        else:
            print("\t\tEmployee Details does not Exist-inavlid")
        print("-"*50)

