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
        o = Order(ref=values[0], price=values[1], products=values[2])
        db.session.add(o)
        db.session.commit()
        return "ok"

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
            return db.session.query(Product).all()
            
        else:
            return db.session.query(Product).filter(Product.cbar==values[0]).all()[0]

def get_product_by_cbar(cbar):
    try:
        return db.session.query(Product).filter(Product.cbar==cbar).all()[0]
    except:
        return False

def set_db(product):

    for key in product.keys():
        try:
            p = db.session.query(Product).filter(Product.name==key).all()[0]
        except:
            return False
        if int(p.qty) > int(product[key]):
            p.qty = int(p.qty) - int(product[key])
            db.session.commit()
    return True


def get_product_by_cat(cat_id):
    return db.session.query(Product).filter(Product.category_id==cat_id).all()

def get_cat():
    return [ {"id":i.id, "name":i.name} for i in db.session.query(Category).all() ]
def get_fab():
    return [ {"id":i.id, "name":i.name} for i in db.session.query(Fabricant).all() ]

def get_by_id(item, id):
    if item == "fabricant":
        return db.session.query(Fabricant).filter(Fabricant.id==id).all()[0].name

    if item == "category":
        return db.session.query(Category).filter(Category.id==id).all()[0].name

def get_product_by_cat(id_cat):
    return [ i for i in db.session.query(Product).filter(Product.category_id==id_cat).all()]

def get_product_by_fab(id_fab):
    return [ i for i in db.session.query(Product).filter(Product.fabricant_id==id_fab).all()]
    
def get_product_by_cat_fab(id_fab, id_cat):
    return [ i for i in db.session.query(Product).filter(Product.category_id==id_cat, Product.fabricant_id==id_fab ).all()]
 