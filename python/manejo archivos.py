from io import open

archivo_texto=open("archivo.txt","r+") #lectura y escritura

#print(archivo_texto.read())

#archivo_texto.seek(11)

#print(archivo_texto.read(11))

#print(archivo_texto.read())

#archivo_texto.seek(len(archivo_texto.readline(1)))

#print(archivo_texto.readline())

#archivo_texto.write("comienzo el texto")

#print(archivo_texto.readline())

lista_texto=archivo_texto.readlines();

lista_texto[1]="Esta linea ha sido incluida desde el interior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()





