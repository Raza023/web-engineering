from Classes import *

s=Student("Ali","BITF19M001",3.5)
s.printStudent()

# Research Student
s2=ReserachStudent("Aisha","ITF19M002",3.6,100)
s2.printStudent()

def test():
    data=[]
    for i in range(2):
        print("Enter Name: ",end="")
        n = input()
        print("Enter Roll no: ", end="")
        r = input()
        print("Enter CGPA: ", end="")
        c = input()
        s=Student(n,r,c)
        data.append(s)
    return data

mydata=test()
for s in mydata:
    s.printStudent()