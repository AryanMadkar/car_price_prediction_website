import pickle as pkl
from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)
df = pd.read_csv("C:/Users/aryan/OneDrive/Desktop/carprice/Clean_car.csv")

model = pkl.load(open("C:/Users/aryan/OneDrive/Desktop/carprice/Linearmodelcar.pkl","rb"))
@app.route('/')
def index():
    companies = sorted(df["company"].unique())
    carmodels = sorted(df["name"].unique())
    year = sorted(df["year"].unique(),reverse=True)
    fuel_type = sorted(df["fuel_type"].unique())    
    return render_template('index.html',companies=companies,carmodels=carmodels,years=year,fuel_type=fuel_type)

@app.route("/predict",methods = ["POST"])
def predict():
    company = request.form.get("company")
    carmodel = request.form.get("model") 
    year = int(request.form.get("year"))
    fuel_type = request.form.get("fuel")
    kms_driven = int(request.form.get("number"))
    print(company,carmodel,year,fuel_type,kms_driven)
    prediction = model.predict(pd.DataFrame([[carmodel,company,year,kms_driven,fuel_type]],columns=["name","company","year","kms_driven","fuel_type"]))
    newpredict = round(prediction[0])
    return str(newpredict)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
