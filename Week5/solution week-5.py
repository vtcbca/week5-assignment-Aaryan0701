import csv
with open("c:/Sqlite/csv/student.csv","w",newline="") as f:
    w=csv.writer(f)
    header=['SID','SNAME','CITY','CONTACT']
    w.writerow(header)
    data=[[1,'Aryan','Vyara',9898989898],
              [2,'Param','Surat',9797979797],
              [3,'Meet','Surat',9696969696],
              [4,'Mann','Bardoli',9595959595],
              [5,'Dhruv','Songadh',9494949494]]
    w.writerows(data)
    s_list=[]
    for i in range(5):
        sid=int(input("Enter id:"))
        sname=input("Enter name:")
        city=input("Enter city:")
        contact=int(input("Enter contact:"))
        sub_list=[sid,sname,city,contact]
        s_list.append(sub_list)
    w.writerows(s_list)
with open("c:/Sqlite/csv/student.csv","r") as f_read:
    r=csv.reader(f_read)
    for i in r:
        print(i)
    
