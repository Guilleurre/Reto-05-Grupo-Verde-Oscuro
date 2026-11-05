# Reto-05-Grupo-Verde-Oscuro

## 1. Descripción del proyecto

Este proyecto consiste en la preparación de datos de préstamos y el desarrollo de un modelo de impago y un modelo de prima utilizando **Python**.

El trabajo está organizado en tres notebooks. Estos archivos permiten separar la preparación de los datos del desarrollo de los modelos y consultar los resultados durante la ejecución.

## 2. Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Jupyter Notebook:** apertura y ejecución de archivos `.ipynb`.
- **Visual Studio Code:** edición y ejecución de los notebooks mediante las extensiones de Python y Jupyter.

Además, es necesario instalar las librerías que se importan en cada notebook.

## 3. Notebooks disponibles

### 3.1. Preparación de los datos

Archivo: `dataframe filtrado sin nulos sin duplicados y categorizado(3).ipynb`

Notebook dedicado al filtrado de los datos, el tratamiento de valores nulos, la eliminación de duplicados y la categorización de variables.

Se propone comenzar por este archivo para revisar la preparación del conjunto de datos antes de trabajar con los modelos.

### 3.2. Modelo de impago

Archivo: `Modelo_impago.ipynb`

Notebook dedicado al desarrollo del modelo de impago de los préstamos.

Para utilizarlo, es necesario disponer del archivo de datos que carga el código. Sus celdas deben ejecutarse en orden para consultar los resultados obtenidos.

### 3.3. Modelo de prima

Archivo: `Modelo_Prima.ipynb`

Notebook dedicado al desarrollo del modelo de prima.

Antes de ejecutarlo, es necesario comprobar qué datos carga y si utiliza algún resultado generado por el modelo de impago.

### 3.3. Docker Reto 5 alumnos
En docker Reto 5 alumnos se encuentra lo utilizado para realizar una API con los datos, dentro de ella se encuentr otro readme que profundiza mas su contenido

## 4. Archivos de datos

Los notebooks necesitan acceder a los archivos indicados en las instrucciones de lectura del código.

Antes de comenzar, comprobar:

- Que los archivos necesarios están disponibles.
- Que sus nombres coinciden con los utilizados en el código.
- Que las rutas corresponden a su ubicación en el ordenador.
- Que las carpetas de destino existen si el código guarda resultados.

Si el trabajo se ejecuta desde otro ordenador, puede ser necesario modificar estas rutas.

## 5. Ejecución del proyecto

Para ejecutar el trabajo en Visual Studio Code:

1. Instalar Python y las extensiones **Python** y **Jupyter**.
2. Abrir la carpeta del proyecto.
3. Abrir el notebook de preparación de datos.
4. Pulsar **Seleccionar kernel** y elegir el entorno de Python.
5. Ejecutar las celdas de arriba abajo o pulsar **Ejecutar todo**.
6. Continuar con los notebooks de los modelos, comprobando los archivos que necesita cada uno.

El orden entre el modelo de impago y el modelo de prima está pendiente de confirmar revisando sus dependencias.

## 6. Comprobación de los resultados

Los resultados aparecen debajo de las celdas ejecutadas.

Para comprobar la ejecución:

- Revisar que todas las celdas terminan sin errores.
- Comprobar que los datos se cargan correctamente.
- Consultar las salidas generadas por cada notebook.
- Verificar los archivos exportados, si el código los guarda.

Para repetir el proceso completo, reiniciar el kernel y ejecutar todas las celdas desde el principio.
