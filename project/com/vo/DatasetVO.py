from wtforms import IntegerField,StringField

class DatasetVO:
    datasetId = IntegerField()
    datasetFilename = StringField()
    datasetFilepath = StringField()
    datasetDescription = StringField()
    datasetActiveStatus = StringField()
