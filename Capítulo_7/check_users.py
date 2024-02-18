unconfirmed_users = ['josé','nuria','ana','josesiño']
confirmed_users = []

while unconfirmed_users:
    user = unconfirmed_users.pop()
    print(f"Usuario {user.title()} confirmado.")
    confirmed_users.append(user)

print("\nLos siguientes usuarios han sido confirmados:")
for username in confirmed_users:
    print(username.title())

print("\nFin del programa.")