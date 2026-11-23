
# APLICACIÓN WEB CON PYTHON Y FLASK

## 1. IDENTIFICACIÓN DEL PROYECTO

**Asignatura:** Programación Web  
**Evaluación:** Encargo N.º 3 - Unidad III  
**Estudiante:** Marcela Muñoz Dorado  
**Institución:** IPLACEX  
**Fecha:** 20-11-2026  

## 2. DESCRIPCIÓN GENERAL

Aplicación web desarrollada mediante Python y el framework Flask, que integra dos ejercicios de procesamiento de datos a través de formularios HTML.

El proyecto incorpora navegación entre páginas, validación de entradas, manejo de errores, procesamiento de solicitudes HTTP y presentación dinámica de resultados.

La interfaz utiliza HTML5 y CSS3, con un diseño adaptable a diferentes tamaños de pantalla.

## 3. FUNCIONALIDADES

### 3.1. Ejercicio N.º 1: Formulario de Notas

Permite ingresar tres notas y un porcentaje de asistencia para calcular el promedio y determinar el estado académico.

**Reglas de funcionamiento:**

- Las notas deben estar comprendidas entre 10 y 70.
- La asistencia debe encontrarse entre 0 % y 100 %.
- El promedio se calcula sumando las tres notas y dividiendo el resultado por tres.
- Para aprobar, se requiere un promedio mayor o igual a 40 y una asistencia mínima del 75 %.
- Si no se cumplen ambas condiciones, el estado será REPROBADO.
- El cálculo se realiza sin aplicar redondeo explícito.

El formulario incorpora validaciones para evitar el procesamiento de valores inválidos o fuera de los rangos establecidos.

### 3.2. Ejercicio N.º 2: Formulario de Nombres

Permite ingresar tres nombres diferentes y determinar cuál contiene la mayor cantidad de letras.

**Reglas de funcionamiento:**

- Se admiten nombres simples y compuestos.
- Se permiten letras mayúsculas, minúsculas, tildes, ñ y ü.
- Se rechazan números, símbolos y campos vacíos.
- No se permiten nombres duplicados, sin distinguir mayúsculas y minúsculas.
- Los espacios internos no se consideran para el conteo de letras.
- Se identifica el nombre con mayor cantidad de caracteres alfabéticos.
- En caso de empate, se conserva el primer nombre que alcanza la longitud máxima.

Los resultados se presentan directamente en el formulario correspondiente.

## 4. TECNOLOGÍAS UTILIZADAS

- Python 3.12
- Flask 3.1.3
- HTML5
- CSS3
- Jinja2
- PyCharm como entorno de desarrollo integrado
- Git para control de versiones
- GitHub para alojamiento del código fuente

## 5. ESTRUCTURA DEL PROYECTO

    encargo_3_flask_iplacex/
    |
    |-- main.py
    |-- requirements.txt
    |-- .gitignore
    |-- README.md
    |
    |-- templates/
    |   |-- index.html
    |   |-- ejercicio1.html
    |   |-- ejercicio2.html
    |
    |-- static/
        |-- style.css

**Descripción de los archivos:**

- `main.py`: contiene la aplicación Flask, las rutas, funciones, validaciones y lógica de procesamiento.
- `index.html`: presenta el menú principal.
- `ejercicio1.html`: contiene el formulario de notas y asistencia.
- `ejercicio2.html`: contiene el formulario de comparación de nombres.
- `style.css`: define los estilos visuales de la aplicación.
- `requirements.txt`: identifica las dependencias de Python.
- `.gitignore`: establece las exclusiones para el control de versiones.
- `README.md`: documenta el proyecto.

## 6. INSTALACIÓN Y EJECUCIÓN

### 6.1. Requisitos previos

Disponer de Python 3.12 y una conexión a Internet para instalar las dependencias necesarias.

### 6.2. Obtener el proyecto

Descargar el repositorio desde GitHub o clonarlo mediante Git y abrir su carpeta en PyCharm.

### 6.3. Crear un entorno virtual

Desde la terminal del proyecto, ejecutar:

    python3 -m venv .venv

Activar el entorno virtual en macOS:

    source .venv/bin/activate

### 6.4. Instalar las dependencias

Ejecutar:

    python -m pip install -r requirements.txt

Este comando instalará Flask y las dependencias necesarias para su funcionamiento.

### 6.5. Ejecutar la aplicación

Desde la carpeta principal del proyecto, ejecutar:

    python main.py

### 6.6. Acceder desde el navegador

Abrir la siguiente dirección:

    http://127.0.0.1:5000

La página principal permitirá acceder a ambos ejercicios.

## 7. CONSIDERACIONES TÉCNICAS

La aplicación utiliza Flask para administrar las rutas y procesar los formularios mediante solicitudes HTTP GET y POST.

Las plantillas HTML se renderizan utilizando Jinja2.

Los datos ingresados son sometidos a validaciones en el navegador y en el servidor.

El código Python incorpora funciones para convertir entradas numéricas, normalizar nombres y comprobar caracteres permitidos.

La aplicación se ejecuta localmente mediante el servidor de desarrollo de Flask, el cual no está destinado a entornos de producción.

## 8. CONTROL DE VERSIONES

El proyecto contempla el uso de Git y GitHub para almacenar y compartir su código fuente.

El archivo `.gitignore` excluye elementos locales y temporales, particularmente el entorno virtual de Python, que no resulta necesario incorporar al repositorio.

Las dependencias requeridas se encuentran identificadas en `requirements.txt`.

## 9. AUTORÍA

**Desarrollado por:** Marcela Muñoz Dorado.

**Identificación de la aplicación:** Programa creado por MMD.

**Finalidad:** Desarrollo académico correspondiente al Encargo N.º 3 de la Unidad III.
