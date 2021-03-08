import pandas as pd
from flask import Flask, render_template




app = Flask(__name__)

@app.route("/")
def index():
    correct = pd.read_csv("./source/correct.csv")
    origin = pd.read_csv("./source/origin.csv")
    return render_template("index.html", 
                           correct_columns=list(correct.columns),
                           origin_columns=list(origin.columns),
                           correct_datum={col: list(correct[col].unique()) for col in correct.columns},
                           origin_datum={col: list(origin[col].unique()) for col in origin.columns})


app.run()
