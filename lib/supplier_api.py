from models import Supplier, db, supplier_schema, suppliers_schema
from flask import flash

class SupplierApi(object):
    @staticmethod
    def create_supplier(request):
        name = request.form['name']
        addr = request.form['addr']
        ph = request.form['ph']
        type = request.form['type']
        if not name or not addr or not ph or not type:
            flash("enter all the field")
        else:
            supplier = Supplier(name,addr,ph,type)
            db.session.add(supplier)
            db.session.commit()
            flash("create succed")
        result = supplier_schema.dump(supplier)
        return result

    @staticmethod
    def query_suppliers():
        suppliers = Supplier.query.all()
        result = suppliers_schema.dump(suppliers)
        return result
    
    @staticmethod
    def get_supplier(id):
        supplier = Supplier.query.get(id)
        return supplier
    
    @staticmethod
    def update_supplier(req , id):
        supplier = Supplier.query.get(id)
        name = req.form['name']
        addr = req.form['addr']
        ph = req.form['ph']
        type = req.form['type']
        if not name or not type or not addr or not ph:
            flash("enter all the field")
        else:
            supplier.name = name
            supplier.addr = addr
            supplier.ph = ph
            supplier.type = type

            db.session.commit()
        return supplier

    @staticmethod
    def delete_supplier(id):
        supplier = Supplier.query.get(id)
        db.session.delete(supplier)
        db.session.commit()
        return supplier  
        

