from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define your models here
class YourModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Function to create all tables
def create_tables():
    with app.app_context():  # Ensures an application context
        db.create_all()

if __name__ == "__main__":
    create_tables()  # Create tables when running app.py
    app.run(debug=True)

