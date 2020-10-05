from project.com.dao import *

class ForumAnswerDAO:

    def insertForumAnswer(self,forumAnswerVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("INSERT INTO forumanswermaster (forumAnswer_LoginId,forumAnswer_ForumQuestionId,forumAnswer,forumAnswerDate,forumAnswerTime,forumAnswerActiveStatus) VALUES('{}','{}','{}','{}','{}','{}')".format(forumAnswerVO.forumAnswer_LoginId,forumAnswerVO.forumAnswer_ForumQuestionId,forumAnswerVO.forumAnswer,forumAnswerVO.forumAnswerDate,forumAnswerVO.forumAnswerTime,forumAnswerVO.forumAnswerActiveStatus))
        connection.commit()
        cursor1.close()
        connection.close()

    def searchForumAnswer(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from forumanswermaster where forumAnswerActiveStatus = 'active'")
        forumAnswerDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return forumAnswerDict

    def deleteAnswer(self,forumAnswerVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE forumanswermaster SET forumAnswerActiveStatus='{}' WHERE forumAnswerId = '{}' ".format(forumAnswerVO.forumAnswerActiveStatus,forumAnswerVO.forumAnswerId))
        connection.commit()
        cursor1.close()
        connection.close()