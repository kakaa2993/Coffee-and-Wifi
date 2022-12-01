from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, URL
import csv

app = Flask(__name__)
app.secret_key = "Kakaa2993@t"
Bootstrap(app=app)


class Form(FlaskForm):
    cafe_name = StringField(label="Cafe Name", )
    location = StringField(label="Cafe Location on Google Maps(URL)",)
    open = StringField(label="Opening Time e.g. 8AM ", )
    close = StringField(label="Closing Time e.g. 5:30PM ", )
    coffee = SelectField(label="Coffee Rating", choices=[(1,"☕"),(2,"☕☕"),(3,"☕☕☕"), (4,"☕☕☕☕"),(5,"☕☕☕☕☕")], )
    wifi = SelectField(label="Wifi Strength Rating ", choices=[(False, "✘"), (1,"💪"), (2, "💪💪"), (3, "💪💪💪"), (4, "💪💪💪💪"), (5, "💪💪💪💪💪")], )
    power = SelectField(label="Power Socket Availability", choices=[(False, "✘"), (1, "🔌"), (2, "🔌🔌"), (3, "🔌🔌🔌"), (4, "🔌🔌🔌🔌"), (5, "🔌🔌🔌🔌🔌")], )
    submit = SubmitField(label="Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def cafes():
    with open(file="cafe-data.csv", encoding="utf-8") as file:
        csv_data = csv.reader(file)
        # for row in csv_data:
        #     print(row)
        # print(csv_data)
        return render_template("cafes.html", rows=csv_data)


@app.route("/add")
def add():
    order_form = Form()
    return render_template("add.html", form=order_form)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
