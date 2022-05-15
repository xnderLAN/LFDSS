from flask import Blueprint, jsonify, redirect, request, render_template, url_for
from uuid import uuid4

from sqlalchemy import false
from .commit_get import *

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return render_template("index.html", fact_id=str(uuid4()), title="LFDSS", home="active")

@views.route("/insertion", methods=["POST", "GET"])
def insertion():
    if request.method == "GET":
        return render_template("insertion.html", title="LFDSS",
                               ins="active", cat=get_db("category", ["all"]),
                               fab=get_db("fabricant", ["all"]))

@views.route("/ravitaillement", methods=["POST", "GET"])
def rav():
    return render_template("rav.html", rav="active")

@views.route("/stock", methods=["POST", "GET"])
def stock():
    cat = get_cat()
    fab = get_fab()
    if request.method=="GET":
        product_list = get_db("produit", ["all"])
        parsed  = [{"name":i.name, 
                    "fab":get_by_id("fabricant", i.fabricant_id), 
                    "category":get_by_id("category", i.category_id), 
                    "cbar":i.cbar, "prix":i.final_price, "qty":i.qty} for i in product_list]
        
        return render_template("stock.html", stock="active", product=parsed, category_list=cat, fabricant_list=fab)
    else: 
        category = request.form.get("category")
        fabricant= request.form.get("fabricant")
        if not category and not fabricant:
            return redirect(url_for("views.stock"))
        elif category and fabricant:
            product_list = get_product_by_cat_fab(int(fabricant), int(category))
            parsed  = [{"name":i.name, 
                    "fab":get_by_id("fabricant", i.fabricant_id), 
                    "category":get_by_id("category", i.category_id), 
                    "cbar":i.cbar, "prix":i.final_price, "qty":i.qty} for i in product_list]
            return render_template("stock.html", stock="active", product=parsed, category_list=cat, fabricant_list=fab)
        elif fabricant:
            product_list = get_product_by_fab(int(fabricant))
            parsed  = [{"name":i.name, 
                    "fab":get_by_id("fabricant", i.fabricant_id), 
                    "category":get_by_id("category", i.category_id), 
                    "cbar":i.cbar, "prix":i.final_price, "qty":i.qty} for i in product_list]
            return render_template("stock.html", stock="active", product=parsed, category_list=cat, fabricant_list=fab)
        elif category:
            product_list = get_product_by_cat(int(category))
            parsed  = [{"name":i.name, 
                    "fab":get_by_id("fabricant", i.fabricant_id), 
                    "category":get_by_id("category", i.category_id), 
                    "cbar":i.cbar, "prix":i.final_price, "qty":i.qty} for i in product_list]
            return render_template("stock.html", stock="active", product=parsed, category_list=cat, fabricant_list=fab)

        

        return render_template("stock.html", stock="active", product=parsed, category_list=cat, fabricant_list=fab)


@views.route("/finance", methods=["POST", "GET"])
def finance():
    return render_template("finance.html", finance="active")

@views.route("/add/<element>", methods=["POST"])
def add(element):
    if request.method == "POST":
       
        if element == "product":
            name = request.form.get("name")
            c_bar= request.form.get("c_bar")
            qty  = request.form.get("qty")
            entry_price  = request.form.get("entry_price") 
            final_price  = request.form.get("final_price") 
            discript = request.form.get("discript") 
            category = request.form.get("category")
            fabricant= request.form.get("fabricant")
            
            c = get_db("category", [category])
            f = get_db("fabricant", [fabricant])
            
            print(entry_price)
            commit = commit_db("product", [name, c_bar, qty, entry_price, final_price, discript, c, f ])
            return redirect(url_for('views.insertion'))

        elif element == "category":
            name = request.form.get("name")
            discript  = request.form.get("discript")
            commit = commit_db("category", [name, discript])
            return redirect(url_for('views.insertion'))
        
        elif element == "fabricant":
            name = request.form.get("name")
            
            commit = commit_db("fabricant", [name])
            return redirect(url_for('views.insertion'))

    return redirect(url_for('views.index'))

@views.route("/get", methods=["POST"])
def get_item():
    rep = request.json
    if "c_bar" in rep.keys():
        product = get_product_by_cbar(rep["c_bar"])
        if product:
            data = {"name": product.name, "prix": product.final_price}
            return jsonify(data)
    return jsonify({"error":"True"})

@views.route("/order", methods=['POST'])
def order():
    data = request.json
    if "product" in data.keys():
        product = data["product"]
        if len(product):
            st_set = set_db(product)
            if st_set:
                st_commit = commit_db("order", [data["or_id"], data["order_price"], str(data["product"])])
                return jsonify({"error":"False"})

    return jsonify({"error":"True"})

