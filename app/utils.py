def create_app():
    from flask import Flask
    from .routes import main
    from config import Config
    app = Flask(__name__)
    app.register_blueprint(main)
    app.config.from_object(Config)
    return app
