print ("LA VAYA CIA")

Salario_presidente=int(input("introduce salario presidente  "))
print ("salario presidente:  " + str(Salario_presidente))

Salario_director=int(input("introduce salario director  "))
print ("salario director:  " + str(Salario_director))

Salario_jefe=int(input("introduce salario jefe  "))
print ("salario jefe:  " + str(Salario_jefe))

Salario_Admin=int(input("introduce salario Admin  "))
print ("salario Admin:  " + str(Salario_Admin))

if Salario_Admin<Salario_jefe<Salario_director<Salario_presidente:
	print("todo funciona correctamente")
else:
	print("algo fallo")
	
