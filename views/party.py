from flask import jsonify, request, Blueprint

from controllers.party import PartyController
from models.party import PartyDoesNotExist

party_controller = PartyController()

party_bp = Blueprint("party_blueprint", __name__)



@party_bp.route("/", methods=["GET"])
def party():
    list_party = []
    for party in party_controller.get_all():
        list_party.append(party.__dict__)
    return jsonify({
        "party": list_party,
        "count": party_controller.count()
    })


@party_bp.route("/<string:id_party>", methods=["GET"])
def get_party_by_id(id_party):
    try:
        party = party_controller.get_by_id(id_party)
    except PartyDoesNotExist:
        return jsonify({
            "error": "El partido no existe"
        }), 404
    else:
        return jsonify(party.__dict__)


@party_bp.route("/", methods=["POST"])
def create_party():
    party = party_controller.create(request.get_json())
    return jsonify({
        "message": "partido creado correctamente",
        "party": party.__dict__
    }), 201


@party_bp.route("/<string:id_party>", methods=["PUT"])
def update_party(id_party):
    try:
        party = party_controller.update(
            id_party,
            request.get_json()
        )
    except PartyDoesNotExist:
        return jsonify({
            "error": "error"
        }), 404
    else:
        return jsonify({
            "party": party.__dict__
        })


@party_bp.route("/<string:id_party>", methods=["DELETE"])
def delete_party(id_party):
    try:
        result = party_controller.delete(id_party)
    except PartyDoesNotExist:
        return jsonify({
            "error": "error"
        }), 404
    else:
        return jsonify({
            "message": "El partido fue eliminado",
            "result": result
        }), 200