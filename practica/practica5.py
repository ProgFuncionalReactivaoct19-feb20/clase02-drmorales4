"""
	Practica 5: uso de funcion lambda
	@drmorales4
"""
import math # para hacer raiz cuadrada

datos = [(10,2), (8,7), (5,4), (3,11), (10,11)]

funcion1 = lambda x: x[0]
funcion2 = lambda x: x[1]

funciones = lambda x: (math.sqrt(funcion1(x)), funcion2(x)**2)

print(list(map(funciones, datos)))
