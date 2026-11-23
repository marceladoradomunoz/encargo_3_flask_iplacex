
############################################################
# Nombre:       Marcela Muñoz Dorado
# Institución:  IPLACEX
# Asignatura:   Programación Web
# Evaluación:   Encargo N.º 3 - Unidad III
# Fecha:        20-11-2026
############################################################

"""
Aplicación web desarrollada con Python y Flask.

Ejercicio 1:
Calcula el promedio de tres notas y determina el estado
de aprobación considerando el promedio y la asistencia.

Ejercicio 2:
Compara tres nombres diferentes e identifica aquel que
contiene la mayor cantidad de letras.

Incluye validación de entradas, manejo de errores y
procesamiento de formularios mediante solicitudes HTTP.
"""

import math
import re
import unicodedata

from flask import Flask, render_template, request


# Inicialización de la aplicación Flask.
app = Flask(__name__)


def convertir_numero(valor):
    """
    Valida y convierte una entrada a número decimal.

    Args:
        valor (str): Dato recibido desde el formulario.

    Returns:
        float | None: Número válido o None si la entrada
        contiene caracteres no permitidos o no es finita.
    """

    texto = (valor or "").strip()

    # Solo admite dígitos y un punto decimal opcional.
    if not re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", texto):
        return None

    try:
        numero = float(texto)

        # Evita valores infinitos o no finitos.
        if not math.isfinite(numero):
            return None

        return numero

    except (ValueError, OverflowError):
        return None


def normalizar_nombre(nombre):
    """
    Normaliza los espacios y caracteres de un nombre.

    Args:
        nombre (str): Nombre ingresado por el usuario.

    Returns:
        str: Nombre normalizado, conservando mayúsculas,
        minúsculas y letras acentuadas.
    """

    nombre = " ".join((nombre or "").split())

    return unicodedata.normalize("NFC", nombre)


def validar_nombre(nombre):
    """
    Verifica que un nombre contenga únicamente letras
    del alfabeto español y espacios internos.

    Args:
        nombre (str): Nombre normalizado.

    Returns:
        bool: True si es válido; False en caso contrario.
    """

    patron = (
        r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+"
        r"(?: [A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+)*"
    )

    return re.fullmatch(patron, nombre) is not None


@app.route("/")
def inicio():
    """
    Renderiza la página principal de la aplicación.

    Returns:
        str: Página HTML con los accesos a los ejercicios.
    """

    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    """
    Procesa el formulario de notas y asistencia.

    Valida que las tres notas estén entre 10 y 70
    y que la asistencia esté entre 0 y 100.

    Para aprobar, el promedio debe ser mayor o igual
    a 40 y la asistencia mayor o igual al 75 %.

    Returns:
        str: Formulario HTML con resultados o errores.
    """

    if request.method == "POST":

        # Recepción y validación de las notas.
        nota1 = convertir_numero(request.form.get("nota1"))
        nota2 = convertir_numero(request.form.get("nota2"))
        nota3 = convertir_numero(request.form.get("nota3"))

        # Recepción y validación de la asistencia.
        asistencia = convertir_numero(
            request.form.get("asistencia")
        )

        valores = [nota1, nota2, nota3, asistencia]

        # Control de entradas no numéricas o incompletas.
        if any(valor is None for valor in valores):
            return render_template(
                "ejercicio1.html",
                error=(
                    "Ingrese únicamente valores numéricos válidos "
                    "en todos los campos. Puede utilizar un punto "
                    "para los valores decimales."
                )
            )

        # Verificación de los rangos establecidos.
        notas = [nota1, nota2, nota3]

        if any(nota < 10 or nota > 70 for nota in notas):
            return render_template(
                "ejercicio1.html",
                error="Las notas deben estar entre 10 y 70."
            )

        if asistencia < 0 or asistencia > 100:
            return render_template(
                "ejercicio1.html",
                error="La asistencia debe estar entre 0 y 100."
            )

        # Cálculo del promedio sin redondeo.
        promedio = (nota1 + nota2 + nota3) / 3

        # Evaluación conjunta de las condiciones.
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        return render_template(
            "ejercicio1.html",
            promedio=promedio,
            estado=estado
        )

    return render_template("ejercicio1.html")


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    """
    Procesa el formulario de comparación de nombres.

    Admite nombres simples y compuestos, letras
    mayúsculas y minúsculas, tildes, ñ y ü.

    Rechaza números, símbolos, nombres vacíos y
    nombres duplicados sin distinguir mayúsculas.

    Para comparar las longitudes se cuentan únicamente
    las letras, excluyendo los espacios internos.

    Returns:
        str: Formulario HTML con resultados o errores.
    """

    if request.method == "POST":

        # Recepción y normalización de los nombres.
        nombre1 = normalizar_nombre(
            request.form.get("nombre1")
        )

        nombre2 = normalizar_nombre(
            request.form.get("nombre2")
        )

        nombre3 = normalizar_nombre(
            request.form.get("nombre3")
        )

        nombres = [nombre1, nombre2, nombre3]

        # Verificación de campos vacíos.
        if not all(nombres):
            return render_template(
                "ejercicio2.html",
                error="Debe ingresar tres nombres."
            )

        # Validación de caracteres permitidos.
        if not all(validar_nombre(nombre) for nombre in nombres):
            return render_template(
                "ejercicio2.html",
                error=(
                    "Los nombres solo pueden contener letras, "
                    "tildes y espacios entre palabras. "
                    "No se permiten números ni símbolos."
                )
            )

        # Comparación sin distinguir mayúsculas.
        nombres_comparables = [
            nombre.casefold() for nombre in nombres
        ]

        if len(set(nombres_comparables)) != 3:
            return render_template(
                "ejercicio2.html",
                error="Debe ingresar tres nombres diferentes."
            )

        # Conteo exclusivo de letras.
        def contar_letras(nombre):
            """
            Cuenta las letras de un nombre.

            Los espacios internos no se consideran
            para determinar su longitud.
            """

            return len(nombre.replace(" ", ""))

        # Selección del nombre con mayor longitud.
        # En caso de empate se conserva el primero.
        nombre_mayor = max(nombres, key=contar_letras)

        cantidad_caracteres = contar_letras(nombre_mayor)

        return render_template(
            "ejercicio2.html",
            nombre_mayor=nombre_mayor,
            cantidad_caracteres=cantidad_caracteres
        )

    return render_template("ejercicio2.html")


if __name__ == "__main__":
    app.run(debug=True)