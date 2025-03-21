import json

from flask import Flask, jsonify, request
from db.db import DB

app = Flask(__name__)
db = DB()

def setup():
    db.create_table()

@app.route("/")
def intro():
    return "Flask website with PostgreSQL connection"

@app.route("/customers")
def get_all():
    try:
        customer = db.get_all_customers()
        return json.dumps(customer), 200
    except Exception as e:
        return jsonify({"error": f"Error getting customer: {e}"}), 500


@app.route("/customers/add", methods=['POST'])
def add_customer():
    try:
        body = json.loads(request.data)
        if body:
            db.create_customer(body['name'], body['email'])
            return "OK", 200
        raise Exception("Unable to add")
        
    except Exception as e:
        return jsonify({"error": f"Error adding customer: {e}"}), 500

if __name__ == "__main__":
    setup()
    app.run(debug=True)