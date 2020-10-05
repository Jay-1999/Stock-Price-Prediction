from wtforms import StringField,IntegerField

class OtpVO:
    otpId = IntegerField()
    emailId = StringField()
    otp = IntegerField()
    otpActiveStatus = StringField()
