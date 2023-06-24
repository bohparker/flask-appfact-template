from sqlalchemy import select
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf import CSRFProtect


db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth_bp.login'
    login_manager.login_message_category = 'info'

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        id = int(user_id)
        return db.session.get(User, id)

    from .views_bp import views_bp
    app.register_blueprint(views_bp)

    from .auth_bp import auth_bp
    app.register_blueprint(auth_bp)

    # error handling
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
    
    @app.errorhandler(403)
    def permission_denied(e):
        return render_template('403.html'), 403

    return app