import pickle

fichero=open("lista_nombre", "rb")

lista=pickle.load(fichero)

print(lista)

