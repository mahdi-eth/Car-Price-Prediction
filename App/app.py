from flask import Flask, render_template, request
from flask_cors import CORS
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
CORS(app)
car = pd.read_csv("cleaned_car.csv")
model = pickle.load(open("LinearRegressionModel.pkl", "rb"))


@app.route("/")
def index():
    companies = sorted(car["company"].unique())
    car_models = sorted(car["name"].unique())
    years = sorted(car["year"].unique(), reverse=True)
    fuel_types = sorted(car["fuel_type"].unique())
    return render_template("index.html", companies=companies, car_models=car_models, years=years, fuel_types=fuel_types)


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    company = request.form.get("company")
    car_model = request.form.get("car_models")
    year = int(request.form.get("year"))
    fuel_type = request.form.get("fuel_type")
    kilo_driven = request.form.get("kilo_driven")

    prediction = model.predict(pd.DataFrame([[car_model, company, year, kilo_driven, fuel_type]],
                                            columns=["name", "company", "year", "kms_driven", "fuel_type"]))
    return str(np.round(prediction[0] / 80, 2))


if __name__ == "__main__":
    app.run(debug=True)
