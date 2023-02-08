from flask import Flask
import os
from app.models import db

postgres_db = os.environ['POSTGRES_DB']
postgres_host = os.environ['DB_HOST']
postgres_db_user = os.environ['DB_USERNAME']
postgres_db_pass = os.environ['DB_PASSWORD']
secret_key = os.environ['SECRET_KEY']

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{postgres_db_user}:{postgres_db_pass}@{postgres_host}/{postgres_db}"
app.config['SECRET_KEY'] = secret_key

# initialize the app with the extension
db.init_app(app)


# Import configuration profile based on FLASK_ENV variable - defaults to Production
if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object('config.DevelopmentConfig')
elif os.environ.get('FLASK_ENV') == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object('config.ProductionConfig')

# Initialize db
with app.app_context():
    db.create_all()

from app.routes import *