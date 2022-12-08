'''
f=open("data.txt")
print(f.read(5))
print(f.read(10))
print(f.readline())
print(f.readlines())
str="Hello World Welcome in the class"
tokens=str.split(" ")
print(tokens[0])

'''
def loadStudentData(filename):
    fr=open(filename)
    lines=fr.readlines()
    studentsData=[]
    for line in lines:
        record=line.split(",")
        if len(record)>=4:
            rollno=record[0]
            name = record[1]
            semmester = record[2]
            cgpa = record[3]
            dict_stu={"rollno":rollno,"name":name}
            dict_stu.update(semmester=semmester)
            dict_stu.update(cgpa=cgpa)
            studentsData.append(dict_stu)

    return studentsData
'''
data=loadStudentData("data.txt")
for d in data:
    print(d)

f2=open("mydata.txt","a")
#f2.write("Hello World")
#f2.write("I have written on file")
#f2.write("today its Thursday")
#f2.write("Tomorrow will be Friday \n")
#f2.write("Then Tomorrow will be Saturday \n")
str1="BITF19M009,Fatima,5,3.5\n"
str2="BITF19M010,Aqifa,5,3.7\n"
str3="BITF19M011,Zaina,5,3.5\n"
str4="BITF19M012,Abiha,5,3.5\n"
mydata=[]
mydata.append(str1)
mydata.append(str2)
mydata.append(str3)
mydata.append(str4)
f2.writelines(mydata)
f2.close()
'''
def dumpStudentData(filename,studentData):
    try:
        f=open(filename,"a")
        records=[]
        for student in studentData:
            print(student)
            rollno=student["rollno"]
            name = student["name"]
            semmester = str(student["semmester"])
            cgpa = str(student["cgpa"])
            record=rollno+","+name+","+semmester+","+cgpa+" \n"
            print(record)
            records.append(record)
        f.writelines(records)
    except Exception as e:
        print(str(e))
    finally:
        f.close()


record1={"rollno":"BITF19M015","name":"Bilal","semmester":5,"cgpa":2.5}
record2={"rollno":"BITF19M016","name":"Kashif","semmester":5,"cgpa":2.5}
record3={"rollno":"BITF19M017","name":"Roohi","semmester":5,"cgpa":2.5}
record4={"rollno":"BITF19M018","name":"Anaya","semmester":5,"cgpa":2.5}
list_=[record1,record2,record3,record4]
dumpStudentData("data.txt",list_)
#str=record1["rollno"]+","+record1["name"]+","+record1["cgpa"]+" \n"
#print(str)
data=loadStudentData("data.txt")
for d in data:
    print(d)
