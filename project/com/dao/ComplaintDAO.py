from project.com.dao import *

class ComplaintDAO:

    def insertComplaint(self, complaintVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO complaintmaster (complaintSubject,complaintDescription,complaintFrom_LoginId,complaintDate,complaintTime,complaintStatus,complaintActiveStatus) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(complaintVO.complaintSubject, complaintVO.complaintDescription, complaintVO.complaintFrom_LoginId, complaintVO.complaintDate, complaintVO.complaintTime, complaintVO.complaintStatus, complaintVO.complaintActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

    def searchComplaint(self):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("select * from complaintmaster inner join loginmaster on complaintFrom_LoginId = loginId where complaintActiveStatus = 'active' and loginActiveStatus = 'active' ")

        complaintDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return complaintDict

    def replyComplaint(self, complaintVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("select * from complaintmaster where  complaintId = '{}' ".format(complaintVO.complaintId))

        complaintDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return complaintDict

    def updateComplaint(self, complaintVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("update complaintmaster set complaintReply='{}', complaintTo_LoginId='{}', complaintStatus='{}' where complaintId = '{}' ".format(complaintVO.complaintReply, complaintVO.complaintTo_LoginId, complaintVO.complaintStatus, complaintVO.complaintId))
        connection.commit()
        cursor1.close()
        connection.close()

    def searchComplaintById(self, complaintVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("select * from complaintmaster inner join loginmaster on complaintFrom_LoginId = loginId where complaintActiveStatus = 'active' and complaintFrom_LoginId = '{}' ".format(complaintVO.complaintFrom_LoginId))

        complaintDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return complaintDict

    def deleteComplaint(self, complaintVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE complaintmaster SET complaintActiveStatus='{}' WHERE complaintId = '{}' ".format(complaintVO.complaintActiveStatus, complaintVO.complaintId))
        connection.commit()
        cursor1.close()
        connection.close()

    def countComplaint(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select COUNT(*) from complaintmaster WHERE complaintActiveStatus='active' AND complaintStatus='pending'")
        complaintDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return complaintDict