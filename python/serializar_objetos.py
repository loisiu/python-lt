import pickle


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


coche1=Vehiculo("toyota", "Corolla")

coche2=Vehiculo("vw", "golf")

coche3=Vehiculo("kia", "forte")

coches=[coche1, coche2, coche3]

fichero=open("loscoches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del(fichero)

ficheroApertura=open("loscoches", "rb")

miscoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in miscoches:

	print(c.estado())





