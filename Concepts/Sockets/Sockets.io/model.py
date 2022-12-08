import pymysql
from views import *

class EarthJoyModel:
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
            
            
    def loginAdmin(self, admin):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute("select adminEmail, adminPswd from admin")
                emailList = cursor.fetchall()
                for e in emailList:
                    if admin.email == e[0] and admin.pswrd == e[1]:
                        return True
                return False
        except Exception as e:
            print("Exception in loginAdmin", str(e))
        finally:
            if cursor != None:
                cursor.close()



    def buyerLogin(self,username,password):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute("select buyerName, buyerPswd from buyer")
                users = cursor.fetchall()
                for u in users:
                    if username == u[0] and password == u[1]:
                        return True
                return False
        except Exception as e:
            print("Exception in buyerLogin", str(e))
        finally:
            if cursor != None:
                cursor.close()
    
    
    def getSellerID(self,username):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query="select sellerid from seller where sellername=%s"
                args = (username)
                cursor.execute(query,args)
                user = cursor.fetchone()
                return user[0]
        except Exception as e:
            print("Exception in getSellerID", str(e))
        finally:
            if cursor != None:
                cursor.close()
                
                
                
    def getBuyerID(self,username):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query="select buyerid from buyer where buyername=%s"
                args = (username)
                cursor.execute(query,args)
                user = cursor.fetchone()
                return user[0]
        except Exception as e:
            print("Exception in getBuyerID", str(e))
        finally:
            if cursor != None:
                cursor.close()
                
    def getSellerIDs(self):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute("select sellerID from seller")
                return cursor.fetchall()    
        except Exception as e:
            print("Exception in getSellerIDs", str(e))
        finally:
            if cursor != None:
                cursor.close()
                
                
                
    def getSellers(self, status):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select seller.*, admin.adminName from seller, admin where AppStatus = %s and seller.adminId = admin.adminId"
                args = (status)
                cursor.execute(query, args)
                check = cursor.fetchall()
                return check
        except Exception as e:
            print("Error in getSellers()", e)


    def getProducts(self, status):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select products.* , seller.sellerName, seller.sellerCategory from products, seller where seller.sellerId = products.sellerId and pAppStatus = %s"
                args = (status)
                cursor.execute(query, args)
                check = cursor.fetchall()
                return check
        except Exception as e:
            print("Error in getProducts()", e)



    def searchExistingProducts(self,keyword):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select products.* , seller.sellerName, seller.sellerCategory from products, seller where seller.sellerId = products.sellerId and pAppStatus = 1 and products.pname=%s"
                args = (keyword)
                cursor.execute(query, args)
                return cursor.fetchall()
        except Exception as e:
            print("Error in getProducts()", e)




    def checkCategoryExist(self,category):
        cursor=None
        flag=False
        try:
            if self.connection!=None:
                cursor = self.connection.cursor()
                query = "select categoryName from categories where categoryName=%s;"
                args = ((category).lower())
                cursor.execute(query,args)
                if cursor.fetchone():
                    flag = True
        except Exception as e:
            print("Exception in checkCategoryExist: ", str(e))
        finally:
            if cursor!=None:
                cursor.close()
                return flag 
    
    def addNewCategory(self,category):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "insert into categories (categoryName) values (%s)"
                args = (category.lower())
                cursor.execute(query, args)
                self.connection.commit()
        except Exception as e:
            print("Exception in addNewCategory", str(e))
        finally:
            if cursor != None:
                cursor.close()
    
    def getCategories(self):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select * from categories"
                cursor.execute(query)
                check = cursor.fetchall()
                return check
        except Exception as e:
            print("Error in getSellers()", e)
            
    
            
    def getCategoryID(self,category):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select catid from categories where categroyName = %s"
                cursor.execute(query,(category))
                return cursor.fetchone()[0]
        except Exception as e:
            print("Error in getCategoryID()", e)

            
    def addNewSubCategory(self,id,subcategory):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "insert into subcategories (catid,subcategory) values (%s,%s)"
                args = (id,subcategory.lower())
                cursor.execute(query, args)
                self.connection.commit()
        except Exception as e:
            print("Exception in addNewSubCategory", str(e))
        finally:
            if cursor != None:
                cursor.close()
                            
    def checkSubCategoryExist(self,subcategory):
        cursor=None
        flag = False
        try:
            if self.connection!=None:
                cursor = self.connection.cursor()
                query = "select subcategory from subcategories where subcategory=%s;"
                args = ((subcategory).lower())
                cursor.execute(query,args)
                if cursor.fetchone():
                    flag = True
        except Exception as e:
            print("Exception in checkSubCategoryExist: ", str(e))
        finally:
            if cursor!=None:
                cursor.close()
                return flag 
        
        
        
    def sellerLogin(self,user,password):    
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute("select sellerName,sellerPswd from seller")
                users = cursor.fetchall()
                for u in users:
                    if user == u[0] and password == u[1]:
                        print("haha")
                        return True
                print("nannana")
                return False
        except Exception as e:
            print("Exception in buyerLogin", str(e))
        finally:
            if cursor != None:
                cursor.close()
                
                
    def getBuyerIDs(self):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute("select buyerId from buyer")
                return cursor.fetchall()    
        except Exception as e:
            print("Exception in getBuyerIDs", str(e))
        finally:
            if cursor != None:
                cursor.close()
                
                
                
    def addMessage(self,roomID,message,datetime,messageby):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "insert into messages (roomID,message,datetime,messageby) values (%s,%s,%s,%s)"
                args = (roomID,message,datetime,messageby)
                cursor.execute(query, args)
                self.connection.commit()
        except Exception as e:
            print("Exception in addMessage", str(e))
        finally:
            if cursor != None:
                cursor.close()
                
                
    def getBuyerName(self,id):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select buyerName from buyer where buyerid = %s"
                cursor.execute(query,(id))
                
                return cursor.fetchone()[0]    
        except Exception as e:
            print("Exception in getBuyerIDs", str(e))
        finally:
            if cursor != None:
                cursor.close()
                
                
    def getSellerName(self,id):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select sellerName from seller where sellerid = %s"
                cursor.execute(query,(id))
                return cursor.fetchone()[0]    
        except Exception as e:
            print("Exception in getBuyerIDs", str(e))
        finally:
            if cursor != None:
                cursor.close()
                
                
    def getBuyerName(self,id):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select buyerName from seller where buyerid = %s"
                cursor.execute(query,(id))
                return cursor.fetchone()[0]    
        except Exception as e:
            print("Exception in getBuyerIDs", str(e))
        finally:
            if cursor != None:
                cursor.close()
                
                
    def getMessages(self,roomID):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select message,messageby,datetime from messages where roomID = %s"
                cursor.execute(query,(roomID))
                return cursor.fetchall()    
        except Exception as e:
            print("Exception in getMessages()", str(e))
        finally:
            if cursor != None:
                cursor.close()