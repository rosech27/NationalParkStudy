import top10yoy
import pandas as pd
import json

from flask import (
    Flask,
    render_template,
    jsonify)


app = Flask(__name__)

@app.route("/")
def home():
    Parks = top10yoy.top10parks()
    #print(type(Parks))
    return render_template("index.html", parks = Parks)

@app.route("/top10data")
def top10():
    data = top10yoy.top10parks()
    print(type(data))
    print(data)
    # return jsonify(str(data))
    return(json.dumps(data))

if __name__ == '__main__':
    app.run(debug=True)
