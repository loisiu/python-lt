print ("LA VAYA SCHOOL")

calif_alumno=input("calificacion del Mono:_")

def evaluacion(calif):
	valoracion="aprobado"
	if calif<5:
		valoracion="reprobado"
	return valoracion
	

print(evaluacion(int(calif_alumno)))





