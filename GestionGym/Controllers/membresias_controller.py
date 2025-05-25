from datetime import date

class MembresiaController:

    def activarMembresia(self, idCliente: int, fechaInicio: date, fechaFin: date) -> bool:
        print(f"Activando membresía para cliente {idCliente} desde {fechaInicio} hasta {fechaFin}")
        return True

    def verificarVencimientoMembresia(self, idCliente: int, fechaActual: date) -> bool:
        print(f"Verificando vencimiento de membresía para cliente {idCliente} en fecha {fechaActual}")
        return False

    def renovarMembresia(self, idCliente: int, nuevaFechaFin: date) -> bool:
        print(f"Renovando membresía para cliente {idCliente} hasta {nuevaFechaFin}")
        return True

    def asociarPagoAMembresia(self, idPago: int, idMembresia: int) -> bool:
        print(f"Asociando pago {idPago} a membresía {idMembresia}")
        return True
