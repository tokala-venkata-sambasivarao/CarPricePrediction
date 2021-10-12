# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 17:19:31 2021

@author: SAMBA
"""


from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('C:\\Users\\SAMBA\\Desktop\\Internship DS\\best_model.pkl', 'rb'))

@app.route("/")

def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    int_features
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('home.html', prediction_text=' Car Price should be $ {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
