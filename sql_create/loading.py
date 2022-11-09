# loading.py load restaurants.db with data from restaurants.csv, food.csv and town.csv

import os 
import sqlite3
import os.path
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables import db, Restaurants, Food, Town, Cuisine
from datetime import datetime

def main():

    # Ensuring the database file exist in the same directory as this file. If not, create the file in the same directory
    if not os.path.isfile('./restaurants.db'):
        db.create_all()

    # Create engine
    engine = create_engine('sqlite:///restaurants.db', echo=False)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Load the db with 4 different tables from csv files
    load_restaurants('./csv_files/restaurants.csv', session)
    load_food('./csv_files/food.csv', session)
    load_town('./csv_files/town.csv', session)
    load_cuisine('./csv_files/cuisine.csv', session)

    session.close()
    engine.dispose()

# Load table restaurants into db
def load_restaurants(file_name, session):
     
    try: 
        # Open csv file 
        with open(file_name, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            # Iterate through reader to access every column in the csv file
            for row in reader: 
                
                # Assign the column to the respective db via the key
                restaurant = Restaurants(
                    name = row['name'],
                    location = row['location'],
                    location_description = row['location_description'],
                    postal_code = str(row['postal_code']),
                    area = row['area'],
                    cuisine = row['cuisine'],
                    description = row['description'],
                    price_lower = int(row['price_lower']),
                    price_upper = int(row['price_upper']),
                    vegetarian = bool(int(row['vegetarian'])),
                    overall_rating = float(row["overall_rating"]),
                    website = row['website'],
                    phone = int(row['phone']),
                    email = row['email'],
                    google_maps_name = row['google_maps_name'],
                    last_updated = datetime.now()
                )

                # Add dict to the session & commit it pass into the engine for adding into db
                session.add(restaurant)
                session.commit()
    
    except: 
        print("Unable to load csv file restaurants")
        return


# Load table food into db
def load_food(file_name, session):
    
    try: 
        # Open csv file 
        with open(file_name, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            # Iterate through reader to access every column in the csv file
            for row in reader: 
                
                # Assign the column to the respective db via the key
                food = Food(
                    name = row['name'],
                    description = row['description'],
                    food_rating = float(row['food_rating']),
                    spice_level = float(row["spice_level"]),
                    restaurant_id = row['restaurant_id']
                )

                # Add dict to the session & commit it pass into the engine for adding into db
                session.add(food)
                session.commit()
    
    except: 
        print("Unable to load csv file food")
        return


# Load table town into db
def load_town(file_name, session):

    try: 
        # Open csv file 
        with open(file_name, newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            # Iterate through reader to access every column in the csv file
            for row in reader: 
                
                # Assign the column to the respective db via the key
                town = Town(
                    area_name = row['name'],
                    blue_code = row['blue_code'],
                    orange_code = row['orange_code']
                )

                # Add dict to the session & commit it pass into the engine for adding into db
                session.add(town)
                session.commit()
    
    except:
        
        print("Unable to load csv file town")
        return

def load_cuisine(file_name, session):

    try: 
        # Open csv file 
        with open(file_name, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Iterate through reader to access every column in the csv file
            for row in reader: 
                
                # Assign the column to the respective db via the key
                cuisine = Cuisine(
                    cuisine_name = row['cuisine'],
                    writeup = row['writeup']
                )

                # Add dict to the session & commit it pass into the engine for adding into db
                session.add(cuisine)
                session.commit()
    
    except:
        
        print("Unable to load csv file cuisine")
        return

if __name__ == "__main__":
    main()