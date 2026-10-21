import pickle
def viewSingleEmployee():
    records=[]
    with open("C:\\Users\\Sai\\Downloads\\Employement Information System\\employeeproj.pick","rb") as fp:
        while True:
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    res=False
    empno=int(input("Enter Employee ID to see the details:"))
    for record in records:
        if(record[0]==empno):
            rec=record
            res=True
            break
    print("-*50")
    if(res):
        print("\tEmployee ID={}".format(rec[0]))
        print("\tEmployee Name={}".format(rec[1]))
        print("\tEmployee CTC={}".format(rec[2]))
    else:
        print("\tEmployee Details Not Found")
    print("-"*50)
def viewAllEmployee():
    with open("C:\\Users\\Sai\\Downloads\\Employement Information System\\employeeproj.pick","rb") as fp:
        print("--"*70)
        print("\tID\tName\tCTC")
        print("--"*70)
        while True:
            try:
                record=pickle.load(fp)
                for val in record:
                    print("\t{}".format(val),end="\t")
                    print()
            except EOFError:
                print("-"*70)
                break

        

