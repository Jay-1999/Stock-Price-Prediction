from flask import request,render_template,session,redirect,url_for
from project import app
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.OtpVO import OtpVO
from project.com.dao.OtpDAO import OtpDAO
import random,string,smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

@app.route('/checkEmail',methods=['POST'])
def checkEmail():

    loginVO=LoginVO()
    loginDAO=LoginDAO()

    session['emailid'] = request.form['emailId']
    loginVO.loginEmailId = session['emailid']



    loginDict=loginDAO.searchLogin(loginVO)

    if len(loginDict) == 0:
        return render_template('admin/login.html',loginemailIderror="Invalid EmailId")
    else:
        otpVo=OtpVO()
        otpDAO=OtpDAO()

        otpVo.otp = ''.join((random.choice(string.digits)) for x in range(4))
        otpVo.emailId = session['emailid']
        otpVo.otpActiveStatus = 'active'
        fromaddr = "darshilami@gmail.com"
        toaddr = loginVO.loginEmailId

        msg = MIMEMultipart()

        msg['From'] = fromaddr

        msg['To'] = toaddr

        msg['Subject'] = "your OTP"

        msg.attach(MIMEText(otpVo.otp, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(fromaddr, "iamdarshil")

        text = msg.as_string()

        server.sendmail(fromaddr, toaddr, text)

        server.quit()
        otpDAO.insertOtp(otpVo)
        return render_template('admin/getOTP.html')

@app.route('/checkOTP',methods=['POST'])
def checkOTP():
    loginVO = LoginVO()


    otpVo = OtpVO()
    otpDAO = OtpDAO()

    otpVo.otp = request.form['otp']
    otpVo.emailId = session['emailid']
    otpVo.otpActiveStatus = 'deactive'

    otpDict = otpDAO.searchOtp(otpVo)
    print otpDict

    if len(otpDict) == 0:
        return render_template('admin/getOTP.html',otperror="*incorrect otp")
    else:
        if (otpDict[0]['otp'] == otpVo.otp and otpDict[0]['emailId'] == otpVo.emailId):
            loginVO.loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))
            loginVO.loginEmailId = otpVo.emailId = session['emailid']
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
            otpDAO.updatePassword(loginVO)
            otpDAO.updateOtpstatus(otpVo)

        else:
            return render_template('admin/getOTP.html',incorrectotp="incorrect otp")
    return redirect(url_for('loadLogin'))
