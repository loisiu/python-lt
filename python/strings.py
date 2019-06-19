nombreusuario=input("Introduce nombre de usuario:  ")
	
print("El nombre es:  ", nombreusuario.capitalize())

edad=input("Introduce la edad:  ")

while(edad.isdigit()==False):

	print("Introduce valor numerico")

	edad=input("Introduce la edad")

print(edad.isdigit())

if(int(edad)<18):

	print("acceso denegado")

#Crea un programa que pida introducir una dirección de email por teclado.
#El programa debe imprimir en consola si la dirección de email es correcta 
#o no en función de si esta tiene el símbolo ‘@’.
#Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o ninguna ‘@’ la dirección será errónea.
#Si la ‘@’ esta al comienzo de la dirección de email o al final, la dirección también será errónea, 
 
mailusuario=input("Introduce direccion de email:    ")
arroba=mailusuario.count('@')

if(arroba!=1 or mailusuario.rfind('@')==(len(mailusuario)-1) or mailusuario.find('@')==0):
	print("Mail incorrecto")


else:
	print("Mail correcto")

my_string ="Hola Mundo!" "loi"
my_string = "Este string contiene \n saltos de Linea"

course = "python 3"
name = "loi"	

final_message = "Nuevo curso de " + course + "por" + name #1
final_message = "Nuevo curso de %s por %s" %(course, name) #2
final_message = "Nuevo curso de {} por {}".format(course, name) #3

print (my_string)
print (final_message)




