from flask import render_template, request, redirect, url_for, session
from project import app
from datetime import datetime
from project.com.dao.ComplaintDAO import ComplaintDAO
from project.com.vo.ComplaintVO import ComplaintVO



@app.route('/viewComplaint')
def viewComplaint():
    try:
        if session['loginRole'] == 'admin':
            complaintDAO = ComplaintDAO()
            complaintDict = complaintDAO.searchComplaint()
            return render_template('admin/viewComplaint.html', complaintDict=complaintDict)
        else:
            complaintDAO = ComplaintDAO()
            complaintVO = ComplaintVO()
            complaintVO.complaintFrom_LoginId = session['loginId']
            complaintDict = complaintDAO.searchComplaintById(complaintVO)
            return render_template('user/viewComplaint.html', complaintDict=complaintDict)
    except:
        return render_template('admin/login.html')


@app.route('/postComplaint')
def postComplaint():
    try:
        if session['loginRole'] == 'user':
            return render_template('user/postComplaint.html')
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

@app.route('/insertComplaint',methods=['POST'])
def insertComplaint():
    try:
        if session['loginRole'] != 'user':
            return redirect(url_for('login'))

        else:
            complaintDAO = ComplaintDAO()
            complaintVO = ComplaintVO()

            complaintVO.complaintSubject = request.form['complaintSubject']
            complaintVO.complaintDescription = request.form['complaintDescription']
            complaintVO.complaintDate, complaintVO.complaintTime = str(datetime.now()).split(' ')
            complaintVO.complaintStatus = 'pending'
            complaintVO.complaintActiveStatus = 'active'
            complaintVO.complaintFrom_LoginId = session['loginId']

            complaintDAO.insertComplaint(complaintVO)
            return redirect(url_for('postComplaint'))
    except:
        return render_template('admin/login.html')

@app.route('/loadComplaintReply',methods=['GET'])
def loadComplaintReply():

    if session['loginRole'] != 'admin':
        return redirect(url_for('login'))

    else:
        complaintDAO = ComplaintDAO()
        complaintVO = ComplaintVO()

        complaintVO.complaintId = request.args.get('complaintId')

        complaintDict = complaintDAO.replyComplaint(complaintVO)

        return render_template('admin/replyComplaint.html', complaintDict=complaintDict)

@app.route('/complaintReply',methods=['POST'])
def complaintReply():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    else:
        complaintDAO = ComplaintDAO()
        complaintVO = ComplaintVO()

        complaintVO.complaintStatus = 'replied'
        complaintVO.complaintReply = request.form['complaintReply']
        complaintVO.complaintTo_LoginId = session['loginId']
        complaintVO.complaintId = request.form['complaintId']
        complaintDAO.updateComplaint(complaintVO)

        return redirect(url_for('viewComplaint'))

@app.route('/deleteComplaint',methods=['GET'])
def deleteComplaint():

    if session['loginRole']== 'admin':
        return redirect(url_for('login'))
    else:
        complaintVO = ComplaintVO()
        complaintDAO = ComplaintDAO()
        complaintVO.complaintId = request.args.get('complaintId')
        complaintVO.complaintActiveStatus = 'deactive'
        complaintDAO.deleteComplaint(complaintVO)
        return redirect(url_for('viewComplaint'))