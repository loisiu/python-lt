def sumar(op1,op2):
	print("El resultado de la suma es:   ", op1+op2)

def restar(op1,op2):
	print("El resultado de la resta es:   ", op1-op2)

def multiplicar(op1,op2):
	print("El resultado de la multipicacion es:   ", op1*op2)

def dividir(dividendo,divisor):
	print("El resultado de la division es:    ", dividendo//divisor)



number_one = 10
number_two = 4

result = number_one + number_two
print ("suma", result)

result = number_one - number_two
print ("Resta", result)

result = number_one * number_two
print ("Multiplicacion", result)

result = number_one / number_two #regresa un flotante
print ("Division", result)

result = number_one // number_two #Regresa un entero
print ("Division", result)

result = number_one ** number_two #Regresa un numero exponencial
print ("Exponencial", result)