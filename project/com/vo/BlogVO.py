from wtforms import IntegerField,StringField

class BlogVO:
    blogId = IntegerField()
    blogTitle = StringField()
    blogDescription = StringField()
    blogFilename = StringField()
    blogFilepath = StringField()
    blogDate =  StringField()
    blogTime = StringField()
    blogActiveStatus = StringField()
