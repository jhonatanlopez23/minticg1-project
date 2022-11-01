from flask import jsonify, Blueprint, request

from controllers.results import ResultsController
from models.results import Results, ResultsDoesNotExist
from models.tables import Tables, TableDoesNotExist
from models.candidates import Candidate, CandidateDoesNotExist

results_bp = Blueprint("results_bp", __name__)
result_controller = ResultsController()


@results_bp.route("/", methods=["GET"])
def get_all():
    return jsonify({
        "results": [item.to_json() for item in result_controller.get_all()]
    })


@results_bp.route("/", methods=["POST"])
def create():
    try:
        results = result_controller.create(request.get_json())
        return jsonify(results.to_json())
    except TableDoesNotExist:
        return jsonify({
            "message": f"la mesa no existe"
        }), 400
    except CandidateDoesNotExist:
        return jsonify({
            "message": f"El candidato no existe"
        }), 400


@results_bp.route("/<string:id_result>", methods=["GET"])
def get_by_id(id_result):
    try:
        result = result_controller.get_by_id(id_result)
        return jsonify(result.to_json())
    except ResultsDoesNotExist:
        return jsonify({
            "message": "El resultado no existe"
        }), 404


@results_bp.route("/<string:id_result>", methods=["PUT"])
def update(id_result):
    try:
        results = result_controller.update(
            id_result, request.get_json())
        return jsonify(results.to_json())
    except TableDoesNotExist:
        return jsonify({
            "message": f"la mesa no existe"
        }), 400
    except CandidateDoesNotExist:
        return jsonify({
            "message": f"el candidato no existe"
        }), 400


@results_bp.route("/<string:id_result>", methods=["DELETE"])
def delete(id_result):
    try:
        return jsonify(result_controller.delete(id_result))
    except ResultsDoesNotExist:
        return jsonify({
            "message": "resultado no existe"
        })
    
