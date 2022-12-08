from AddressbookModel import AddressbookModel
from ViewClasses import *
class AddressbookController:
    def __init__(self):
        self.model = AddressbookModel("localhost", "root", "Chalbhag@1", "raza")

    def signup(self):
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        u = User(email, password)
        flag=True
        while(flag):
            exist = self.model.checkUserExist(u)
            if not exist:
                insert = self.model.insertUser(u)
                if insert:
                    print("Signup successful")
                else:
                    print("Error in signup")
                flag = False
            else:
                print("User already exist")
                email = input("Enter Email: ")
                password = input("Enter Password: ")
                u = User(email, password)
                flag = True





