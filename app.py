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
    return jsonify({"message": "Welcome to the home page"})

@app.route("/Predict", methods=["GET", "POST"])
def get_prediction():
    content = pd.DataFrame(request.json, index=[0])
    result = {} 
    user_data = getdiscretization(content, 'age', bins = file_paths['bins'])
    model = load_model(file_paths['model_path'])
    prediction = model.predict(user_data) 
    print(prediction)

    if prediction[0] == 1:
        result['msg'] = 'have heart problem '
    else:
        result['msg'] = 'doesnot have heart problem '

    return jsonify(result)


def handler(event, context):
    # return app.run(host='', port=8080)
    print(event)
    content = pd.DataFrame(json.loads(event['body']), index=[0])
    result = {} 
    user_data = getdiscretization(content, 'age', bins = file_paths['bins'])
    model = load_model(file_paths['model_path'])
    prediction = model.predict(user_data) 
    print(prediction)

    if prediction[0] == 1:
        result['msg'] = 'have heart problem '
    else:
        result['msg'] = 'doesnot have heart problem '

    resp = {
        "statusCode": 200,
        "body": json.dumps({"message": result['msg']}),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        }
    }
    return resp

if __name__ == '__main__':
    app.run(port=5000, debug=True)



