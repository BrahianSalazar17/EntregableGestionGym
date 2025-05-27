from datetime import date
from persona import Persona

class Cliente(Persona):
    def __init__(self, id_persona, nombre, correo, telefono, direccion, fechaRegistro=None, estado="", membresia=""):
        super().__init__(id_persona, nombre, correo, telefono, direccion)
        self.fechaRegistro = fechaRegistro if fechaRegistro else date.today()
        self.estado = estado
        self.membresia = membresia

    def registrarCliente(self, datosCliente: dict) -> bool:
        try:
            super().actualizarDatos(datosCliente)
            self.fechaRegistro = datosCliente.get('fechaRegistro', date.today())
            self.estado = datosCliente.get('estado', "Activo")
            self.membresia = datosCliente.get('membresia', "")
            return True
        except Exception as e:
            print(f"Error al registrar cliente: {e}")
            return False

    def consultarEstadoMembresia(self) -> str:
        return self.estado
