from flask import render_template,session,redirect,url_for,request
from project import app
from datetime import datetime
from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.vo.FeedbackVO import FeedbackVO

@app.route('/viewFeedback')
def viewFeedback():
    try:
        if session['loginRole'] == 'admin':
            feedbackDAO = FeedbackDAO()
            feedbackDict = feedbackDAO.searchFeedback()
            return render_template('admin/viewFeedback.html', feedbackDict=feedbackDict)
        else:
            feedbackDAO = FeedbackDAO()
            feedbackVO = FeedbackVO()
            feedbackVO.feedbackFrom_LoginId = session['loginId']
            feedbackDict = feedbackDAO.searchFeedbackById(feedbackVO)
            return render_template('user/viewFeedback.html', feedbackDict=feedbackDict)
    except:
        return render_template('admin/login.html')

@app.route('/postFeedback')
def postFeedback():
    try:
        if session['loginRole'] == 'user':
            return render_template('user/postFeedback.html')
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

@app.route('/insertFeedback',methods=['POST'])
def insertFeedback():
    if session['loginRole'] != 'user':
        return redirect(url_for('login'))

    else:
        feedbackDAO = FeedbackDAO()
        feedbackVO = FeedbackVO()

        feedbackVO.feedbackRating = request.form['feedbackRating']
        feedbackVO.feedbackMessage = request.form['feedbackMessage']
        feedbackVO.feedbackDate, feedbackVO.feedbackTime = str(datetime.now()).split(' ')
        feedbackVO.feedbackActiveStatus = 'active'

        feedbackVO.feedbackFrom_LoginId = session['loginId']

        feedbackDAO.insertFeedback(feedbackVO)

        return redirect(url_for('postFeedback'))

@app.route('/updateFeedback')
def updateFeedback():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    else:
        feedbackDAO = FeedbackDAO()
        feedbackVO = FeedbackVO()
        feedbackVO.feedbackId = request.args.get('feedbackId')
        feedbackVO.feedbackTo_LoginId = session['loginId']
        feedbackDAO.updateFeedback(feedbackVO)
        return redirect(url_for('viewFeedback'))

@app.route('/deleteFeedback',methods=['GET'])
def deleteFeedback():
    if session['loginRole']== 'admin':
        return redirect(url_for('login'))
    else:
        feedbackVO = FeedbackVO()
        feedbackDAO = FeedbackDAO()
        feedbackVO.feedbackId = request.args.get('feedbackId')
        feedbackVO.feedbackActiveStatus = 'deactive'
        feedbackDAO.deleteFeedback(feedbackVO)
        return redirect(url_for('viewFeedback'))
