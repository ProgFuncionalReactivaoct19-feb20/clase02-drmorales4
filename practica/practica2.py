"""
	Practica 2: uso de funcion lambda
	@drmorales4
"""

cadena_personalizada = lambda x, y: "%s capital de %s" % (x.upper(), y.upper())

print(cadena_personalizada("Cuenca", "Azuay"))