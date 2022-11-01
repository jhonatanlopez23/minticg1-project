from flask import Flask, jsonify
from views.party import party_bp
from views.candidate import candidates_bp
from views.tables import tables_bp
from views.results import results_bp


app = Flask(__name__)


@app.route("/", methods=["GET"])
def ping():
    return jsonify({
        "message": "Server Runing..."
    })


app.register_blueprint(party_bp, url_prefix="/party")
app.register_blueprint(candidates_bp, url_prefix="/candidate")
app.register_blueprint(tables_bp, url_prefix="/table")
app.register_blueprint(results_bp, url_prefix="/result")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
