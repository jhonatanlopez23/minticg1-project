from flask import Flask, jsonify, request, Blueprint


from controllers.tables import TablesController, TableDoesNotExist

tables_controller = TablesController()

tables_bp = Blueprint("tables_blueprint", __name__)


@tables_bp.route("/", methods=["GET"])
def tables():
    list_tables = []
    for tables in tables_controller.get_all():
        list_tables.append(tables.__dict__)
    return jsonify({
        "tables": list_tables,
        "count": tables_controller.count()
    })


@tables_bp.route("/<string:id_table>", methods=["GET"])
def get_tables_by_id(id_table):
    try:
        table = tables_controller.get_by_id(id_table)
    except TableDoesNotExist:
        return jsonify({
            "error": "La mesa no existe"
        })
    else:
        return jsonify(table.__dict__)


@tables_bp.route("/", methods=["POST"])
def create_table():
    table = tables_controller.create(request.get_json())
    return jsonify({
        "menssage": " Mesa fue creada de forma exitosa",
        "table": table.__dict__
    }), 201


@tables_bp.route("/<string:id_table>", methods=["PUT"])
def update_table(id_table):
    try:
        table = tables_controller.update(
            id_table,
            request.get_json()
        )
    except TableDoesNotExist:
        return jsonify({
            "error": "error"
        }), 404
    else:
        return jsonify({
            "table": table.__dict__
        })


@tables_bp.route("/<string:id_table>", methods=["DELETE"])
def delete_table(id_table):
    try:
        result = tables_controller.delete(id_table)
    except TableDoesNotExist:
        return jsonify({
            "error": "error"
        }), 404
    else:
        return jsonify({
            "message": "la mesa fue borrada",
            "result": result
        }), 200
