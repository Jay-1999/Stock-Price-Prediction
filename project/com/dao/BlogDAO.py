from project.com.dao import *

class BlogDAO:

    def insertBlog(self,blogVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO blogmaster (blogTitle,blogDescription,blogFilename,blogFilepath,blogDate,blogTime,blogActiveStatus) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(blogVO.blogTitle,blogVO.blogDescription,blogVO.blogFilename,blogVO.blogFilepath,blogVO.blogDate,blogVO.blogTime,blogVO.blogActiveStatus))


        connection.commit()
        cursor1.close()
        connection.close()

    def searchBlog(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from blogmaster WHERE blogActiveStatus='active' ORDER BY blogId DESC")
        blogDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return blogDict

    def deleteBlog(self,blogVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE blogmaster SET blogActiveStatus='{}' WHERE blogId = '{}' ".format(blogVO.blogActiveStatus,blogVO.blogId))
        connection.commit()
        cursor1.close()
        connection.close()

    def searchBlogbyId(self,blogVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from blogmaster WHERE blogId='{}'".format(blogVO.blogId))
        blogDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return blogDict

    def updateBlog(self,blogVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE blogmaster SET blogTitle='{}',blogDescription='{}',blogFilename='{}',blogFilepath='{}' WHERE blogId = '{}'".format(blogVO.blogTitle,blogVO.blogDescription,blogVO.blogFilename,blogVO.blogFilepath,blogVO.blogId))
        # print blogVO.blogId
        connection.commit()
        cursor1.close()
        connection.close()

    def countBlog(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select COUNT(*) from blogmaster WHERE blogActivestatus='active'")
        blogDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return blogDict