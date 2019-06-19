def generapares(limite):

	num=1

	while num<limite:

		yield num*2

		num=num+1

devuelvepares=generapares(10)	
	

print(next(devuelvepares))

print("mas codigo")

print(next(devuelvepares))

print("mas codigo")

print(next(devuelvepares))

print("mas codigo")

def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		#for subelemento in elemento:
		yield from elemento

ciudades_devueltas=devuelve_ciudades("Guadalajara","CDMX","Queretaro","Leon")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

