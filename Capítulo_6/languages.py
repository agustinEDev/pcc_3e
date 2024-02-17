favorite_languages = {
    "Agustín" : "Python",
    "José" : "C#",
    "Nuria" : "Java",
    "Ana" : "HTML",
    "Joserrili" : "Caca"
}

print(f"El lenguaje de programación favorito de José es {favorite_languages['José']}.")

#utilizamos el método get para obtener un valor y que no de error

berta_language = favorite_languages.get("Berta", "No existe lenguaje para Berta")
print(f"El lenguaje favorito de Berta es: {berta_language}.")

ana_language = favorite_languages.get("Ana", "No existe lenguaje para Ana")
print(f"El lenguaje favorito de Ana es: {ana_language}.")