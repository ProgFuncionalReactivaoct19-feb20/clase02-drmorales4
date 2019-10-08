"""
	Practica 3: uso de funcion lambda
	@drmorales4
"""

suma = (10, 11)
suma1 = lambda x: x[0]
suma2 = lambda x: x[1]

print(suma1(suma) + suma2(suma))
