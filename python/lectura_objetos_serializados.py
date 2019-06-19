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

ficheroApertura=open("loscoches", "rb")

miscoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in miscoches:

	print(c.estado())

