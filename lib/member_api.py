from models import Member, db, member_schema, members_schema
from flask import flash

class MemberApi(object):
    @staticmethod
    def create_member(request):
        fname = request.form['fname']
        lname = request.form['lname']
        addr = request.form['addr']
        ph = request.form['ph']
        type = request.form['type']
        if not fname or not lname or not addr or not ph or not type:
            flash("enter all the field")
        else:
            member = Member(fname,lname,addr,ph,type)
            db.session.add(member)
            db.session.commit()
            flash("create succed")
        result = member_schema.dump(member)
        return result

    @staticmethod
    def query_members():
        members = Member.query.all()
        result = members_schema.dump(members)
        return result
    
    @staticmethod
    def get_member(id):
        member = Member.query.get(id)
        return member
    
    @staticmethod
    def update_member(req , id):
        member = Member.query.get(id)
        fname = req.form['fname']
        lname = req.form['lname']
        addr = req.form['addr']
        ph = req.form['ph']
        type = req.form['type']
        if not fname or not lname or not type or not addr or not ph:
            flash("enter all the field")
        else:
            member.fname = fname
            member.lname = lname
            member.addr = addr
            member.ph = ph
            member.type = type

            db.session.commit()
        return member

    @staticmethod
    def delete_member(id):
        member = Member.query.get(id)
        db.session.delete(member)
        db.session.commit()
        return member  
        

