class Vehiculo():

	def __init__(self, marca, modelo):
		
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelerar=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print ("Marca: ", self.marca, "\nmodelo: ", self.modelo,
		 "\nenmarcha: ", self.enmarcha, "\n:acelera ", self.acelera,
		  "\nfrena: ", self.frena)

class furgoneta(Vehiculo):

	def carga(self, carga):
		self.cargado=carga
		if(self.cargado):
			return "Con Carga"
		else:
			return "Sin carga"	


class moto(Vehiculo):
	hccaballito=""
	def caballito(self):
		self.hccaballito="voy haciendo el caballito"

	def estado(self):
		print ("Marca: ", self.marca, "\nmodelo: ", self.modelo,
		 "\nenmarcha: ", self.enmarcha, "\n:acelera ", self.acelera,
		  "\nfrena: ", self.frena, "\n", self.hccaballito)
	
class VElectricos(Vehiculo):
	def __init__(self, marca, modelo):
	
		super(). __init__(marca, modelo)
		
		self.autonomia=100

		
	def cargarEnergia(self):
		self.cargando=True	


mimoto=moto("Honda", "CBR1000")

mimoto.caballito()

mimoto.estado()

mifurgoneta=furgoneta("toyota", "Hilux")
mifurgoneta.arrrancar()
mifurgoneta.estado()
print(mifurgoneta.carga(True))

class bicicletaElectrica(VElectricos, Vehiculo):

	pass
	
mibici=bicicletaElectrica("Vaya", "monos")



	

class persona():

	def __init__(self, nombre, edad,  lugar_residencia):

		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=lugar_residencia

	def descripcion (self):

		print ("nombre:  ", self.nombre,
		 "edad:  ", self.edad,
		  "lugar_residencia:     ", self.lugar_residencia)

		
class empleado(persona):

	def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, lugar_residencia_empleado):

		super().__init__(nombre_empleado, edad_empleado, lugar_residencia_empleado)

		self.salario=salario
		self.antigüedad=antigüedad

	def descripcion(self):

		super().descripcion()

		print("salario:  ", self.salario, "antigüedad:  ", self.antigüedad)	

loi=persona("loi", 46, "mexico")


loi.descripcion()

print(isinstance(loi,persona))
