from flask import request, render_template, session, redirect, url_for
from project import app
from werkzeug.utils import secure_filename
from project.com.vo.DatasetVO import DatasetVO
from project.com.dao.DatasetDAO import DatasetDAO
import os



@app.route('/loadDataset')
def loadDataSet():

    try:
        if session['loginRole'] == 'admin':
            return render_template('admin/addDataset.html')
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')


@app.route('/insertDataset',methods=['POST'])
def insertDataset():

    try:
        if session['loginRole'] == 'admin':
            datasetVO = DatasetVO()
            datasetDAO = DatasetDAO()
            UPLOAD_FOLDER = 'C:/project/admin/project/static/adminResources/dataset'

            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            file = request.files['datasetFile']

            filename = secure_filename(file.filename)

            filepath = os.path.join(app.config['UPLOAD_FOLDER'])

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            datasetVO.datasetFilename = filename
            datasetVO.datasetFilepath = filepath
            datasetVO.datasetDescription = request.form['datasetDescription']
            datasetVO.datasetActiveStatus = 'active'

            datasetDAO.insertDataset(datasetVO)
            return render_template('admin/addDataset.html')
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')



@app.route('/viewDataset')
def viewDataset():

    try:
        if session['loginRole'] == 'admin':
            datasetDAO = DatasetDAO()
            datasetDict=datasetDAO.searchDataset()
            return render_template('admin/viewDataset.html',datasetDict=datasetDict)
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

@app.route('/deleteDataSet',methods=['GET'])
def deleteDataSet():

    try:
        if session['loginRole'] == 'admin':
            datasetVO = DatasetVO()
            datasetDAO = DatasetDAO()
            datasetVO.datasetId=request.args.get('datasetId')
            datasetVO.datasetActiveStatus='deactive'
            datasetDAO.deleteDataset(datasetVO)
            return redirect(url_for('viewDataset'))
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

@app.route('/viewPrediction')
def viewPrediction():
    try:
        if session['loginRole'] == 'user':
            return render_template('user/viewPrediction.html')
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')



