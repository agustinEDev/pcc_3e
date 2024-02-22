import sys
sys.path.append('../modulos/')
from modulos.boleto import Boleto

mi_boleto = Boleto()
mi_boleto.generar_numero()
boleto_premiado = Boleto()
contador = 0
print(f"Mi boleto: {mi_boleto.numero}")

while boleto_premiado.numero != mi_boleto.numero:
    boleto_premiado.generar_numero()
    contador += 1

print(f"Boleto premiado: {boleto_premiado.numero}")
print(f"Has necesitado {contador} intentos para ganar la lotería.")