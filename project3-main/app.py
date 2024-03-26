from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/addition", methods=["POST"])
def addition():
    data = request.get_json()
    result = data["num1"] + data["num2"]
    return jsonify({"result": result})


@app.route("/subtraction", methods=["POST"])
def subtraction():
    data = request.get_json()
    result = data["num1"] - data["num2"]
    return jsonify({"result": result})


@app.route("/multiplication", methods=["POST"])
def multiplication():
    data = request.get_json()
    result = data["num1"] * data["num2"]
    return jsonify({"result": result})


@app.route("/division", methods=["POST"])
def division():
    data = request.get_json()
    if data["num2"] == 0:
        return jsonify({"ERROR"}), 404
    result = data["num1"] / data["num2"]
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
