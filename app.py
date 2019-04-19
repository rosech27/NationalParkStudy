<<<<<<< HEAD
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
=======
# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import top10yoy
import json

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def home():
    #return render_template("index.html")
    Parks = top10yoy.top10parks()
    #print(Parks)
    return render_template("index.html", parks = Parks)


@app.route("/api/visits")
def pals():
    
    engine = create_engine('sqlite:///natpark.db', echo=False)
    # new_df.to_sql('visits', con=engine, if_exists='replace')
    connection = engine.connect()
    result = connection.execute("select * from visits")

    visit_data = [[r[1],r[2]] for r in result]
   # year, visitors = [r[2],r[1] for r in result]
 
    return jsonify(visit_data)
    #return (year, vistors)


@app.route("/top10data")
def top10():
    data = top10yoy.top10parks()
    #print(type(data))
    #print(data)
    # return jsonify(str(data))
    return(json.dumps(data))


if __name__ == "__main__":
    app.run()
>>>>>>> 23b9a8fdfc2c924e1172acee84c0f13ea7bcd471
