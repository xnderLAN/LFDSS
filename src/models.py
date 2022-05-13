from . import db

class Product(db.Model):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name        = db.Column(db.String(40), nullable=False, unique=True) 
    cbar        = db.Column(db.String(40), nullable=False, unique=True)
    qty         = db.Column(db.Integer)
    entry_price = db.Column(db.Float)
    final_price = db.Column(db.Integer)
    discript    = db.Column(db.String(180))
    category_id = db.Column(db.Integer, nullable=False)
    fabricant_id= db.Column(db.Integer)

class Category(db.Model):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name        = db.Column(db.String(40), nullable=False, unique=True)
    discript    = db.Column(db.String(180))
    
class Order(db.Model):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ref         = db.Column(db.String(40), nullable=False, unique=True)
    products    = db.Column(db.String(40), nullable=False)
    price       = db.Column(db.Integer)

class Fabricant(db.Model):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name        = db.Column(db.String(40), nullable=False, unique=True)