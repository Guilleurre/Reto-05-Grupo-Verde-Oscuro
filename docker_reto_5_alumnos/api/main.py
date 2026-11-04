from flask import Flask
from sqlalchemy import create_engine, text
import requests
import os


app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL,pool_pre_ping=True)


@app.get("/")
def root():
    return {
        "mensaje": "API Flask funcionando"
    }

@app.get("/prestamos")
def listar_prestamos():
    with engine.connect() as conexion:
        resultado = conexion.execute(
            text("SELECT * FROM clientes_credito")
        )
        prestamos = [dict(fila) for fila in resultado.mappings()]

    return {"prestamos": prestamos}



@app.get("/prestamos/<int:id>")
def buscar_prestamo(id):
    with engine.connect() as conexion:
        resultado = conexion.execute(
            text("SELECT * FROM clientes_credito WHERE id = :id"),
            {"id": id}
        )
        prestamo = resultado.mappings().first()

    if prestamo is None:
        return {"error": "Préstamo no encontrado"}, 404

    return {"prestamo": dict(prestamo)}



@app.get("/estadisticas")
def obtener_estadisticas():

    with engine.connect() as conexion:
        resultado = conexion.execute(text("""
            SELECT
                COUNT(*) AS total_prestamos,
                AVG(edad) AS edad_media,
                AVG(ingresos) AS ingresos_medios
            FROM clientes_credito
        """))

        estadisticas = resultado.mappings().first()

    return {"estadisticas": dict(estadisticas)}, 200


@app.get("/prestamos/ingresos")
def ordenar_ingresos():

    with engine.connect() as conexion:
        resultado = conexion.execute(text("""
            SELECT *
            FROM clientes_credito
            ORDER BY ingresos DESC
        """))

        prestamos = [dict(fila) for fila in resultado.mappings()]

    return {"prestamos": prestamos}, 200



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )