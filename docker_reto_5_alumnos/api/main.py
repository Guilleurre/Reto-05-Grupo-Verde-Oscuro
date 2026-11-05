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
            text("""
            SELECT *
            FROM clientes_credito
            LIMIT 1000
        """)
        )
        prestamos = [dict(fila) for fila in resultado.mappings()]

    return {"prestamos": prestamos}


@app.get("/prestamos/vivienda")
def prestamos_vivienda():
    with engine.connect() as conexion:
        resultado = conexion.execute(text("""
            SELECT *
            FROM clientes_credito
            WHERE proposito = 'Vivienda'
            LIMIT 1000
        """))

        prestamos = [dict(fila) for fila in resultado.mappings()]

    return {"prestamos": prestamos}, 200



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

@app.get("/prestamos/ingresos")
def ordenar_ingresos():

    with engine.connect() as conexion:
        resultado = conexion.execute(text("""
            SELECT *
            FROM clientes_credito
            ORDER BY ingresos DESC
            LIMIT 1000
        """))

        prestamos = [dict(fila) for fila in resultado.mappings()]

    return {"prestamos": prestamos}, 200

@app.get("/prestamos/impago")
def prestamos_impago():
    with engine.connect() as conexion:
        resultado = conexion.execute(text("""
            SELECT *
            FROM clientes_credito
            WHERE impago = 1
            LIMIT 1000
        """))

        prestamos = [dict(fila) for fila in resultado.mappings()]

    return {"prestamos": prestamos}, 200


@app.get("/prestamos/pago")
def prestamos_pago():
    with engine.connect() as conexion:
        resultado = conexion.execute(text("""
            SELECT *
            FROM clientes_credito
            WHERE impago = 0
            LIMIT 1000
        """))

        prestamos = [dict(fila) for fila in resultado.mappings()]

    return {"prestamos": prestamos}, 200

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


#para la consulta con una api externa he elegido una que te dice la ciudad sabiendo el codigo postal

@app.get("/codigo_postal/<codigo>")
def codigo_postal(codigo):

    respuesta = requests.get(
        f"https://api.zippopotam.us/es/{codigo}"
    )

    if respuesta.status_code != 200:
        return {"error": "Código postal no encontrado"}, 404

    return respuesta.json(), 200





if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )