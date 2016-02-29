def f (p, *otros):
	"""Esta función imprime en pantalla 
	el primer valor, el los siguientes en forma de Tupla
	y la tupla separada."""

	print "Numero"
	print p

	print "Tupla junta"
	print otros

	print "Tupla separada"
	for i in otros:
		print i

f(8)
f(8,1)
f(8,1,2)
f(8,1,2,3)

def sumar (x,y):
	#Suma dos números y los devuelve como una función
	return x + y

suma = sumar (3,4)
print suma