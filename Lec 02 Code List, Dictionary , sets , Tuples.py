x=10
print(id(10))
print(id(x))
x=x+1
print(id(x))
print(x)
list1=[10,5,9,8,7,5]
list2=list1[1:6:2]
print(list2)
print(list1[3:6])

#Tuple
MyFirstTuple=(10,12,5,15,5)
print(MyFirstTuple)
for e in MyFirstTuple:
    print(e)
print(MyFirstTuple[3])
#MyFirstTuple[3]=85


# Set
testSet={10,"one",2,"three",3.5}
print(testSet)
print(testSet)
testSet.add(55)

#print(testSet[2])
for e in testSet:
    print(e)

# Dictionary

studentDic={"name":"Ali","rollno":3,"semmester":5, "cgpa":3.5}
print(studentDic["name"])
print(studentDic["rollno"])
print(studentDic["semmester"])

for key in studentDic:
    print(key,":",studentDic[key])

for e in studentDic.items():
    print(e)

for e in studentDic.values():
    print(e)

car1={"brand":"Toyota" , "model":"Yaris" , "year":2021}
car2={"brand":"Hundai" , "model":"Elantra" , "year":2021}
car3={"brand":"Kia" , "model":"Sportage" , "year":2021}
carList=[]
carList.append(car1)
carList.append(car2)
carList.append(car3)
for car in carList:
    print("brand:",car["brand"],"year",car["year"])

def createStudentData():
    studentData=[]
    recCount=int(input("Enter number of Student Records"))
    for  i in range(recCount):
        name=input("Enter Name")
        rollno = input("Enter RollNo")
        cgpa = input("Enter CGPA")
        student={"name":name,"rollno":rollno,"cgpa":cgpa}
        studentData.append(student)
    return studentData

data=createStudentData()
for d in data:
    print(d)