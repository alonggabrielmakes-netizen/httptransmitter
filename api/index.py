from flask import Flask, request, Response
from flask_cors import CORS
import json
#  MUST be at TOP LEVEL — that's what Vercel wants!
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST", "OPTIONS"])
def index():
    if request.method == "OPTIONS":
        return "", 200
    
    data = {}
    raw_text = request.get_data(as_text=True)
    if raw_text:
        try:
            data = json.loads(raw_text)
        except json.JSONDecodeError:
            print("Invalid JSON received")
    input_value = data.get("value", "")
    print(f"Received: {input_value}")
    
    # Example: flip bits
    output_value = "".join("1" if c == "0" else "0" for c in input_value)
    
    return Response(
        json.dumps({"value": output_value}),
        status=200,
        mimetype="application/json"
    )

# Remove that other handler stuff — we don't need it!

