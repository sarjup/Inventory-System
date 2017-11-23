from models import Member, db, member_schema, members_schema
from flask import flash

class MemberApi(object):
    @staticmethod
    def create_member(request):
        fname = request.form['fname']
        lname = request.form['lname']
        addr = request.form['addr']
        ph = request.form['ph']
        d_date = request.form['d_date']
        e_date = request.form['e_date']
        type = request.form['type']
        if not fname or not lname or not addr or not ph or not d_date or not e_date or not type:
            flash("enter all the field")
        else:
            member = Member(fname,lname,addr,ph, d_date, e_date,type)
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
        d_date = req.form['d_date']
        e_date = req.form['e_date']
        type = req.form['type']
        if not fname or not lname or not type or not addr or not d_date or not e_date or not ph:
            flash("enter all the field")
        else:
            member.fname = fname
            member.lname = lname
            member.addr = addr
            member.ph = ph
            member.d_date = d_date
            member.e_date = e_date
            member.type = type

            db.session.commit()
        return member

    @staticmethod
    def delete_member(id):
        member = Member.query.get(id)
        db.session.delete(member)
        db.session.commit()
        return member  
        

