from flask import Flask, request, jsonify
 from flask_cors import CORS
 app = Flask(__name__)
 CORS(app)  # allow Build Logic to talk to us
 @app.route("/", methods=["POST", "OPTIONS"])
 def handle_request():
     # Handle preflight
     if request.method == "OPTIONS":
         return "", 200
     
     # Get what the transmitter sent
     data = request.json
     input_value = data.get("value", "")
     print(f"Received: {input_value}")
     
     # logic here example: flip bits
     output_value = "".join("1" if c == "0" else "0" for c in input_value)
     
     # Send back JSON — exactly what the transmitter expects!
     return jsonify({"value": output_value}), 200
 # Vercel Python handler
 from vercel_python import make_wsgi_app
 app = make_wsgi_app(app)
