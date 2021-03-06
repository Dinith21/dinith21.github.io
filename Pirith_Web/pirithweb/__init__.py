from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from pirithweb.config import Config
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    # from pirithweb.models import User, Post
    # admin = Admin(app)
    # admin.add_view(ModelView(User, db.session))
    # admin.add_view(ModelView(Post, db.session))

    from pirithweb.users.routes import users
    from pirithweb.posts.routes import posts
    from pirithweb.main.routes import main
    from pirithweb.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
