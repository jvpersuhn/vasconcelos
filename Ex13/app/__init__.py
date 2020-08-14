from flask import Flask
from Ex13.app.history.view import app_empresa
from Ex13.database import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/empresa"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    db.init_app(app)
    _register_blueprint(app)
    return app

def _register_blueprint(app):
    app.register_blueprint(app_empresa)


