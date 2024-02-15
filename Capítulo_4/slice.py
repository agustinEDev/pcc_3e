players = ["ross", "joey", "chandler", "rachel", "monica", "phoeby"]
#Imprimimos desde el 0 hasta el 3
print(players[0:3])
#Imprimimos desde el 3 hasta el 6
print(players[3:6])
#Imprimimos a partir del 3
print(players[3:])
#Imprimimos hasta el 3
print(players[:3])

#Utilizamos un bucle para imprimir desde una posición
for player in players[3:]:
    print(player)
#Utilizamos el bucle para imprimir hasta una posición
for player in players[:-3]:
    print(player)
