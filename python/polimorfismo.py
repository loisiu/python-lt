class Vayamonos():

	def personajes(self):
		print("Una familia de simpaticos primates")


class osos():

	def personajes(self):
		print("abrazo de osos")


class littlecast():

	def personajes(self):
		print("pequeñiños")



def personajesmarca(marca):
	marca.personajes()


mimarca=littlecast()

personajesmarca(mimarca)

mimarca=Vayamonos()

personajesmarca(mimarca)


