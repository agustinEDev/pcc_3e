invitados = ["winston churchill", "abraham lincoln", "steve jobs", "alejandro magno"]

print(f"Invito a cenar a {invitados[0].title()} para hablar sobre la WWII.")
print(f"Invito a cenar a {invitados[1].title()} para hablar sobre el fin de la esclavitud.")
print(f"Invito a cenar a {invitados[2].title()} para hablar sobre diseño e innovación.")
print(f"Invito a cenar a {invitados[3].title()} para hablar de la victoria sobre el imperio Persa.")

print(f"No puede asistir {invitados[2].title()}.")
invitados[2] = "julio cesar"

print(f"Invito a cenar a {invitados[0].title()} para hablar sobre la WWII.")
print(f"Invito a cenar a {invitados[1].title()} para hablar sobre el fin de la esclavitud.")
print(f"Invito a cenar a {invitados[2].title()} para hablar sobre el Imperio Romano.")
print(f"Invito a cenar a {invitados[3].title()} para hablar de la victoria sobre el imperio Persa.")

print("Hemos encontrado una mesa con 8 espacios.")
invitados.insert(0,"cleopatra")
invitados.insert(3,"vincent van gogh")
invitados.append("Freddy Mercury")

print(f"Invito a cenar a {invitados[0].title()} para hablar sobre la el imperio Egipcio.")
print(f"Invito a cenar a {invitados[1].title()} para hablar sobre la WWII.")
print(f"Invito a cenar a {invitados[2].title()} para hablar sobre el fin de la esclavitud.")
print(f"Invito a cenar a {invitados[3].title()} para hablar sobre el impresionismo.")
print(f"Invito a cenar a {invitados[4].title()} para hablar sobre el Imperio Romano.")
print(f"Invito a cenar a {invitados[5].title()} para hablar de la victoria sobre el imperio Persa.")
print(f"Invito a cenar a {invitados[6].title()} para hablar sobre Queen.")

print("Nos han comunicado que sólo hay una mesa para dos personas.")
print(f"Lo siento mucho, pero no puedo invitaros a cenar:\n{invitados[0].title()}, \n{invitados[2].title()}, \n{invitados[3].title()}, \n{invitados[4].title()}, \n{invitados[6].title()}")
del invitados[6]
del invitados[4]
del invitados[3]
del invitados[2]
del invitados[0]

print(f"Quedarían solo {len(invitados)} invitados para la cena.")
invitado_1 = invitados.pop(1)
invitado_2 = invitados.pop(0)

print(f"{invitado_1.title()} y {invitado_2.title()}, vosotros seguís invitados.")
print(invitados)
