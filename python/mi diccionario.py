vayadiccionario={"alemania":"berlin","francia":"paris","mexico":"df","canada":"toronto"}

vayadiccionario["italia"]="lisboa"

print(vayadiccionario["francia"])

print(vayadiccionario)
vayadiccionario["italia"]="roma"
print(vayadiccionario)
del(vayadiccionario["francia"])
print(vayadiccionario)

vayadiccionariomix={"jordan":23, "nba":"usa", "chicago":"bulls"}
print(vayadiccionariomix)

tuplama=["alemania","mexico","francia","toronto"]
midiccionario={tuplama[0]:"berlin",tuplama[1]:"df",tuplama[2]:"paris",tuplama[3]:"canada"}
print(midiccionario["mexico"])
minba={23:"jordan","nombre":"michael","team":"bulls","anillos":[91,92,93, 96, 97, 98]}
print(minba["anillos"])
minba={23:"jordan","nombre":"michael","team":"bulls","anillos":{"temporada":[91,92,93, 96, 97, 98]}}
print(minba.keys())
print(minba.values())
print(len(minba))
print(minba)










