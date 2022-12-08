class Student:
    def __init__(self,name,rollno,cgpa):
        self.name=name
        self.rollno=rollno
        self.cgpa=cgpa
    def printStudent(self):
        print("Name:",self.name,"Rollno:",self.rollno,"CGPA:",self.cgpa, end=" ")


class ReserachStudent(Student):
    def __init__(self ,name,rollno,cgpa, noofarticles):
        super().__init__(name,rollno,cgpa)
        self.numArticles=noofarticles

    def printStudent(self):
        super().printStudent()
        print("Number of Articles:",self.numArticles)