course = "el mio"
my_string = "curso Python Loi"


"""FORMATO"""
result = "{} de {} " .format(course, my_string)
result = result.lower()
result = result.upper()
print (result)

"""BUSQUEDA"""

pos = result.find ("codigo")
count = result.count ("C")
print (pos)


new_string = result.replace ("c", "f")
#new_string = result.split (" ")
print (new_string)