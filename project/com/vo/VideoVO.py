from wtforms import IntegerField,StringField

class VideoVO:
    videoId = IntegerField()
    videoTitle = StringField()
    videoDescription = StringField()
    videoFilename = StringField()
    videoFilepath = StringField()
    videoDate = StringField()
    videoTime = StringField()
    videoActiveStatus = StringField()
