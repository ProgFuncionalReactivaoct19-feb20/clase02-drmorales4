"""
	Practica 4: uso de funcion lambda
	@drmorales4
"""

lista = [10,2,8,7,5,4,3,11,0, 1]

elevado = lambda x: x**3

print(list(map(elevado, lista)))