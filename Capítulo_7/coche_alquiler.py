#Creamos una lista con las marcas de coches que tenemos
coches = ['ford', 'volvo', 'seat', 'citroen']

print("Bienvenido al programa de alquiler de coches...\n")
peticion = input("Qué marca de coche desea alquilar? ")
if peticion.lower() in coches:
    print(f"La marca {peticion.title()} está disponible.")
else:
    print(f"La marca {peticion.title()} no está disponible.")

print("\nFin del programa.\n")