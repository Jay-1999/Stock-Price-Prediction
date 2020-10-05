from flask import request, render_template, session, redirect, url_for
from project.com.dao.DatasetDAO import DatasetDAO
from project.com.vo.PredictVO import PredictVO
from project.com.dao.PredictDAO import PredictDAO
from datetime import date
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from project import app

@app.route('/loadManagePrediction')
def loadManagePrediction():
    try:
        if session['loginRole'] == 'admin':
            datasetDAO = DatasetDAO()
            datasetDict=datasetDAO.searchDataset()
            return render_template('admin/managePrediction.html',datasetDict=datasetDict)
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

# @app.route('/loadManagePrediction')
# def loadManagePrediction():
#
#     try:
#         if session['loginRole'] == 'admin':
#             predictDAO = PredictDAO()
#
#             datasetDict = predictDAO.searchDPrediction()
#
#             return render_template('admin/managePrediction.html',datasetDict=datasetDict)
#         else:
#             return render_template('admin/login.html')
#
#     except:
#          return render_template('admin/login.html')


@app.route('/loadPredictNow')
def loadPredictNow():

    try:
        if session['loginRole'] == 'admin':
            return render_template('admin/login.html')
        else:
            datasetDAO = DatasetDAO()
            companyDict = datasetDAO.selectcompany()
            return render_template('user/predictNow.html',companyDict=companyDict)
    except:
         return render_template('admin/login.html')


@app.route('/predictNow',methods=['GET'])
def predictNow():
    try:
        if session['loginRole'] == 'user':
            return render_template('admin/login.html')
        else:
            predictVO = PredictVO()
            predictDAO = PredictDAO()
            predictVO.predictionFilename = request.args.get('datasetFilename')
            Dataset = pd.read_csv("C:\\project\\admin\\project\\static\\adminResources\\dataset\\{}".format(predictVO.predictionFilename))

            Dataset.info()

            Dataset.dropna()

            # X= Dataset.iloc[:,[3,7,9,13,14]].values
            # y= Dataset.iloc[:,[4,5,6,8]].values

            X = Dataset[['Close']]
            y = Dataset.iloc[:, 2].values

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

            lin_reg = LinearRegression()
            lin_reg.fit(X_train, y_train)

            # y_pred = lin_reg.predict(X_test)
            prv_price = Dataset['Close'].tail(1)
            myvals = [[float(prv_price)]]

            answer = lin_reg.predict(myvals)
            print("prediction", answer)
            ans = lin_reg.score(X, y)
            ans = (ans * 100)
            print(ans)
            predictVO.predictionDate = str(date.today())
            predictVO.predictionPrice = answer[0]
            predictDAO.insertPrediction(predictVO)
            # predictDict = predictDAO.searchDPrediction()
            return redirect(url_for('loadManagePrediction'))
    except:
         return render_template('admin/login.html')

@app.route('/viewprice',methods=['post'])
def viewprice():
    try:
        if session['loginRole'] == 'admin':
            return render_template('admin/login.html')
        else:
            predictVO = PredictVO()
            predictDAO = PredictDAO()
            predictVO.predictionFilename = request.form['company']
            priceDict = predictDAO.getPrice(predictVO)
            # print priceDict
            return render_template('user/viewPrediction.html',priceDict=priceDict)
    except:
         return render_template('admin/login.html')



