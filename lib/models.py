from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime

db = SQLAlchemy()
ma = Marshmallow()

class Admin(db.Model):
    '''Model for tbl_admin'''
    __tablename__ = 'tbl_admin'

    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(100), nullable = False)
    lname = db.Column(db.String(100))
    uname = db.Column(db.String(100),unique=True, nullable = False)
    # email = db.Column(db.String(100), key = 'email')
    pw = db.Column(db.String(100), nullable = False)
    addr = db.Column(db.String(100))
    ph = db.Column(db.String, unique = True)

    def __init__(self, fname, lname, uname, pw, addr, ph):
        self.fname = fname
        self.lname = lname
        self.uname = uname
        self.pw = pw
        self.addr = addr
        self.ph = ph

    def __repr__(self):
        return self.fname

class Member(db.Model):
    __tablename__ = 'tbl_member'
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(100), nullable = False)
    lname = db.Column(db.String(100))
    addr = db.Column(db.String(100))
    ph = db.Column(db.String(50), nullable = False)
    type = db.Column(db.String(50), nullable = False)

    def __init__(self, fname, lname, addr, ph, type):
        self.fname = fname
        self.lname = lname
        self.addr = addr
        self.ph = ph
        self.type = type

    def __repr__(self):
        return self.fname



# Schema Classes
class AdminSchema(ma.Schema):
    class Meta:
        # Field to expose
        fields = ('id','fname','lname','uname','pw','addr','ph')

class MemberSchema(ma.Schema):
    class Meta:
        fields = ('id','fname','lname','addr','ph','type')


# Schema here
admin_schema = AdminSchema()
admins_schema = AdminSchema(many = True)

member_schema = MemberSchema()
members_schema = MemberSchema(many = True)

    
