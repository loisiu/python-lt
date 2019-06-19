import math

#def evaluaedad(edad):
#	if edad<0:
#		raise TypeError("Que os pasa?, edad negativa")
#	if edad<20:
#		return "eres un puberto"
#	elif edad<40:
#		return "eres un polluelo"
#	elif edad<65:
#		return "vales mucho"
#	elif edad<100:
#		return "Miami"

#print (evaluaedad(46))	

def calculaRaiz(num1):

	if num1<0:
		raise ValueError("El Número no puede ser negativo")

	else:
		return math.sqrt(num1)

op1=(int(input("Introduce un numero:  ")))

try:
	print(calculaRaiz(op1))

except ValueError as ErrordeNumeroNegativo:

	print(ErrordeNumeroNegativo)

print("Programa Terminado")


