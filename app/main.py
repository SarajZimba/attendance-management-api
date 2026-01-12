from flask import Flask
from app.db import db
from app.config.development import DevelopmentConfig
from dotenv import load_dotenv
from app.routes.attendance_routes import attendance_bp
from app.routes.frontend_routes import frontend_bp

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(attendance_bp, url_prefix="/attendance")
    app.register_blueprint(frontend_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
