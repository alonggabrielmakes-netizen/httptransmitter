from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route("/", methods=["GET"])
def index_get():
    input_value = request.args.get("value", "")
    print(f"GET Received: {input_value}")
    output_value = "".join("1" if c == "0" else "0" for c in input_value)
    resp = jsonify({"value": output_value})
    resp.headers["Content-Type"] = "application/json"
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp
@app.route("/", methods=["POST", "OPTIONS"])
def index():
    if request.method == "OPTIONS":
      resp = make_response("", 200)
      resp.headers["Access-Control-Allow-Origin"] = "*"
      resp.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
      resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
      return resp
    input_value = request.form.get("value", "")
    print(f"Received: {input_value}")
    output_value = "".join("1" if c == "0" else "0" for c in input_value)
    return jsonify({"value": output_value})
    
