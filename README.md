# PROYECTO.FINAL


¡Hola! Mi nombre es Tomás Arroyo, alumno de Henry, y este es el proyecto que desarrollé como MLOps Engineer en Steam, una plataforma multinacional de videojuegos. Aquí te presentaré un vistazo general sobre el trabajo que realicé.

Contexto
Fui encargado de crear un sistema de recomendación de videojuegos para los usuarios de Steam como Ingeniero de Datos. Sin embargo, al analizar la madurez de los datos proporcionados, me encontré con diversos desafíos: datos anidados, falta de procesos automatizados para actualizar productos y más. Por lo tanto, me vi en la necesidad de empezar desde cero, lo que representó un emocionante desafío.

ETL
El primer paso fue realizar (ETL) extracción, transformacion y carga de datos. los mismos llegaron en un formato .gz, primero hubo que descomprimirlos, luego una vez como json, los abri y transforme. saque aquellas columnas innecesarias, tambien elimine los valores faltantes. Con la funcion Merge uni los 3 Dataframes iniciales para poder trabajar con un unico dataframe desde donde realizar las consultas.
esta limpieza y preparación de los datos lo realice para poder optimizar el rendimiento de la API y facilitar el entrenamiento del modelo de aprendizaje automático.

Desarrollo API con FastAPI

Desarrollé una API utilizando el framework FastAPI respetando los criterios APIREST me ayude mucho con el video https://www.youtube.com/watch?v=J0y2tjBz2Ao. Teniendo lo basico de la Fastapi empece a realizar las consultas. Algunos de los endpoints que creé incluyen:

ENDPOINTS
PlayTimeGenre: Devuelve el año con más horas jugadas para un género específico.
UserForGenre: Muestra el usuario que ha jugado más horas para un género en particular.

Modelo de Aprendizaje Automático
Después de preparar los datos y desarrollar la API, entrené un sistema de recomendación de videojuegos. Opté por relación user-item para hacer las recomendaciones. El resultado de este modelo puede consumirse a través de la API, el modelo recomendara 5 juegos para el usuario.

RENDER

Por ultimo, hice el despliegue del codigo para su consulta web desde Render. me fue bastante dificultoso dado que no podia avanzar a la hora de hacer el commit en render, hasta que comprendi que era un problema con las librerias y una vez modificado los nombres de las librerias desde el archivo requirements.txt pude finalmente subir el codigo.

Video Demo
Grabé un video corto donde muestro el resultado de las consultas propuestas y del modelo de ML entrenado el cual comparti en youtube para que lo puedas ver.


PD
por una cuestion de tiempo no llegue a finalizar el analisis de sentimiento

contacto
tomas.alejandro.arroyo@gmail.com

