class Auto():

	def __init__(self):

		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False

	def arrancar(self,arrancamos):
		self.__enmarcha=arrancamos

		if(self.__enmarcha):
			Chequeo=self.__chequeo_interno()
		
		if(self.__enmarcha and Chequeo):
			return "el auto esta en Marcha"

		elif(self.__enmarcha and Chequeo==False):
			return "Algo esta fallando, no podemos arrancar"	

		else: 

			return "El auto esta Parado"

	def estado(self):
		print("El auto tiene ", self.__ruedas, "ruedas. una Ancho de", self.__anchoChasis, "y el largo de ", self.__largoChasis)		
	
	def __chequeo_interno(self):
		print ("Realizando Chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

			return True

		else:
		
			return False	




miAuto=Auto()
print(miAuto.arrancar(True))
miAuto.estado()


print("---------------segundo objeto----------")

miAuto2=Auto()
print(miAuto2.arrancar(False))
miAuto2.estado()









