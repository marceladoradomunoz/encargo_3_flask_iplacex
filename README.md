
# APLICACIÓN WEB CON PYTHON Y FLASK

## APLICACIÓN PUBLICADA

**[ABRIR APLICACIÓN WEB EN RENDER](https://encargo-3-flask-iplacex.onrender.com)**

La aplicación permite ejecutar ambos ejercicios directamente desde un navegador web.

**Nota:** El servicio utiliza el plan gratuito de Render, por lo que el primer acceso puede demorar después de un período de inactividad.

## 1. IDENTIFICACIÓN DEL PROYECTO

**Asignatura:** Programación Web  
**Evaluación:** Encargo N.º 3 - Unidad III  
**Estudiante:** Marcela Muñoz Dorado  
**Institución:** IPLACEX  
**Fecha:** 20-11-2026

## 2. DESCRIPCIÓN

Aplicación web desarrollada con Python y Flask, que integra dos formularios HTML para procesar información, validar entradas y presentar resultados.

**Ejercicio N.º 1: Formulario de Notas**

Calcula el promedio de tres notas y determina el estado académico. Para aprobar se requiere un promedio mínimo de 40 y una asistencia igual o superior al 75 %.

**Ejercicio N.º 2: Formulario de Nombres**

Compara tres nombres diferentes e identifica aquel que contiene la mayor cantidad de letras, excluyendo los espacios. Incorpora validaciones de caracteres y nombres duplicados.

## 3. TECNOLOGÍAS UTILIZADAS

- Python
- Flask 3.1.3
- HTML5 y CSS3
- Jinja2
- Gunicorn 23.0.0
- Git y GitHub
- Render

## 4. ESTRUCTURA DEL PROYECTO

    encargo_3_flask_iplacex/
    ├── main.py
    ├── requirements.txt
    ├── .gitignore
    ├── README.md
    ├── static/
    │   └── style.css
    └── templates/
        ├── index.html
        ├── ejercicio1.html
        └── ejercicio2.html

## 5. INSTALACIÓN Y EJECUCIÓN LOCAL

Desde la carpeta principal del proyecto, ejecutar:

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
    python main.py

Abrir en el navegador:

http://127.0.0.1:5000

## 6. AUTORÍA

**Desarrollado por:** Marcela Muñoz Dorado.

**Identificación:** Programa creado por MMD.
