from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    Bootstrap5(app)

    app.secret_key = 'mysecret'
    
    #Add DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'
    db.init_app(app)
    
    #Set upload folder
    UPLOAD_FOLDER = 'static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    #add Blueprints
    from . import views
    app.register_blueprint(views.mainbp)

    #add destinations
    from . import destinations
    app.register_blueprint(destinations.destinationBlueprint)
    from . import auth
    app.register_blueprint(auth.authBlueprint)

    return app

