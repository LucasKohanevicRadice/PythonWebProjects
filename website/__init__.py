from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'gugugaga'

    from .views import views # From views file, imports the views blueprint

    app.register_blueprint(views, url_prefix="/") # Registers the blueprint into the app

    return app

