from flask import jsonify, request, Blueprint


from controllers.candidates import CandidatesController
from models.party import PartyDoesNotExist
from models.candidates import CandidateDoesNotExist

candidates_controller = CandidatesController()

candidates_bp = Blueprint("candidates_bp", __name__)


@candidates_bp.route("/", methods=["GET"])
def get_all():

    return jsonify({
        "candidates": [item.to_json() for item in candidates_controller.get_all()]
    })


@candidates_bp.route("/<string:id_candidate>", methods=["GET"])
def get_by_id(id_candidate):
    try:
        candidate = candidates_controller.get_by_id(id_candidate)
    except CandidateDoesNotExist:
        return jsonify({
            "error": "El candidato no existe"
        }), 404
    else:
        return jsonify(candidate.__dict__)


@candidates_bp.route("/", methods=["POST"])
def create():
    body = request.get_json()
    candidate = candidates_controller.create(body)
    return jsonify({
        "candidate": candidate.to_json()
    })


@candidates_bp.route("/<string:id_candidate>", methods=["PUT"])
def update(id_candidate):
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
def delete(id_candidate):
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
