from project.com.dao import *

class OtpDAO:
    def insertOtp(self,otpVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("INSERT INTO otpmaster (emailId,otp,otpActiveStatus) VALUES('{}','{}','{}')".format(otpVO.emailId,otpVO.otp,otpVO.otpActiveStatus))
        connection.commit()
        cursor1.close()
        connection.close()

    def searchOtp(self,otpVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("SELECT * FROM otpmaster WHERE emailId = '{}' AND otpActiveStatus = 'active' AND otpId =(SELECT MAX(otpId) FROM otpmaster)".format(otpVO.emailId))
        otpDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return otpDict

    def updatePassword(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE loginmaster SET loginPassword='{}' WHERE loginEmailId = '{}' ".format(loginVO.loginPassword, loginVO.loginEmailId))
        connection.commit()
        cursor1.close()
        connection.close()

    def updateOtpstatus(self,otpVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE otpmaster SET otpActiveStatus='{}' WHERE emailId = '{}' ".format(otpVO.otpActiveStatus, otpVO.emailId))
        connection.commit()
        cursor1.close()
        connection.close()