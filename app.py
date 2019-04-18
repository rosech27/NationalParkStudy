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
