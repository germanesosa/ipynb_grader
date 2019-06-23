# Jupyter Grader

Este cuaderno interactivo de Jupyter Notebook fue creado con el objetivo de fijar un criterio de corrección (rúbrica) aprovechando las posibilidades de ipywidgets, emulando el sistema utilizado en sistemas LMS como Moddle.

Además de lograr un criterio transversal de corrección entre un equipo de docentes, puede ser compartido con los alumnos con antelación a la ejecución de la tarea (tarea propiamente dicha, examen, trabajo práctico, etc).

Para calificar una tarea, se debe:
- Crear una copia de este archivo y del archivo jupyter_grader.py en una Carpeta que identifique a la tarea en cuestión. 
- Determinar los tipos de rúbrica, tal como se hace en el ejemplo.
- Crear grupos de calificación indicando en cada uno los items a evaluar, y el tipo de rúbrica asociado, como en el ejemplo.
- Generar una copia de este archivo .ipynb para cada alumno (o grupo) al que se vaya a corregir la tarea, dando a la copia un nombre representativo.

Para almacenar la calificación:
- El método exportar() crea un archivo con el mismo nombre dado a este archivo y extensión .csv donde se almacenan las calificaciones de cada item.
- El método importar() permite traer una calificación previamente realizada, para editarla y luego volver a exportarla cuando sea necesario
