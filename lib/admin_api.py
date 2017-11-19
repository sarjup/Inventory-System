from models import Admin, db, admin_schema, admins_schema
from flask import flash

class AdminApi(object):
    @staticmethod
    def create_admin(request):
        fname = request.form['fname']
        lname = request.form['lname']
        uname = request.form['uname']
        pw = request.form['pw']
        addr = request.form['addr']
        ph = request.form['ph']
        if not fname or not lname or not uname or not pw or not addr or not ph:
            flash("enter all the field")
        else:
            admin = Admin(fname,lname,uname,pw,addr,ph)
            db.session.add(admin)
            db.session.commit()
            flash("create succed")
        result = admin_schema.dump(admin)
        return result

    @staticmethod
    def query_admins():
        admins = Admin.query.all()
        result = admins_schema.dump(admins)
        return result
    
    @staticmethod
    def get_admin(id):
        admin = Admin.query.get(id)
        return admin
    
    @staticmethod
    def update_admin(req , id):
        admin = Admin.query.get(id)
        fname = req.form['fname']
        lname = req.form['lname']
        uname = req.form['uname']
        pw = req.form['pw']
        addr = req.form['addr']
        ph = req.form['ph']
        if not fname or not lname or not uname or not pw or not addr or not ph:
            flash("enter all the field")
        else:
            admin.fname = fname
            admin.lname = lname
            admin.uname = uname
            admin.pw = pw
            admin.addr = addr
            admin.ph = ph

            db.session.commit()
        return admin

    @staticmethod
    def delete_admin(id):
        admin = Admin.query.get(id)
        db.session.delete(admin)
        db.session.commit()
        return admin  
        

