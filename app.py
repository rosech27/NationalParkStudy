# Import Dependencies 
from flask import Flask, render_template, redirect
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import pymongo

import os


# Hidden authetication file
#import config 

# Create an instance of Flask app
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'
mongo = pymongo.MongoClient(conn)



# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def home(): 

    # Find data
    # mars_info = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html")

# Route that will trigger scrape function
# @app.route("/")
# def scrape(): 

    # Run scrapped functions
    # mars_info = mongo.db.mars_info
    # mars_info.update({}, mars_data, upsert=True)
    # return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)