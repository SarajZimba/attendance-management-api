# manage.py
from app.main import create_app
from app.db import db
from flask_migrate import Migrate
from flask.cli import FlaskGroup

# Create the app
app = create_app()

# Initialize Migrate
migrate = Migrate(app, db)

# Set up CLI
cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
