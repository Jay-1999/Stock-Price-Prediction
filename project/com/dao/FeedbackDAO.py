from project.com.dao import *

class FeedbackDAO:

    def insertFeedback(self,feedbackVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("INSERT INTO feedbackmaster (feedbackMessage,feedbackFrom_LoginId,feedbackRating,feedbackDate,feedbackTime,feedbackActiveStatus) VALUES('{}','{}','{}','{}','{}','{}')".format(feedbackVO.feedbackMessage,feedbackVO.feedbackFrom_LoginId,feedbackVO.feedbackRating,feedbackVO.feedbackDate,feedbackVO.feedbackTime,feedbackVO.feedbackActiveStatus))
        connection.commit()
        cursor1.close()
        connection.close()

    def searchFeedback(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from feedbackmaster inner join loginmaster on feedbackFrom_LoginId = loginId where feedbackActiveStatus = 'active' and loginActiveStatus = 'active' ")
        feedbackDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return feedbackDict

    def searchFeedbackById(self,feedbackVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from feedbackmaster inner join loginmaster on feedbackFrom_LoginId = loginId where feedbackActiveStatus = 'active' and feedbackFrom_LoginId = '{}' ".format(feedbackVO.feedbackFrom_LoginId))
        feedbackDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return feedbackDict

    def updateFeedback(self,feedbackVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE feedbackmaster SET feedbackTo_LoginId='{}' WHERE feedbackId = '{}'".format(feedbackVO.feedbackTo_LoginId,feedbackVO.feedbackId))
        connection.commit()
        cursor1.close()
        connection.close()

    def deleteFeedback(self,feedbackVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE feedbackmaster SET feedbackActiveStatus='{}' WHERE feedbackId = '{}' ".format(feedbackVO.feedbackActiveStatus,feedbackVO.feedbackId))
        connection.commit()
        cursor1.close()
        connection.close()

    def countfeedback(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select COUNT(*) from feedbackmaster WHERE feedbackActiveStatus='active'")
        feedbackDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return feedbackDict
