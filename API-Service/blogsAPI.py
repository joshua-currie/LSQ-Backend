from flask import Flask, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)

CORS(app)

DATA_PATH = os.path.join(os.path.dirname(__file__), '../Angular-Component-Data')

@app.route('/data/blogs', methods=['GET'])
def get_data():
    component_name = 'blogs'
    try:
        with open(os.path.join(DATA_PATH, f'{component_name}.json'), 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Data not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
