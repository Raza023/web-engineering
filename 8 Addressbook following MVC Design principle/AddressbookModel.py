from ViewClasses import *
import pymysql
class AddressbookModel:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.connection=None
        try:
            self.connection=pymysql.connect(host=self.host, user=self.user,password=self.password,database=self.database)
        except Exception as e:
            print("There is error in connection",str(e))

    def __del__(self):
        if self.connection!=None:
            self.connection.close()

    def checkUserExist(self,user):
        try:
            if self.connection!=None:
                cursor=self.connection.cursor()
                cursor.execute("select uemail from users")
                emailList=cursor.fetchall()
                for e in emailList:
                    if user.email==e[0]:
                        return True
                return False
        except Exception as e:
            print("Exception in checkUserExist ",str(e))
        finally:
            if cursor!=None:
                cursor.close()

    def insertUser(self,user):
        try:
            if self.connection!=None:
                cursor=self.connection.cursor()
                query="insert into users (uemail,upassword) values (%s,%s)"
                args=(user.email,user.password)
                cursor.execute(query,args)
                self.connection.commit()
                return True
            else:
                return False
        except Exception as e:
            return False
            print("Exception in insertUser ",str(e))
        finally:
            if cursor!=None:
                cursor.close()



