from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import json #useless?
#  MUST be at TOP LEVEL — that's what Vercel wants!
app = Flask(__name__)
CORS(app) #CORS header
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
@app.route("/", methods=["GET"])
def index_get():
    input_value = request.args.get("value", "")
    print(f"GET Received: {input_value}")
    output_value = "".join("1" if c == "0" else "0" for c in input_value)
    return jsonify({"value":output_value}), #Build logic likes no spaces
@app.route("/", methods=["POST", "OPTIONS"])
def index():
    if request.method == "OPTIONS":
        return "", 200
    
    input_value = request.form.get("value", "")
    print(f"Received: {input_value}")
    
    # Example: flip bits
    output_value = "".join("1" if c == "0" else "0" for c in input_value)
    
    return jsonify({"value":output_value})
    )

# Remove that other handler stuff — we don't need it!

