from flask import Blueprint, jsonify, redirect, request, render_template, url_for
from uuid import uuid4
from .commit_get import commit_db, get_db, set_db

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
    return "rav"

@views.route("/stock", methods=["POST", "GET"])
def stock():
    return render_template("stock.html", stock="active")

@views.route("/finance", methods=["POST", "GET"])
def finance():
    return "Finance"

@views.route("/add/<element>", methods=["POST"])
def add(element):
    if request.method == "POST":
       
        if element == "product":
            name = request.form.get("name")
            c_bar= request.form.get("c_bar")
            qty  = request.form.get("qty")
            entry_price  = request.form.get("entry_price") 
            final_price  = request.form.get("final_price") 
            discript  = request.form.get("discript") 
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
    rep = request.json["c_bar"]
    product = get_db("produit", [rep])
    data = {"name": product.name, "prix": product.final_price}
    return jsonify(data)

@views.route("/req")
def req():
    return render_template("sc.html")
