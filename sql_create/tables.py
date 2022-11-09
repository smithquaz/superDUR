# tables.py define the Model used in the sqlite3 database to create restaurants.db

# Disabling pylint error (it provides false positives)
# pylint: disable=no-member

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurants.db'
db = SQLAlchemy(app)

class Restaurants(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(70), nullable = False)
    location = db.Column(db.Text, nullable = False)
    location_description = db.Column(db.Text, nullable = False)
    postal_code = db.Column(db.String(6), nullable = False)
    area = db.Column(db.String(20), nullable = False)
    cuisine = db.Column(db.String(20), nullable = False)
    description = db.Column(db.Text, nullable = False)
    price_lower = db.Column(db.Integer, nullable = False)
    price_upper = db.Column(db.Integer, nullable = False)
    vegetarian = db.Column(db.Boolean, nullable = False)
    overall_rating = db.Column(db.Float, nullable = False)
    website = db.Column(db.Text)
    phone = db.Column(db.Integer)
    email = db.Column(db.Text)
    google_maps_name = db.Column(db.Text, nullable = False)
    last_updated = db.Column(db.DateTime, nullable = False)
    food = db.relationship('Food', backref="Restaurants", lazy = True)
    town = db.relationship('Town', backref="Restaurants", lazy = True)
    
    def __init__(self, **kwargs):
        super(Restaurants, self).__init__(**kwargs)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(320), nullable = False)
    description = db.Column(db.Text, nullable = False)
    food_rating = db.Column(db.Float, nullable = False)
    spice_level = db.Column(db.Float, nullable = False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable = False)

    def __init__(self, **kwargs):
        super(Food, self).__init__(**kwargs)

class Town(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    area_name = db.Column(db.String(30), db.ForeignKey('restaurants.area'), nullable = False)
    blue_code = db.Column(db.Integer, nullable = False)
    orange_code = db.Column(db.Integer, nullable = False)
    
    def __init__(self, **kwargs):
        super(Town, self).__init__(**kwargs)

# Note: Cuisine table does not link back to original restaurants table
class Cuisine(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cuisine_name = db.Column(db.String(30), nullable = False)
    writeup = db.Column(db.Text, nullable = False)
    
    def __init__(self, **kwargs):
        super(Cuisine, self).__init__(**kwargs)