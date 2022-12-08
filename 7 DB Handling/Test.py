from Classes import Student

import pymysql
def selectAllData():
    studentlist=[]
    mydb=None
    mydbCursor=None
    try:
        mydb = pymysql.connect(host="localhost", user="root", password="Chalbhag@1", database="raza")
        # Get cursor object
        mydbCursor = mydb.cursor()
        mydbCursor.execute("select * from students;")
        data=mydbCursor.fetchall()
        for d in data:
            s=Student(d[0],d[1],float(d[2]))
            studentlist.append(s)
    except Exception as e:
        print("In Fetch Student got exception",str(e))
    finally:
        if  mydbCursor!=None:
            mydbCursor.close()
        if mydb !=None:
            mydb.close()
    return studentlist


def insertStudent(student):
    mydb=None
    mydbCursor=None
    try:
        mydb = pymysql.connect(host="localhost", user="root", password="Chalbhag@1", database="raza")
        # Get cursor object
        mydbCursor = mydb.cursor()
        query="insert into students(name,rollno,cgpa) values(%s,%s,%s)"
        args=(student.name,student.rollno,student.cgpa)
        mydbCursor.execute(query,args)
        #print(mydbCursor.fetchone())
        mydb.commit()
    except Exception as e:
        print("In Insert Student got exception", str(e))
    finally:
        if mydbCursor != None:
            mydbCursor.close()
        if mydb != None:
            mydb.close()

def updateStudentByRollNumber(rollno,student):
    mydb = None
    mydbCursor = None
    try:
        mydb = pymysql.connect(host="localhost",user="root", password="Chalbhag@1", database="raza")
        # Get cursor object
        mydbCursor = mydb.cursor()
        query = "update students set name=%s , cgpa=%s where rollno=%s"
        args = (student.name,  student.cgpa ,rollno)
        mydbCursor.execute(query, args)
        mydb.commit()
    except Exception as e:
        print("In updateStudentByRollNumber Student got exception", str(e))
    finally:
        if mydbCursor != None:
            mydbCursor.close()
        if mydb != None:
            mydb.close()

def insertStudentmultipleinDB():
    n=input("Enter number of Students: ")
    for i in range(int(n)):
        name=input("Enter Name: ")
        rollno = input("Enter rollno: ")
        cgpa = input("Enter CGPA: ")
        s=Student(name,rollno,cgpa)
        insertStudent(s)

def deleteStudentByRollNumber(rollno):
    mydb = None
    mydbCursor = None
    try:
        mydb = pymysql.connect(host="localhost",user="root", password="Chalbhag@1", database="raza")
        # Get cursor object
        mydbCursor = mydb.cursor()
        query = "delete from students where rollno = %s"
        args = (rollno)
        mydbCursor.execute(query, args)
        mydb.commit()
    except Exception as e:
        print("In deleteStudentByRollNumber Student got exception", str(e))
    finally:
        if mydbCursor != None:
            mydbCursor.close()
        if mydb != None:
            mydb.close()


#Main

# student=Student("XYZ","BITF19M013",3.74)
# insertStudent(student)

# student=Student("Ahmed","BITF19M012",4.0)
# updateStudentByRollNumber("BITF19M012",student)

deleteStudentByRollNumber("BITF19M012")

#insertStudentmultipleinDB()

studentdata=selectAllData()
for s in studentdata:
    s.printStudent()
