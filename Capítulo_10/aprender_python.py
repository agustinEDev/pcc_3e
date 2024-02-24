from pathlib import Path

path = Path('../files/aprender_python.txt')
file = path.read_text()
print(file)

#Recorremos directamente la lista que devuelve el splitlines
for linea in file.splitlines():
    linea = linea.replace('Python', 'C#')
    print(linea)

# ----------------- Escribir en un fichero ---------------------
#Este fragmento escribe una sola línea
path2 = Path('../files/programming.txt')
path2.write_text("Prueba de escritura.")

#El método write_text() sobreescribe el archivo
#Este fragmento escribe varias líneas concatenadas dentro de una variable.
cadena = 'Me gusta programar en Python.\n'
cadena += 'Python es como un lego.\n'
cadena += 'Me recuerda a mis tardes de pequeño en Sotelo.\n'
path2.write_text(cadena)