def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1, num2):
	
	try:
		return num1/num2

	except ZeroDivisionError:
		print("No se puede divir entre 0")
		return "operacion erronea"
		
while True:
	try:
		op1=(int(input("introduce el primer numero")))

		op2=(int(input("introduce el segundo numero")))

		break

	except ValueError:
		print("Los valores son incorrectos, intenta de nuevo  ")

operacion=input ("introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1, op2))

elif operacion=="multiplica":
	print(multiplica(op1, op2))

elif operacion=="divide":
	print(divide(op1, op2))

else:
	print ("operacion no contemplada")

print ("operacion ejecutada. continuacion del programa")

