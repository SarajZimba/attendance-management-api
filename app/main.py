from flask import Flask
from app.db import db
from app.config.development import DevelopmentConfig
from dotenv import load_dotenv
from app.routes.attendance_routes import attendance_bp
from app.routes.frontend_routes import frontend_bp
# in main.py, inside create_app()
from app.routes.user_routes import user_bp
from app.routes.report_routes import report_bp
from flask_migrate import Migrate

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(attendance_bp, url_prefix="/attendance")
    app.register_blueprint(frontend_bp)
    app.register_blueprint(user_bp, url_prefix="/users")

    app.register_blueprint(report_bp, url_prefix="/reports")

    return app

app = create_app()

# 🔹 Initialize Flask-Migrate
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
