from wtforms import StringField,IntegerField

class RegisterVO:
    registerId = IntegerField()
    register_LoginId = IntegerField()
    registerFirstName = StringField()
    registerLastName = StringField()
    registerGender = StringField()
    registerAddress = StringField()
    registerPincode = IntegerField()
    registerContact = IntegerField()
    registerEmailId = StringField()
    registerDate = StringField()
    registerTime = StringField()
    registerActiveStatus = StringField()