from ssl import ALERT_DESCRIPTION_CERTIFICATE_EXPIRED
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'itsalive'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app