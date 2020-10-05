from project.com.dao import *

class PredictDAO:

    def insertPrediction(self,predictVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("INSERT INTO predictionmaster (predictionDate,predictionFilename,predictionPrice)VALUES ('{}','{}','{}')".format(predictVO.predictionDate,predictVO.predictionFilename,predictVO.predictionPrice))
        connection.commit()
        cursor1.close()
        connection.close()

    def searchDPrediction(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from predictionmaster")
        predictDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return predictDict

    def loadManagePrediction(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from datasetmaster")
        datasetDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return datasetDict

    def getPrice(self,predictVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("SELECT * FROM predictionmaster WHERE predictionFilename='{}' ORDER BY predictionId DESC".format(predictVO.predictionFilename))
        priceDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return priceDict