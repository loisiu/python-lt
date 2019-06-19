print("VAYA ASIGNATURAS")
print("Asignaturas opcionales: Python - Java - PHP")
opcion=input("Selecciona la asignatura:  ")

asignatura=opcion.lower()

if asignatura in ("python", "java", "php"):
	print("Asignatura Elegida" + asignatura)

else:
	print("La asignatura es Incorrecta")

