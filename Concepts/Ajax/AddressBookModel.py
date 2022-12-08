from ViewClasses import User,Contact

import pymysql

class AddressbookModel:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        try:
            self.connection = pymysql.connect(host=self.host, user=self.user,password=self.password,database=self.database)
        except Exception as e:
            print("There is an error in connection", str(e))
    def __del__(self):
        if self.connection!=None:
            self.connection.close()

    def checkUserCredentials(self, user):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute("select email, password from users")
                emailList = cursor.fetchall()
                for e in emailList:
                    if user.email == e[0] and user.password == e[1]:
                        return True
                return False
        except Exception as e:
            print("Exception in checkUserCredentials", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def checkUserExist(self, user):
        cursor = None
        try:
            if self.connection!=None:
                cursor = self.connection.cursor()
                cursor.execute("select email from users")
                emailList = cursor.fetchall()
                # print(emailList)
                for e in emailList:
                    if user.email == e[0]:
                        return True
                return False
        except Exception as e:
            print("Exception in checkUserExist",str(e))
        finally:
            if cursor!=None:
                cursor.close()

    def insertUser(self,user):
        cursor = None
        try:
            if self.connection!=None:
                cursor = self.connection.cursor()
                query = "insert into users (email,password) values (%s,%s)"
                args = (user.email, user.password)
                cursor.execute(query, args)
                self.connection.commit()
                return True
            else:
                return False
        except Exception as e:
            print("Exception in insertUser. ", str(e))
            return False
        finally:
            if cursor!=None:
                cursor.close()

    def insertContact(self, contact):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                # query = "select user_id from users where email='%s'"
                # args = (user.email)
                # cursor.execute(query, args)
                # ids = cursor.fetchall()
                # uid = ids[0]
                query = "insert into addressbook (user_id,Contact_name,Contact_mobile,Contact_city,Contact_profession) values (%s,%s,%s,%s,%s)"
                uid=1
                args = (uid, contact.name, contact.mobile, contact.city, contact.profession)
                cursor.execute(query, args)
                self.connection.commit()
                return True
            else:
                return False
        except Exception as e:
            print("Exception in insertContact", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

    def updateContact(self, c ,cid):
        cursor = None
        flag = False
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                name = c.name
                name = name.upper()
                mobile = c.mobile
                mobile = mobile.upper()
                city = c.city
                city = city.upper()
                prof = c.profession
                prof = prof.upper()
                query = "update addressbook set Contact_name = %s, Contact_mobile= %s, Contact_city=%s, Contact_profession=%s where contact_id = %s"
                args = (name, mobile, city, prof, cid)
                cursor.execute(query, args)
                self.connection.commit()
                return True
            else:
                return False
        except Exception as e:
            print("Exception handling in updateContact. ",str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

    def getContact(self):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "Select Contact_name, Contact_mobile, contact_city, Contact_profession from addressbook"
                cursor.execute(query)
                record = cursor.fetchall()
                # cList = []
                # print(cList)
                # for i in record:
                #     c = Contact(i[0], i[1], i[2], i[3])
                #     cList.append(c)
                return record
            else:
                return False
        except Exception as e:
            return False
            print("Exception in gettingUser", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def getOneContact(self,cname):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "Select * from addressbook where Contact_name = %s"
                args= (cname)
                cursor.execute(query, args)
                record = cursor.fetchone()
                print(record)
                if record != None:
                    # contact = Contact(record[2],record[3],record[4],record[5])
                    return record[0]
                else:
                    return False
            else:
                return False
        except Exception as e:
            return False
            print("Exception in getOneContact", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def getCityContacts(self,city):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "Select Contact_name, Contact_mobile, contact_city, Contact_profession from addressbook where Contact_city = %s"
                args= (city)
                cursor.execute(query, args)
                record = cursor.fetchall()
                return record
            else:
                return False
        except Exception as e:
            return False
            print("Exception in getCityContact", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def deleteContact(self):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select * from addressbook;"
                args = ()
                cursor.execute(query, args)
                data2 = cursor.fetchall()
                print("Available records to delete: ")
                for i in range(len(data2)):
                    print(data2[i])
                list1 = []
                for i in range(len(data2)):
                    list1.append(data2[i][0])
                print("Available contact ids to delete record: ", list1)
                if len(list1)==0:
                    print("No data found.")
                    return False
                else:
                    ch = True
                    while (ch == True):
                        if len(list1) == 0:
                            break
                        else:
                            print("Enter a contact id to delete: ", end="")
                            inp = input()
                            ef=True
                            while (ef):
                                if inp.isnumeric():
                                    ef=False
                                else:
                                    print("Please enter a correct contact id to delete: ", end="")
                                    inp = input()
                            i = 0
                            flag = True
                            while i < len(list1):
                                if int(inp) == list1[i]:
                                    flag = False
                                    break
                                else:
                                    ch = True
                                i = i + 1
                        if flag == False:
                            ch = False
                    cid = inp
                    query = "delete from addressbook where contact_id = %s"
                    args = (cid)
                    cursor.execute(query, args)
                    self.connection.commit()
                    return True
            else:
                return False
        except Exception as e:
            print("Contact does not exist.")
            return False
        finally:
            if cursor != None:
                cursor.close()
    def searchContact(self):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                check=True
                while(check):
                    print("\nPress 1 to search by name.")
                    print("Press 2 to search partially by name.")
                    print("Press 3 to search by city.")
                    print("Press 4 to search by profession.")
                    print("Press 0 to exit from search.")
                    choice = input("Enter Your Choice: ")
                    if choice == "1":
                        name = input("Enter Name: ")
                        query = "select * from addressbook where Contact_name=%s;"
                        args = (name)
                        cursor.execute(query, args)
                        data2 = None
                        data2 = cursor.fetchall()
                        print("Available records: ")
                        if len(data2)==0:
                            print("Nothing!")
                        else:
                            for i in range(len(data2)):
                                print(data2[i])
                        check = True
                    elif choice == "2":
                        name = input("Enter partial characters of name: ")
                        query = "select * from addressbook where Contact_name like %s;"
                        args = ("%"+name+"%")
                        cursor.execute(query, args)
                        data2 = None
                        data2 = cursor.fetchall()
                        print("Available records: ")
                        if len(data2) == 0:
                            print("Nothing!")
                        else:
                            for i in range(len(data2)):
                                print(data2[i])
                        check = True
                    elif choice == "3":
                        city = input("Enter City: ")
                        query = "select * from addressbook where Contact_city=%s;"
                        args = (city)
                        cursor.execute(query, args)
                        data2 = None
                        data2 = cursor.fetchall()
                        print("Available records: ")
                        if len(data2) == 0:
                            print("Nothing!")
                        else:
                            for i in range(len(data2)):
                                print(data2[i])
                        check = True
                    elif choice == "4":
                        prof = input("Enter profession: ")
                        query = "select * from addressbook where Contact_profession=%s;"
                        args = (prof)
                        cursor.execute(query, args)
                        data2 = None
                        data2 = cursor.fetchall()
                        print("Available records: ")
                        if len(data2) == 0:
                            print("Nothing!")
                        else:
                            for i in range(len(data2)):
                                print(data2[i])
                        check = True
                    elif choice == "0":
                        check = False
                    else:
                        print("Please enter correct choice.")
                        check = True

        except Exception as e:
            print("Exception in searchContact", str(e))

    def loginUser(self, user):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "Select email,password from users where email=%s and password=%s"
                args = (user.email, user.password)
                cursor.execute(query, args)
                record = cursor.fetchone()
                if record[0] == user.email and record[1] == user.password:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return False
            print("Exception in loginUser", str(e))
        finally:
            if cursor != None:
                cursor.close()