from flask import render_template,request,redirect,url_for,session
from project import app
from datetime import datetime
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.RegisterVO import RegisterVO
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
import random,string,smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

@app.route('/loadRegister')
def loadRegister():
    return render_template('user/register.html')


@app.route('/insertRegister',methods=['POST'])
def insertRegister():

    registerDAO = RegisterDAO()
    registerVO = RegisterVO()

    loginDAO = LoginDAO()
    loginVO  = LoginVO()
    loginVO.loginEmailId = request.form['registerEmailId']
    registerDict=loginDAO.searchLogin(loginVO)

    if len(registerDict)>0:
        return render_template('user/register.html',errorreg="*already registered")
    else:
        registerVO.registerFirstName = request.form['registerFirstName']
        registerVO.registerLastName = request.form['registerLastName']
        registerVO.registerGender = request.form['registerGender']
        registerVO.registerAddress = request.form['registerAddress']
        registerVO.registerPincode = request.form['registerPincode']
        registerVO.registerContact = request.form['registerContact']
        registerVO.registerDate, registerVO.registerTime = str(datetime.now()).split(' ')
        registerVO.registerActiveStatus = 'active'


        loginVO.loginRole = 'user'
        loginVO.loginActiveStatus = 'active'

        loginVO.loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))
        fromaddr = "darshilami@gmail.com"
        toaddr = loginVO.loginEmailId

        msg = MIMEMultipart()

        msg['From'] = fromaddr

        msg['To'] = toaddr

        msg['Subject'] = "your password"

        msg.attach(MIMEText(loginVO.loginPassword, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(fromaddr, "iamdarshil")

        text = msg.as_string()

        server.sendmail(fromaddr, toaddr, text)

        server.quit()


        loginDAO.insertLogin(loginVO)
        loginDict=loginDAO.searchLoginId()

        registerVO.register_LoginId=loginDict[0]['max(loginId)']
        registerDAO.insertRegister(registerVO)
        return redirect(url_for('loadLogin'))

    return redirect(url_for('loadLogin'))


@app.route('/viewUser')
def viewUser():
    try:
        if session['loginRole'] == 'admin':
            registerDAO = RegisterDAO()
            userDict=registerDAO.searchUser()
            return render_template('admin/viewUser.html',userDict=userDict)
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')

@app.route('/blockUser',methods=['GET'])
def blockUser():

    try:
        if session['loginRole'] == 'admin':
            registerVO = RegisterVO()
            registerDAO = RegisterDAO()
            loginDAO = LoginDAO()
            loginVO = LoginVO()
            registerVO.register_LoginId = loginVO.loginId =request.args.get('register_LoginId')
            registerVO.registerActiveStatus = loginVO.loginActiveStatus ='deactive'
            registerDAO.blockUser(registerVO)
            loginDAO.blockUser(loginVO)
            return redirect(url_for('viewUser'))
        else:
            return render_template('admin/login.html')
    except:
        return render_template('admin/login.html')


@app.route('/updateProfile',methods=['POST'])
def updateProfile():
    try:
        registerDAO = RegisterDAO()
        registerVO = RegisterVO()

        loginDAO = LoginDAO()
        loginVO  = LoginVO()

        registerVO.registerFirstName = request.form['registerFirstName']
        registerVO.registerLastName = request.form['registerLastName']
        registerVO.registerGender = request.form['registerGender']
        registerVO.registerAddress = request.form['registerAddress']
        registerVO.registerPincode = request.form['registerPincode']
        registerVO.registerContact = request.form['registerContact']

        loginVO.loginEmailId = request.form['registerEmailId']
        loginVO.loginPassword = request.form['loginPassword']
        loginVO.loginId = registerVO.register_LoginId = request.form['loginId']

        loginDict = loginDAO.searchLoginIddata(loginVO)

        if loginVO.loginPassword == loginDict[0]['loginPassword']:
            loginDAO.updateProfile(loginVO)
            registerDAO.updateProfile(registerVO)
            return redirect(url_for('loadProfile'))
        else:
            session['error']="*wrong password Please enter again"
            return  redirect(url_for('loadEditprofile'))
    except:
        return render_template('admin/login.html')

