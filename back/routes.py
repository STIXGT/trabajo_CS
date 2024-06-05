# routes.py
from flask import request, jsonify

def init_routes(app, mysql):

    @app.route('/clientes', methods=['GET'])
    def get_clientes():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Clientes")
        data = cur.fetchall()
        cur.close()
        return jsonify(data)

    @app.route('/clientes/<int:id>', methods=['GET'])
    def get_cliente(id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Clientes WHERE id = %s", (id,))
        data = cur.fetchone()
        cur.close()
        if data:
            return jsonify(data)
        return jsonify({'message': 'Cliente no encontrado'}), 404

    @app.route('/clientes', methods=['POST'])
    def create_cliente():
        data = request.json
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Clientes (nombre, email, telefono) VALUES (%s, %s, %s)",
                    (data['nombre'], data['email'], data['telefono']))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Cliente creado'}), 201

    @app.route('/clientes/<int:id>', methods=['PUT'])
    def update_cliente(id):
        data = request.json
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Clientes SET nombre = %s, email = %s, telefono = %s WHERE id = %s",
                    (data['nombre'], data['email'], data['telefono'], id))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Cliente actualizado'})

    @app.route('/clientes/<int:id>', methods=['DELETE'])
    def delete_cliente(id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Clientes WHERE id = %s", (id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'Cliente eliminado'})

    # Similarmente, puedes añadir rutas para Habitaciones y Reservas

    @app.route('/habitaciones', methods=['GET'])
    def get_habitaciones():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Habitaciones")
        data = cur.fetchall()
        cur.close()
        return jsonify(data)

    @app.route('/reservas', methods=['GET'])
    def get_reservas():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Reservas")
        data = cur.fetchall()
        cur.close()
        return jsonify(data)

    # Añadir rutas para crear, actualizar y eliminar Habitaciones y Reservas de manera similar
