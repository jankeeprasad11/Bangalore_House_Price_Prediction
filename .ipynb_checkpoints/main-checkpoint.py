# flask, scikit-learn, pandas, pickle-mixin, flask-cors

import pandas as pd
import numpy as np
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
data = pd.read_csv("D:\Programing Practices\Machine Learning\Projects\Bengaluru_House_Price_Prediction\cleaned_data.csv")
pipe = pickle.load(open("D:\Programing Practices\Machine Learning\Projects\Bengaluru_House_Price_Prediction\RidgeModel.pkl",'rb'))


@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict',methods=['POST'])
def predict():

    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')
    
    # print(location, bhk, bath, sqft);

    input = pd.DataFrame([[location, sqft, bath, bhk]], columns=['location', 'sqft', 'bath', 'bhk'])
    prediction = pipe.predict(input)[0] * 1e5

    return str(np.round(prediction,2))

if __name__=="__main__":
    app.run(debug=True, port=5001)