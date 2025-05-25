from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional, List

app = FastAPI()

# ----- MODELOS PARA LA API -----

class Cliente(BaseModel):
    id: int
    nombre: str

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None

class RegistroEntradaModel(BaseModel):
    id_registro: int
    id_cliente: int
    fecha_hora_entrada: Optional[datetime] = None

# ----- DATOS SIMULADOS -----
clientes = []
registros = []

# ----- RUTAS -----

@app.get("/clientes")
def obtener_clientes():
    return clientes

@app.post("/clientes")
def crear_cliente(cliente: Cliente):
    clientes.append(cliente)
    return {"mensaje": "Cliente creado correctamente"}

@app.put("/clientes/{id_cliente}")
def actualizar_cliente(id_cliente: int, datos: ClienteUpdate):
    for c in clientes:
        if c.id == id_cliente:
            if datos.nombre:
                c.nombre = datos.nombre
            return {"mensaje": "Cliente actualizado"}
    return {"error": "Cliente no encontrado"}

@app.delete("/clientes/{id_cliente}")
def eliminar_cliente(id_cliente: int):
    global clientes
    clientes = [c for c in clientes if c.id != id_cliente]
    return {"mensaje": "Cliente eliminado"}

@app.post("/entrada")
def registrar_entrada(entrada: RegistroEntradaModel):
    hora = entrada.fecha_hora_entrada or datetime.now()
    if hora.time() < datetime.strptime("06:00", "%H:%M").time() or hora.time() > datetime.strptime("22:00", "%H:%M").time():
        return {"estado": "Denegado", "mensaje": "Fuera del horario permitido"}
    registros.append(entrada)
    return {"estado": "Permitido", "mensaje": "Entrada registrada"}
