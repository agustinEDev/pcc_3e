current_users = ["jorge", "félix", "yelena", "admin", "jose antonio", "andré", "diana", "marcos"]
new_users = ["Francisco", "JORGE", "Jose Antonio", "Manuel"]
#Si current_users está vacía no haría la comprobación de los nombre
if current_users:
    for new_user in new_users:
        if new_user.lower() in current_users:
            print(f"El usuario {new_user.title()} ya existe. Introduzca otro.")
        else:
            current_users.append(new_user.lower())
            print(f"Se añade {new_user.title()} a la lista de usuarios.")
else:
    for new_user in new_users:
        current_users.append(new_user.lower())
        print(f"Se añade {new_user.title()} a la lista de usuarios.")

print("Los usuarios dados de alta son:")
print(current_users)