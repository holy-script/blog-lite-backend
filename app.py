from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
cors = CORS(app, supports_credentials=True,
            origins=os.environ.get("FRONTEND_URL"))
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/", methods=["GET"])
@cross_origin()
def helloworld():
    if request.method == "GET":
        data = {"data": "Hello from Flask!"}
        return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
