from project.com.dao import *

class RegisterDAO:

    def insertRegister(self,registerVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("INSERT INTO registermaster (register_LoginId,registerFirstName,registerLastName,registerGender,registerAddress,registerPincode,registerContact,registerDate,registerTime,registerActiveStatus) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(registerVO.register_LoginId,registerVO.registerFirstName,registerVO.registerLastName, registerVO.registerGender, registerVO.registerAddress, registerVO.registerPincode,registerVO.registerContact, registerVO.registerDate,registerVO.registerTime, registerVO.registerActiveStatus))
        connection.commit()
        cursor1.close()
        connection.close()

    def searchRegister(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select register_LoginId,registerFirstName,registerLastName from registermaster WHERE registerActiveStatus='active'")
        registerDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return registerDict

    def searchUser(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from loginmaster INNER JOIN registermaster ON loginid=register_Loginid WHERE loginActivestatus='active'")
        userDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return userDict

    def countuser(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select COUNT(*) from registermaster WHERE registerActivestatus='active'")
        userDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return userDict

    def getdata(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("SELECT * FROM loginmaster INNER JOIN registermaster ON loginid=register_Loginid WHERE loginActivestatus='active' AND loginId=loginVO.loginId")
        getdataDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return getdataDict

    def updateProfile(self,registerVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE registermaster SET registerFirstName = '{}',registerLastName = '{}',registerGender = '{}',registerAddress = '{}',registerPincode = '{}',registerContact = '{}'  WHERE register_LoginId = '{}' ".format(registerVO.registerFirstName,registerVO.registerLastName, registerVO.registerGender, registerVO.registerAddress, registerVO.registerPincode,registerVO.registerContact, registerVO.register_LoginId))
        connection.commit()
        cursor1.close()
        connection.close()

    def findFirstName(self,registerVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("SELECT registerFirstname FROM registermaster WHERE register_LoginId='{}'".format(registerVO.register_LoginId))
        firstnameDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return firstnameDict

    def blockUser(self,registerVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE registermaster SET registerActiveStatus = '{}' WHERE register_LoginId = '{}'".format(registerVO.registerActiveStatus,registerVO.register_LoginId))
        connection.commit()
        cursor1.close()
        connection.close()
