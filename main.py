from flask import Flask, jsonify, request
import random, string

app = Flask(__name__)

issued_keys = set()
used_keys = set()

def generate_key(length=12):
    while True:
        key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if key not in issued_keys:
            issued_keys.add(key)
            return key

@app.route("/getKey")
def get_key():
    key = generate_key()
    return jsonify({"key": key})

@app.route("/validateKey")
def validate_key():
    key = request.args.get("key")
    if key in issued_keys and key not in used_keys:
        used_keys.add(key)
        return jsonify({"valid": True})
    return jsonify({"valid": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
