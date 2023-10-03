# PROYECTO.FINAL


¡Hola! Mi nombre es Tomás Arroyo, alumno de Henry, y este es el proyecto que desarrollé como MLOps Engineer en Steam, una plataforma multinacional de videojuegos. Aquí te presentaré un vistazo general sobre el trabajo que realicé.

Contexto
Fui encargado de crear un sistema de recomendación de videojuegos para los usuarios de Steam. Sin embargo, al analizar la madurez de los datos proporcionados, me encontré con diversos desafíos: datos anidados, falta de procesos automatizados para actualizar productos y más. Por lo tanto, me vi en la necesidad de empezar desde cero, lo que representó un emocionante desafío.

Transformaciones
Realicé una limpieza y preparación de los datos mismos para optimizar el rendimiento de la API y facilitar el entrenamiento del modelo de aprendizaje automático.

Desarrollo API con FastAPI
Desarrollé una API utilizando el framework FastAPI. Algunos de los endpoints que creé incluyen:

PlayTimeGenre: Devuelve el año con más horas jugadas para un género específico.
UserForGenre: Muestra el usuario que ha jugado más horas para un género en particular.
UsersRecommend: Proporciona el top 3 de juegos más recomendados por año.
Modelo de Aprendizaje Automático
Después de preparar los datos y desarrollar la API, entrené un sistema de recomendación de videojuegos. Opté por relación user-item para hacer las recomendaciones. El resultado de este modelo puede consumirse a través de la API.

Video Demo
Grabé un video corto donde muestro el resultado de las consultas propuestas y del modelo de ML entrenado el cual comparti en youtube para que lo puedas ver.
