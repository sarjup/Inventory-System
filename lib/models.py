from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from sqlalchemy.dialects.postgresql import NUMERIC

from flask_marshmallow import Marshmallow
import datetime

db = SQLAlchemy()
ma = Marshmallow()

# Admin Model
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

# Member Model
class Member(db.Model):
    __tablename__ = 'tbl_member'
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(100), nullable = False)
    lname = db.Column(db.String(100))
    addr = db.Column(db.String(100))
    ph = db.Column(db.String(50), nullable = False)
    d_date = db.Column(db.Date, nullable = False)
    e_date = db.Column(db.Date, nullable = False)
    type = db.Column(db.String(50), nullable = False)

    def __init__(self, fname, lname, addr, ph, d_date, e_date, type):
        self.fname = fname
        self.lname = lname
        self.addr = addr
        self.ph = ph
        self.d_date = d_date
        self.e_date = e_date
        self.type = type

    def __repr__(self):
        return self.fname

# Supplier Model
class Supplier(db.Model):
    __tablename__ = 'tbl_supplier'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    addr = db.Column(db.String(100))
    ph = db.Column(db.String(50), nullable = False)
    type = db.Column(db.String(50), nullable = False)

    def __init__(self, name, addr, ph, type):
        self.name = name
        self.addr = addr
        self.ph = ph
        self.type = type

    def __repr__(self):
        return self.name

# Product Model
class Product(db.Model):
    __tablename__ = 'tbl_product'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(100), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    price = db.Column(db.Numeric(8,2), nullable = False)

    __table_args__ = (
        CheckConstraint(quantity >= 0, name='check_quantity_positive'),
        {})

    def __init__(self, name, description,price, quantity=0):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
    def __repr__(self):
        return self.name


    

# Schema Classes
class AdminSchema(ma.Schema):
    class Meta:
        # Field to expose
        fields = ('id','fname','lname','uname','pw','addr','ph')

class MemberSchema(ma.Schema):
    class Meta:
        fields = ('id','fname','lname','addr','ph', 'd_date', 'e_date', 'type')

class SupplierSchema(ma.Schema):
    class Meta:
        fields = ('id','name','addr','ph','type')

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','description','price')


# Schema here
admin_schema = AdminSchema()
admins_schema = AdminSchema(many = True)

member_schema = MemberSchema()
members_schema = MemberSchema(many = True)

supplier_schema = SupplierSchema()
suppliers_schema = SupplierSchema(many = True)

product_schema = ProductSchema()
products_schema = ProductSchema(many = True)




    
