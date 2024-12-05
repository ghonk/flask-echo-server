from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

@app.route('/strlen', methods=['POST'])
def strlen():
    data = request.get_json()
    if "string" not in data:
        return jsonify({"error": "Missing 'string' key"}), 400
    return jsonify({"length": len(data["string"])})


if __name__ == "__main__":
    app.run(debug=True)

