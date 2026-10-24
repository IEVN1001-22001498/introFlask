
from flask import Blueprint, jsonify
from database import mysql

alumnos_bp = Blueprint(
    'maestros',
    __name__,
    url_prefix='/api/maestros'
)

@alumnos_bp.route('', methods=['GET'])
def lista_maestros():
    cursor = None

    try:
        cursor = mysql.connection.cursor()
        cursor.execute("""SELECT * FROM maestros""")

        datos = cursor.fetchall()
        maestros = [
            fila_a_diccionario(cursor, fila)
            for fila in datos
        ] 

        return jsonify({
            'maestros': maestros,
            'mensaje' : 'Lista de maestros',
            'exito': True
        }), 200

    except Exception:
        return jsonify({
            'mensaje': 'Error al consultar los maestros',
            'exito': False
        }), 500

    finally:
        if cursor is not None:
            cursor.close()
