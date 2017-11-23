# third parties libraries
from flask import Flask, render_template, request, flash, url_for, redirect, jsonify, session
from os import path
from json import dumps
import logging
from werkzeug.routing import BaseConverter

# our libraries
from models import db, ma
from models import admin_schema,member_schema,supplier_schema,product_schema
from config import postgres
from admin_api import AdminApi
from member_api import MemberApi
from supplier_api import SupplierApi
from product_api import ProductApi

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# # template path
# template_dir = path.abspath('templates')
# app = Flask(__name__, template_folder=template_dir)

# static_dir = path.abspath('./static')
# app = Flask(__name__, static_folder=static_dir)

# ...app config...
app.config['SQLALCHEMY_DATABASE_URI'] = postgres
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hello'

# ...initialize db...
db.init_app(app)

# ...initialize ma...
ma.init_app(app)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter


# def checkLogin():
#     if session.get('logged_in'):
#         print "hello"
#         return True
#     return render_template('landing.html')
#         # username = session.get('username')
    


@app.route('/')
def index():
        if session.get('logged_in'):
           
            username = session.get('username')
            return render_template('index.html', username=username)
        return render_template('landing.html')
    
@app.route('/api/login', methods = ['POST'])
def login():
    admin = AdminApi.login_admin(request)
    # print '=='*50
    # print admin
    if admin:
        session['username'] = request.form['uname']
        # print session.get('username')
        session['logged_in'] = True

    else:
        flash('Username or Password is incorrect')
    return redirect(url_for('index'))

@app.route('/api/logout', methods = ['GET'])
def logout():
    if session.get('logged_in'):
        session.pop('username',None)
        session['logged_in'] = False
    return redirect(url_for('index'))

@app.route('/admin-create')
def admin_form():
    if session.get('logged_in'):
        username = session.get('username')
        return render_template('createAdmin.html', username=username)
    return redirect(url_for('index'))

@app.route('/admins')
def admin_list():
    if session.get('logged_in'):
        username = session.get('username')
        return render_template('adminList.html', username=username)
    return redirect(url_for('index'))


@app.route('/Products')
def product():
    if session.get('logged_in'):
        username = session.get('username')
        return render_template('products.html', username=username)
    return redirect(url_for('index'))
    


    

# ------------------------ admin crud --------------------------------
# create admin
@app.route('/api/admins', methods = ['POST'])
def create_admin():
    new_admin = AdminApi.create_admin(request)
    return jsonify(new_admin.data)

# get all admin
@app.route('/api/admins', methods = ['GET'])
def get_admins():
    admins = AdminApi.query_admins()
    return jsonify(admins.data)

# get a admin
@app.route('/api/admins/<id>', methods = ['GET'])
def get_admin(id):
    admin = AdminApi.get_admin(id)
    return admin_schema.jsonify(admin)

# update admin
@app.route('/api/admins/<id>', methods = ['PUT'])
def update_admin(id):
    # print ('first_name %s' % request.form['fname'])
    admin = AdminApi.update_admin(request , id)
    return admin_schema.jsonify(admin)

# delete a admin
@app.route('/api/admins/<id>', methods = ['DELETE'])
def delete_admin(id):
    admin = AdminApi.delete_admin(id)
    return admin_schema.jsonify(admin)

# ------------------ member crud --------------------------

# create member
@app.route('/api/members', methods = ['POST'])
def create_member():
    new_member = MemberApi.create_member(request)
    return jsonify(new_member.data)

# get all member
@app.route('/api/members', methods = ['GET'])
def get_members():
    members = MemberApi.query_members()
    return jsonify(members.data)

# get a member
@app.route('/api/members/<id>', methods = ['GET'])
def get_member(id):
    member = MemberApi.get_member(id)
    return member_schema.jsonify(member)

# update member
@app.route('/api/members/<id>', methods = ['PUT'])
def update_member(id):
    # print ('first_name %s' % request.form['fname'])
    member = MemberApi.update_member(request , id)
    return member_schema.jsonify(member)

# delete a member
@app.route('/api/members/<id>', methods = ['DELETE'])
def delete_member(id):
    member = MemberApi.delete_member(id)
    return member_schema.jsonify(member)


#------------- Supplier Crud --------------------------
# create supplier
@app.route('/api/suppliers', methods = ['POST'])
def create_supplier():
    new_supplier = SupplierApi.create_supplier(request)
    return jsonify(new_supplier.data)

# get all supplier
@app.route('/api/suppliers', methods = ['GET'])
def get_suppliers():
    suppliers = SupplierApi.query_suppliers()
    return jsonify(suppliers.data)

# get a supplier
@app.route('/api/suppliers/<id>', methods = ['GET'])
def get_supplier(id):
    supplier = SupplierApi.get_supplier(id)
    return supplier_schema.jsonify(supplier)

# update supplier
@app.route('/api/suppliers/<id>', methods = ['PUT'])
def update_supplier(id):
    # print ('first_name %s' % request.form['fname'])
    supplier = SupplierApi.update_supplier(request , id)
    return supplier_schema.jsonify(supplier)

# delete a supplier
@app.route('/api/suppliers/<id>', methods = ['DELETE'])
def delete_supplier(id):
    supplier = SupplierApi.delete_supplier(id)
    return supplier_schema.jsonify(supplier)

#------------product crud -----------------------------------
# create product
@app.route('/api/products', methods = ['POST'])
def create_product():
    new_product = ProductApi.create_product(request)
    return product_schema.dumps(new_product,default=str)

# get all product
@app.route('/api/products', methods = ['GET'])
def get_products():
    products = ProductApi.query_products()
    return dumps(products.data, default=str)

# get a product
@app.route('/api/products/<id>', methods = ['GET'])
def get_product(id):
    product = ProductApi.get_product(id)
    return product_schema.dumps(product, default= str)

# update product
@app.route('/api/products/<id>', methods = ['PUT'])
def update_product(id):
    product = ProductApi.update_product(request , id)
    return product_schema.dumps(product, default = str)

@app.route('/api/products/<id>', methods = ['DELETE'])
def delete_product(id):
    product = ProductApi.delete_product(id)
    return product_schema.dumps(product,default = str)

# -------------------------purchase crud -----------------------






