from flask import jsonify, request, Blueprint

from controllers.candidate import candidatesController
from models.candidate import CandidateDoesNotExist

candidates_controller = candidatesController()

candidates_bp = Blueprint("candidates_blueprint", __name__)


@candidates_bp.route("/", methods=["GET"])
def candidates():
    list_candidates = []
    for candidate in candidates_controller.get_all():
        list_candidates.append(candidate.__dict__)
    return jsonify({
        "candidates": list_candidates,
        "count": candidates_controller.count()
    })


@candidates_bp.route("/<string:id_candidate>", methods=["GET"])
def get_candidate_by_id(id_candidate):
    try:
        candidate = candidates_controller.get_by_id(id_candidate)
    except CandidateDoesNotExist:
        return jsonify({
            "error": "El candidato no existe"
        }), 404
    else:
        return jsonify(candidate.__dict__)


@candidates_bp.route("/", methods=["POST"])
def create_candidate():
    candidate = candidates_controller.create(request.get_json())
    return jsonify({
        "message": "candidato fue creado de forma exitosa",
        "candidate": candidate.__dict__
    }), 201


@candidates_bp.route("/<string:id_candidate>", methods=["PUT"])
def update_candidate(id_candidate):
    try:
        candidate = candidates_controller.update(
            id_candidate,
            request.get_json()
        )
    except CandidateDoesNotExist:
        return jsonify({
            "error": "error"
        }), 404
    else:
        return jsonify({
            "candidate": candidate.__dict__
        })


@candidates_bp.route("/<string:id_candidate>", methods=["DELETE"])
def delete_candidate(id_candidate):
    try:
        result = candidates_controller.delete(id_candidate)
    except CandidateDoesNotExist:
        return jsonify({
            "error": "error"
        }), 404
    else:
        return jsonify({
            "message": "el candidato fue borrado",
            "result": result
        }), 200