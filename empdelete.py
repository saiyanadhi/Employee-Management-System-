import pickle
def empdelete():
    records=[]
    with open("C:\\Users\\Sai\\Downloads\\Employement Information System\\employeeproj.pick","rb") as fp:
        while (True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    res=False
    empno=int(input("Enter the Employee Number to delete:"))
    for i in range(len(records)):
        if (records[i][0]==empno):
            recindex=i
            res=True
            break
    print("-"*50)
    if(res):
        records.pop(recindex)
        with open("C:\\Users\\Sai\\Downloads\\Employement Information System\\employeeproj.pick","wb") as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\t\tEmployee Dteails Deleted sucessfully--verify")
    else:
        print("\t\tEmployee Details does not Exist-inavlid")
    print("-"*50)

            