from wtforms import StringField,IntegerField

class LoginVO:
    loginId = IntegerField()
    loginEmailId = StringField()
    loginPassword = StringField()
    loginRole = StringField()
    loginActiveStatus = StringField()