from project.com.dao import *

class VideoDAO:

    def insertVideo(self,videoVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("INSERT INTO videomaster (videoTitle,videoDescription,videoFilename,videoFilepath,videoDate,videoTime,videoActiveStatus) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(videoVO.videoTitle,videoVO.videoDescription,videoVO.videoFilename,videoVO.videoFilepath,videoVO.videoDate,videoVO.videoTime,videoVO.videoActiveStatus))
        connection.commit()
        cursor1.close()
        connection.close()

    def searchVideo(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from videomaster WHERE videoActiveStatus='active'")
        videoDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return videoDict

    def deleteVideo(self,videoVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE videomaster SET videoActiveStatus='{}' WHERE videoId = '{}' ".format(videoVO.videoActiveStatus,videoVO.videoId))
        connection.commit()
        cursor1.close()
        connection.close()

    def countVideo(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select COUNT(*) from videomaster WHERE videoActivestatus='active'")
        videoDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return videoDict