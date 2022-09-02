from ..utils.db import db

class Bill(db.Model):
    __tablename__ = "bill"
    id = db.Column(db.Integer, primary_key=True)
    date_bill = db.Column(db.Date, nullable=False)
    value = db.Column(db.Integer, nullable=False)
    type_ = db.Column("type",db.Integer, nullable=False)
    observation = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users', backref='bills')

    def __init__(self, id,date_bill,user_id,value,type_,observation):
        self.id=id
        self.date_bill=date_bill
        self.user_id=user_id
        self.value=value
        self.type_=type_
        self.observation=observation

    def __rpr__(self):
        return "date_bill: {"+self.date_bill+"} value:{"+self.value+"} type: {"+self.type_+"} observation:{"+self.observation+"} " 