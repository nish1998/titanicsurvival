#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 14:50:12 2018

@author: nishant
"""
#from __future__ import print_function # In python 2.7
from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle
import os

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            X = [[(data["x"]), (data["y"]), (data["z"]), (data["l"]), (data["m"]), (data["n"]), (data["o"]) ]]
            X=np.asarray(X)
            loaded_model = pickle.load(open('finalized_model.sav', "rb"))
        except ValueError:
            return jsonify(X.tolist())

        return jsonify(loaded_model.predict(X).tolist())
@app.route('/')
def index():
    return "ok"

if __name__ == '__main__':
    app.run()
