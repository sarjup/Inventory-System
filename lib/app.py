from flask import Flask, render_template, request, flash, url_for, redirect, jsonify
from os import path
import logging

from models import db, ma
from models import admin_schema,member_schema
from config import postgres
from admin_api import AdminApi
from member_api import MemberApi

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# template path
template_dir = path.abspath('./templates')
app = Flask(__name__, template_folder=template_dir)

# ...app config...
app.config['SQLALCHEMY_DATABASE_URI'] = postgres
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hello'

# ...initialize db...
db.init_app(app)

# ...initialize ma...
ma.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

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
    print ('first_name %s' % request.form['fname'])
    admin = AdminApi.update_admin(request , id)
    return admin_schema.jsonify(admin)

# delete a admin
@app.route('/api/admins/<id>', methods = ['DELETE'])
def delete_admin(id):
    admin = AdminApi.delete_admin(id)
    return admin_schema.jsonify(admin)

###################################################################

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

