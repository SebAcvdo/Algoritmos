En caso de no tener alguna librería instalada, ejecutar los siguientes comandos en la consola.

heapq = pip install heapq
copy = pip install copy
timeit = pip install timeit
tabulate = pip install tabulate
numpy = pip install numpy
matplotlib = pip install matplotlib
pillow = pip install pillow
cv 2= pip install opencv-python
msvcrt = pip install getch


Es de suma importancia abrir la carpeta completa del proyecto(Practica 4) para ejecutarlo de manera correcta.

El programa despliega un menú donde es posible seleccionar alguna opcion en base a las pruebas solicitadas en la práctica.

Al seleccionar alguna opción, despliega en la consola la codificación del contenido del archivo seleccionado, seguido del 
árbol binario de los caracteres que conforman el archivo. Después de esto imprime archivo de entrada, archivo de salida,
bits totales sin comprimir, bits totales al comprimir, porcentaje de compresión, tiempo y una tabla con los caracteres, su 
frecuencia y su codigo

Al ejecutar alguna de las opciones disponibles por primera vez, se genera un nuevo archivo txt donde se almacena el mensaje
descomprimido.

En el caso de la imagen, ejecuta primero una funcion, la cual se encarga de convertir la imagen a escale de grises para después
mapear la imagen, para poder escribirlo en un txt que será después comprimido y descomprimido. En pocas palabras, al comprimir 
una imagen generamos 3 archivos. El primero es un mapeo de la imagen, el segundo la descompresion y el tercero la imagen en 
escala de grises. 

Si se desea realizar otra prueba, basta con ejecutar de nuevo el programa.

Si se desea ejecuitar algún testeo, se puede modificar el contenido de los archivos txt. El archivo de salida contendrá el mismo texto.