from unicodedata import category, name
from .models import Product, Category, Order, Fabricant
from . import db

def commit_db(item, values):
    if item == "category":
        c = Category(name=values[0], discript=values[1])
        db.session.add(c)
        db.session.commit()
        return "ok"
    
    elif item == "fabricant":
        f = Fabricant(name=values[0])
        db.session.add(f)
        db.session.commit()
        return "ok"
    
    elif item == "product":
        p = Product(name=values[0], cbar=values[1], qty=values[2], entry_price=values[3],
        final_price=values[4], discript=values[5], category_id=values[6], fabricant_id=values[7])
        db.session.add(p)
        db.session.commit()

    elif item == "order":
        pass

def get_db(item, values):
    if item == "category":
        if values[0]=="all":
            return [i[0] for i in db.session.query(Category.name).all()]
        else:
            return db.session.query(Category.id).filter(Category.name==values[0]).all()[0][0]

    elif item == "fabricant":
        if values[0]=="all":
            return [i[0] for i in db.session.query(Fabricant.name).all()]
        else:
            return db.session.query(Fabricant.id).filter(Fabricant.name==values[0]).all()[0][0]

    elif item == "produit":
        if values[0]== "all":
            pass
        else:
            return db.session.query(Product).filter(Product.cbar==values[0]).all()[0]
def set_db(item, values):
    pass