from models import Product, db, product_schema, products_schema
from flask import flash

class ProductApi(object):
    @staticmethod
    def create_product(request):
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        if not name or not description or not price:
            flash("enter all the field")
        else:
            product = Product(name,description,price)
            db.session.add(product)
            db.session.commit()
            flash("create succed")
        result = product
        return result

    @staticmethod
    def query_products():
        products = Product.query.all()
        result = products_schema.dump(products)
        return result
    
    @staticmethod
    def get_product(id):
        product = Product.query.get(id)
        return product
    
    @staticmethod
    def update_product(req , id):
        product = Product.query.get(id)
        name = req.form['name']
        description = req.form['description']
        price = req.form['price']
        if not name or not description or not price:
            flash("enter all the field")
        else:
            product.name = name
            product.description = description
            product.price = price
            
            db.session.commit()
        return product

    @staticmethod
    def delete_product(id):
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return product  
        

