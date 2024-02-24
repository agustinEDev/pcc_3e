from pathlib import Path

#Podemos darle el path relativo '../files/pi_digits.py' o el absoluto:
file = Path('/Users/agustined/Desktop/python_work/files/pi_digits.txt')
#Utilizamos el método read_text() para leer el contenido completo del fichero
#El método rstrip() quita los espacios que haya a la derecha del contenido
content = file.read_text().rstrip()
#Imprimimos el contenido de la variable
print(f"{content}\n")

#Dividimos el contenido en líneas y lo imprimimos en un bucle
lines = content.splitlines()
for line in lines:
    print(f"{line}")
print()

#Concatenamos las líneas en una variable y la imprimimos por pantalla
pi_lines=''
for line in lines:
    pi_lines += line
print(f"{pi_lines}\n")

#Abrimos un fichero nuevo
file_long = Path('../files/pi_million_digits.txt')
content_long = file_long.read_text()
lines_long = content_long.splitlines()
pi_long_lines = ''
for line in lines_long:
    pi_long_lines += line

print(f"{pi_long_lines[:80]}")
print(len(pi_long_lines))

birthday = input("Type your bithday in the form ddmmyy ---> ")
if birthday in pi_long_lines:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Sorry, your birthday don´t appear in the first million digits of pi.")