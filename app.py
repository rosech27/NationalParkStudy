# Import Dependencies 
from flask import Flask, render_template, redirect
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo
import pandas as pd
import pymongo

# Hidden authetication file
#import config 

# Create an instance of Flask app
app = Flask(__name__)
# Create connection variable
# conn = 'mongodb://localhost:27017'
# mongo = pymongo.MongoClient(conn)
mongo = PyMongo(app, uri="mongodb://localhost:27017/records_db")

# function to scrape data and push to mongoDB
url = 'https://en.wikipedia.org/wiki/List_of_national_parks_of_the_United_States'
table = pd.read_html(url)
nat_park_df = table[1]
nat_park_df.columns = ['Name', 'Image', 'Location', 'Date established', 'Area', 'Recreation visitors', 'Description']
nat_park_df = nat_park_df.drop([0])
nat_park_df = nat_park_df.drop(columns=['Image', 'Area'])
# new data frame with split value columns 
new = nat_park_df["Location"].str.split("/", n = 1, expand = True)
nat_park_df["Location"] = new[1]

data = nat_park_df.to_dict(orient='records')
# nps_data = mongo.db.nps_data.find_one()

# nps_data.update({}, data, upsert=True)
mongo.db.collection.insert_many(data)
# Update the Mongo database using update and upsert=True
# mongo.db.collection.update({}, data, upsert=True)

# Create route that renders index.html template
@app.route("/")
def root():
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
