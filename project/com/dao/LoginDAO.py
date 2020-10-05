from project.com.dao import *


class LoginDAO:
    def searchLogin(self, loginVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from loginmaster WHERE loginEmailId = '{}' AND loginActiveStatus='active'".format(loginVO.loginEmailId))
        loginDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return loginDict

    def insertLogin(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("INSERT INTO loginmaster (loginEmailId,loginRole,loginActiveStatus,loginPassword) VALUES('{}','{}','{}','{}')".format(loginVO.loginEmailId,loginVO.loginRole,loginVO.loginActiveStatus,loginVO.loginPassword))
        connection.commit()
        cursor1.close()
        connection.close()

    def searchLoginId(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select max(loginId) from loginmaster")
        loginDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return loginDict

    def updatePassword(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE loginmaster SET loginPassword='{}' WHERE loginEmailId = '{}' ".format(loginVO.loginPassword, loginVO.loginEmailId))
        connection.commit()
        cursor1.close()
        connection.close()

    def getdata(self,loginVO):
            connection = con_db()
            cursor1 = connection.cursor()
            cursor1.execute("SELECT * FROM loginmaster INNER JOIN registermaster ON loginid=register_Loginid WHERE loginActivestatus='active' AND loginId='{}'".format(loginVO.loginId))
            getdataDict = cursor1.fetchall()
            cursor1.close()
            connection.close()
            return getdataDict

    def searchLoginIddata(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from loginmaster WHERE loginId='{}'".format(loginVO.loginId))
        loginDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return loginDict

    def updateProfile(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE loginmaster SET loginEmailId = '{}' WHERE loginId = '{}' ".format(loginVO.loginEmailId, loginVO.loginId))
        connection.commit()
        cursor1.close()
        connection.close()

    def changePassword(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE loginmaster SET loginPassword='{}' WHERE loginId = '{}' ".format(loginVO.loginPassword, loginVO.loginId))
        connection.commit()
        cursor1.close()
        connection.close()

    def blockUser(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE loginmaster SET loginActiveStatus = '{}' WHERE loginId = '{}'".format(loginVO.loginActiveStatus,loginVO.loginId))
        connection.commit()
        cursor1.close()
        connection.close()






