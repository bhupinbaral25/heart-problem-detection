import pickle
import yaml
import json
import numpy as np
import requests
import pandas as pd
from src.utils import getdiscretization
from flask import Flask, render_template, request, redirect, url_for, jsonify


with open("config.yaml", "r") as config:
    file_paths = yaml.safe_load(config)


def read_json()-> pd.DataFrame:

    json_file = open('user_data.json', 'r')

    return pd.DataFrame(json.loads(json_file.read()), index=[0])


def load_model(model_path: str):
    """Loads and returns the model from the project directory.
    Args:
        model_path: Path of the model
    Returns:
        model. A linear_model loaded from the directory.
    """
    try:
        return pickle.load(open(model_path, "rb"))
    except pickle.UnpicklingError as e:
        raise f"Unpickling Error: {e}"
    except Exception as e:
        raise e

#API Creating Using flask
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
        
    return render_template("index.html")

@app.route("/Predict", methods=["GET", "POST"])
def get_prediction():

    result = {} 
    user_data = getdiscretization(read_json(), 'age', bins = file_paths['bins'])
    model = load_model(file_paths['model_path'])
    prediction = model.predict(user_data) 

    if prediction[0] == 1:
        result['msg'] = 'have heart problem '
    else:
        result['msg'] = 'doesnot have heart problem '

    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

