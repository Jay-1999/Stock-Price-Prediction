from wtforms import IntegerField, StringField


class ComplaintVO():
    complaintId = IntegerField()
    complaintSubject = StringField()
    complaintDescription = StringField()
    complaintTo_LoginId = IntegerField()
    complaintFrom_LoginId = IntegerField()
    complaintDate = StringField()
    complaintTime = StringField()
    complaintReply = StringField()
    complaintStatus = StringField()
    complaintActiveStatus = StringField()
