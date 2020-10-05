from project.com.dao import *

class ForumQuestionDAO:

    def insertForumQuestion(self,forumQuestionVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO forumquestionmaster (forumQuestion_LoginId,forumQuestion,forumQuestionDiscussion, forumQuestionDate,forumQuestionTime,forumQuestionActiveStatus) VALUES ('{}','{}','{}','{}','{}','{}')".format(forumQuestionVO.forumQuestion_LoginId,forumQuestionVO.forumQuestion,forumQuestionVO.forumQuestionDiscussion,forumQuestionVO.forumQuestionDate,forumQuestionVO.forumQuestionTime,forumQuestionVO.forumQuestionActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

    def searchForumQuestion(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from forumquestionmaster where forumQuestionActiveStatus = 'active'")
        forumQuestionDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return forumQuestionDict

    def searchForumQuestionById(self,forumQuestionVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from forumquestionmaster where forumQuestionId='{}'".format(forumQuestionVO.forumQuestionId))
        forumQuestionDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return forumQuestionDict

    def deleteQuestion(self,forumQuestionVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE forumquestionmaster SET forumQuestionActiveStatus='{}' WHERE forumQuestionId = '{}' ".format(forumQuestionVO.forumQuestionActiveStatus,forumQuestionVO.forumQuestionId))
        connection.commit()
        cursor1.close()
        connection.close()

    def discussQuestion(self,forumQuestionVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE forumquestionmaster SET forumQuestionDiscussion='{}' WHERE forumQuestionId = '{}' ".format(forumQuestionVO.forumQuestionDiscussion,forumQuestionVO.forumQuestionId))
        connection.commit()
        cursor1.close()
        connection.close()