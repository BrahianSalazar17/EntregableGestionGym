from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos simulada con usuarios ya creados
usuarios = {
    1: {
        "Id_persona": 1,
        "Nombre": "Ana Torres",
        "Correo": "ana.torres@email.com",
        "Telefono": "3111234567",
        "Direccion": "Calle 123 #45-67"
    },
    2: {
        "Id_persona": 2,
        "Nombre": "Luis Gómez",
        "Correo": "luis.gomez@email.com",
        "Telefono": "3109876543",
        "Direccion": "Cra 10 #20-30"
    },
    3: {
        "Id_persona": 3,
        "Nombre": "Marta Ruiz",
        "Correo": "marta.ruiz@email.com",
        "Telefono": "3001112233",
        "Direccion": "Av. Siempre Viva 742"
    }
}

# Obtener todos o uno por ID
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    id_persona = request.args.get('id', type=int)
    if id_persona:
        usuario = usuarios.get(id_persona)
        if usuario:
            return jsonify(usuario)
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(list(usuarios.values()))

# Crear nuevo usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    nuevo_id = max(usuarios.keys()) + 1
    datos["Id_persona"] = nuevo_id
    usuarios[nuevo_id] = datos
    return jsonify({"resultado": True, "usuario": datos}), 201

# Actualizar usuario
@app.route('/usuarios/<int:id_persona>', methods=['PUT'])
def actualizar_usuario(id_persona):
    if id_persona in usuarios:
        datos_actualizados = request.get_json()
        usuarios[id_persona].update(datos_actualizados)
        return jsonify({"resultado": True, "usuario": usuarios[id_persona]})
    return jsonify({"resultado": False, "error": "Usuario no encontrado"}), 404

# Eliminar usuario
@app.route('/usuarios/<int:id_persona>', methods=['DELETE'])
def eliminar_usuario(id_persona):
    if id_persona in usuarios:
        del usuarios[id_persona]
        return jsonify({"resultado": True})
    return jsonify({"resultado": False, "error": "Usuario no encontrado"}), 404

@app.route('/')
def inicio():
    return "API de Usuarios Activa"

if __name__ == '__main__':
    app.run(debug=True)

