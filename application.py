from flask import Flask, request,jsonify,render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd

##working on flask

application = Flask(__name__)
app = application

#import lasso regression and standard scaler pickle
lasso_model = pickle.load(open("models/lasso_model.pk1"),'rb')
scaler_model = pickle.load(open("models/scaler_lasso_model.pk1"),'rb')

#creating homepage
@app.route('/')
def index():
    return render_template('index.html')



if __name__=="__main__":
    app.run(host="0.0.0.0")