from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ALPSOODKEdkhfds4d5s6f4dsf"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/db.sql'
    db.init_app(app)

    from .views import views
    app.register_blueprint(views)
    from .models import Product, Category
    return app

