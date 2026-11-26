from flask import Blueprint, current_app, jsonify

from ..db import connect, execute


def delete_student_blueprint():
    blueprint = Blueprint("delete_student", __name__)

    @blueprint.route("/students/<int:student_id>", methods=["DELETE"])
    def delete_student(student_id):
        connection = connect(current_app.config["DATABASE_URL"])
        try:
            cursor = execute(
                connection,
                "DELETE FROM students WHERE id = %s",
                (student_id,),
            )
            connection.commit()
        finally:
            connection.close()

        if cursor.rowcount == 0:
            return jsonify({"error": "Student not found."}), 404
        return "", 204

    return blueprint
