from wtforms import IntegerField,StringField

class PredictVO:
    predictionId = IntegerField()
    predictionPrvDate = StringField()
    predictionDate = StringField()
    predictionFilename = StringField()
    predictionActualPrice = IntegerField()
    predictionPrice = IntegerField()
