from flask import Flask, render_template, redirect, url_for, Response
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from typing import List

# API config
app: Flask = Flask(__name__)
app.secret_key = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"  # put your secret key here
Bootstrap(app=app)


class Form(FlaskForm):
    cafe_name: StringField = StringField(label="Cafe Name", validators=[DataRequired()])
    location: StringField = StringField(label="Cafe Location on Google Maps(URL)",
                           validators=[DataRequired(), URL(message="Invalid URL")])
    open: StringField = StringField(label="Opening Time e.g. 8AM ",
                       validators=[DataRequired()])
    close: StringField = StringField(label="Closing Time e.g. 5:30PM ",
                        validators=[DataRequired()])
    coffee_rating: SelectField = SelectField(label="Coffee Rating",
                                choices=["☕", "☕☕",  "☕☕☕",  "☕☕☕☕", "☕☕☕☕☕"],
                                validators=[])
    wifi_rating: SelectField = SelectField(label="Wifi Strength Rating ",
                              choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])
    power_sockets: SelectField = SelectField(label="Power Socket Availability",
                                choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit: SubmitField = SubmitField(label="Submit")


# The routes
@app.route("/")
def home() -> str:
    return render_template("index.html")


@app.route("/cafes")
def cafes() -> str:
    list_rows: List = []
    with open(file="cafe-data.csv", encoding="utf-8", newline='') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            list_rows.append(row)
    return render_template("cafes.html", rows=list_rows)


def add_data_to_database(detail) -> None:
    with open("cafe-data.csv", "a", encoding="utf-8", newline='') as csv_file:
        csv_file.write(",".join(detail))


@app.route("/add", methods=['POST', 'GET'])
def add() -> str | Response:
    order_form: FlaskForm = Form()
    if order_form.validate_on_submit():
        data: List[str | None] = [f"\n{order_form.cafe_name.data}", order_form.location.data, order_form.open.data, order_form.close.data, order_form.coffee_rating.data, order_form.wifi_rating.data, order_form.power_sockets.data]
        add_data_to_database(data)
        return redirect(url_for('cafes'))
    return render_template("add.html", form=order_form)


if __name__ == "__main__":
     # Only for debugging while developing
    app.run(debug=True, host="localhost", port=5000)
