# Bajibot Backend

## Descripción

Este proyecto fue propuesto para el curso de Inteligencia Artificial del ciclo VII de la carrera de Ingeniería de Sistemas de la Universidad Nacional Mayor de San Marcos.

La finalidad de este proyecto fue aplicar los conocimientos adquiridos en el curso, por ello, se opto por el desarrollo de un chatbot sobre recetas de comida.

## Características

- Este sistema permite al usuario ingresar sus preferencias para una mejor recomendación de recetas.
- Este sistema contiene un chatbot para interactuar con el usuario.

## Herramientas utilizadas

- Python
- Flask
- Sqlite3
- Gemini API
- Pycharm
- Postman

## Requisitos

- Instalar un IDE o editor de código configurado para Python.
- Instalar Python 3.8 o superior.
- Adquirir una API Key de Gemini API.

## Instrucciones para su uso

- Clonar el repositorio.
````bash
git clone https://github.com/Fabo2303/bajibot-backend.git
````
- Abrir el proyecto en un IDE o editor de código.
- Instalar las dependencias.
````bash
pip install -r requirements.txt
````
- Crear un archivo .env en la raíz del proyecto.
- Agregar la API Key de Gemini API al archivo .env.
````bash
SECRET_KEY = 'SECRET_KEY'
JWT_SECRET_KEY = 'JWT_SECRET'
GEMINI_API_KEY = 'API_KEY'
````
- Ejecutar el archivo app.py.
````bash
python app.py
````

## Análisis con Sonarqube
![Análisis con Sonarqube](https://github.com/user-attachments/assets/f57dc08c-4471-4730-96e4-2ab0d3bd53d8)