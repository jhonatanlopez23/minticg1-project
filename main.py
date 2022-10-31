from flask import Flask, jsonify
from views.party import party_bp


app = Flask(__name__)


@app.route("/", methods=["GET"])
def ping():
    return jsonify({
        "message": "Server Runing..."
    })


app.register_blueprint(party_bp, url_prefix="/party")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
