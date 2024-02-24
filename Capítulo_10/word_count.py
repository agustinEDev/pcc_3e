from pathlib import Path

def count_words(path):
    #Cuenta el número de palabras de un archivo
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        #Hacemos que el fallo sea silencioso
        #path = f'{path}'
        #print(f"El fichero {path.removeprefix('../files/')} no existe.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        path = f'{path}'
        print(f"El fichero {path.removeprefix('../files/')} tiene {num_words} palabras. ")

filenames = ['alice.txt', 'siddarta.txt', 'little_women.txt', 'moby_dick.txt']
for filename in filenames:
    ruta = '../files/' + filename
    path = Path(ruta)
    count_words(path)
