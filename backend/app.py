
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Backend is running"})

@app.route("https://simplefullstack.onrender.com//message", methods=["POST"])
def message():
    data = request.get_json(silent=True) or {}
    name = data.get("name", "Guest")

    return jsonify({
        "message": f"Hello {name}! Backend connected successfully."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
