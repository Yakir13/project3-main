from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/addition", methods=["POST"])
def addition():
    data = request.get_json()
    result = data["num1"] + data["num2"]
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
