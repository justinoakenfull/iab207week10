from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import datetime

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    Bootstrap5(app)

    Bcrypt(app)

    app.secret_key = 'mysecret'
    
    #Add DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'
    db.init_app(app)

    #Add Auth
    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
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

    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("404.html", error=e)
    
    @app.context_processor
    def get_context():
      year = datetime.datetime.today().year
      return dict(year=year)

    return app
