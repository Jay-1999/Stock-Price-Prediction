from flask import request,render_template,session,redirect,url_for
from project import app
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.RegisterVO import RegisterVO
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.dao.DatasetDAO import DatasetDAO
from project.com.dao.BlogDAO import BlogDAO
from project.com.dao.VideoDAO import VideoDAO
from project.com.dao.ComplaintDAO import ComplaintDAO
from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.dao.PredictDAO import PredictDAO

import random,string,smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
otp=''

@app.route('/')
def login():
    return render_template('admin/login.html')

@app.route('/loadLogin')
def loadLogin():
    return render_template('admin/login.html')

@app.route('/loadForgotPassword')
def loadForgotPassword():
    return render_template('admin/forgetPassword.html')



@app.route('/loadIndex')
def loadIndex():
    try:
        if session['loginRole'] == 'admin':
            registerDAO = RegisterDAO()
            datasetDAO = DatasetDAO()
            blogDAO = BlogDAO()
            videoDAO = VideoDAO()
            complaintDAO = ComplaintDAO()
            feedbackDAO = FeedbackDAO()
            predictDAO = PredictDAO()

            userdict=registerDAO.countuser()
            companydict=datasetDAO.countcompany()
            blogDict=blogDAO.countBlog()
            videoDict=videoDAO.countVideo()
            complaintDict=complaintDAO.countComplaint()
            feedbackDict=feedbackDAO.countfeedback()
            predictDict = predictDAO.searchDPrediction()

            return render_template('admin/index.html',userdict=userdict,companydict=companydict,blogDict=blogDict,videoDict=videoDict,feedbackDict=feedbackDict,complaintDict=complaintDict,predictDict=predictDict)
        else:
            blogDAO = BlogDAO()
            blogDict = blogDAO.searchBlog()
            return render_template('user/index.html',blogDict=blogDict)
    except:
       return render_template('admin/login.html')




@app.route('/checkLogin',methods=['POST'])
def checkLogin():
    loginVO=LoginVO()
    loginDAO=LoginDAO()


    loginVO.loginEmailId=request.form['loginEmailId']
    loginVO.loginPassword=request.form['loginPassword']

    loginDict=loginDAO.searchLogin(loginVO)



    if len(loginDict) == 0:
        return render_template('admin/login.html',loginemailIderror="*you are not registered")
    elif loginVO.loginPassword != loginDict[0]['loginPassword']:
        return render_template('admin/login.html',loginPassworderror="*Incorrect email or password")
    elif loginDict[0]['loginRole'] == 'admin':
        session['loginRole'] = loginDict[0]['loginRole']
        session['loginId'] = loginDict[0]['loginId']
        return redirect(url_for('loadIndex'))
    else:
        registerVO = RegisterVO()
        registerDAO = RegisterDAO()
        session['loginRole'] = loginDict[0]['loginRole']
        session['loginId'] = registerVO.register_LoginId = loginDict[0]['loginId']

        firstnameDict=registerDAO.findFirstName(registerVO)
        session['registerFirstname'] = firstnameDict[0]['registerFirstname']
        return redirect(url_for("loadIndex"))

@app.route('/loadProfile')
def loadProfile():
    try:
        if session['loginRole'] == 'user':
            loginVO = LoginVO()
            loginDAO = LoginDAO()
            loginVO.loginId = session['loginId']
            getdataDict = loginDAO.getdata(loginVO)
            return render_template('user/profilePage.html',getdataDict=getdataDict)
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

@app.route('/loadEditprofile')
def loadEditprofile():
    try:
        if session['loginRole'] == 'user':
            loginVO = LoginVO()
            loginDAO = LoginDAO()
            loginVO.loginId = session['loginId']
            getdataDict = loginDAO.getdata(loginVO)
            if "error" in session:
                error=session['error']
                session.pop('error')
                return render_template('user/editProfile.html',getdataDict=getdataDict,error=error)
            else:
                return render_template('user/editProfile.html', getdataDict=getdataDict)
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

@app.route('/loadChangepassword')
def loadChangepassword():
     try:
        if session['loginRole'] == 'user':
            if "error" in session:
                error=session['error']
                session.pop('error')
                return render_template('user/changePassword.html',error=error)
            else:
                return render_template('user/changePassword.html')
        else:
            return render_template('admin/login.html')
     except:
         return render_template('admin/login.html')

@app.route('/updatePassword',methods=['POST'])
def updatePassword():
    try:
        if session['loginRole'] == 'user':
            loginDAO = LoginDAO()
            loginVO = LoginVO()

            loginVO.loginId = session['loginId']
            loginpassword = request.form['loginpassword']
            loginVO.loginPassword = request.form['loginPassword']


            loginDict = loginDAO.searchLoginIddata(loginVO)
            # print loginDict

            if loginpassword == loginDict[0]['loginPassword']:
                loginDAO.changePassword(loginVO)
                return redirect(url_for('loadProfile'))
            else:
                session['error'] = "*wrong password Please enter again"
                return redirect(url_for('loadChangepassword'))
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

@app.route('/loadAboutus')
def loadAboutus():
    try:
        if session['loginRole'] == 'user':
            return render_template('user/about.html')
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

@app.route('/loadContactus')
def loadContactus():
    try:
        if session['loginRole'] == 'user':
            return render_template('user/contact.html')
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')



@app.route('/logout')
def logout():
    session.clear()
    return render_template('admin/login.html')

