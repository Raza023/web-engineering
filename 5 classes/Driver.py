from Classes import Student,ReserachStudent
s=Student("Ali","BITF19M001",3.5)
s.printStudent()
# Research Student
s2=ReserachStudent("Aisha","BITF19M002",3.6,100)
s2.printStudent()

def test():
    data=[]
    for i in range(2):
        n = input("Enter Name")
        r = input("Enter rollno")
        c = input("Enter cgpa")
        s=Student(n,r,c)
        data.append(s)

    return data
mydata=test()
for s in mydata:
    s.printStudent()