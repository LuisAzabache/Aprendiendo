#DICCIONARIOS
#Tiene una estructura de clave:valor

midiccionario={"Alemania":"Berlin", "Francia":"Paris", "ReinoUnido":"Londres", "España":"Madrid"}
print(midiccionario["Francia"])
print(midiccionario["España"])
#imprime
#Paris
#Madrid

#Agregar elementos a un diccionario ya construido
midiccionario={"Alemania":"Berlin", "Francia":"Paris", "ReinoUnido":"Londres", "Españana":"Madrid"}
midiccionario["Italia"]="Lisboa"   #de esta nmanera se añade un nuevo elemento a un diccionario
print(midiccionario)
#imprime {'Alemania': 'Berlin', 'Francia': 'Paris', 'ReinoUnido': 'Londres', 'Españana': 'Madrid', 'Italia': 'Lisboa'}

#ya que se hizo un error de que Lisboa es la capital de Italia se debe corregir
midiccionario["Italia"]="Roma"
print(midiccionario)
#Imprime {'Alemania': 'Berlin', 'Francia': 'Paris', 'ReinoUnido': 'Londres', 'Españana': 'Madrid', 'Italia': 'Lisboa'} con error
#Imprime {'Alemania': 'Berlin', 'Francia': 'Paris', 'ReinoUnido': 'Londres', 'Españana': 'Madrid', 'Italia': 'Roma'}   con correccion

#para eliminar un elemento se utiliza el metodo "del"
del midiccionario["ReinoUnido"]
print(midiccionario)
#imprime {'Alemania': 'Berlin', 'Francia': 'Paris', 'Españana': 'Madrid', 'Italia': 'Roma'}

midiccionario={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(midiccionario)
#imprime {'Alemania': 'Berlin', 23: 'Jordan', 'Mosqueteros': 3}

# Se asigna valores mediante tuplas de la siguiente manera
mitupla=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres", mitupla[3]:"Berlin"}
print(midiccionario)
#imprime  {'España': 'Madrid', 'Francia': 'Paris', 'Reino Unido': 'Londres', 'Alemania': 'Berlin'}
print(midiccionario["Francia"])
#imprime Paris


#Como hacer que un diccionario almacene una tupla
midiccionario={23:"Jordan", "Nombre": "Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario)
#imprime {23: 'Jordan', 'Nombre': 'Michael', 'Equipo': 'Chicago', 'anillos': [1991, 1992, 1993, 1996, 1997, 1998]}

print(midiccionario["Equipo"])
#imprime Chicago

print(midiccionario["anillos"])
#imprime [1991, 1992, 1993, 1996, 1997, 1998]   se ha impreso una tupla que se encontraba dentro de un diccionario


#Como incluir un diccionario dentro de otro diccionario
midiccionario1={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario1)
#imprime {23: 'Jordan', 'Nombre': 'Michael', 'Equipo': 'Chicago', 'anillos': {'Temporadas': [1991, 1992, 1993, 1996, 1997, 1998]}}

#para imprimir los valores o las claves se usan los métodos "keys" y "values"
midiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario.keys())    #metodo keys
#imprime  dict_keys([23, 'Nombre', 'Equipo', 'anillos'])   <--- Se imprime las claves del diccionario

print(midiccionario.values())     #metodo values
#imrpime   dict_values(['Jordan', 'Michael', 'Chicago', {'Temporadas': [1991, 1992, 1993, 1996, 1997, 1998]}])       <----- se imprime los valores del diccionario

#longitud del diccionario
print(len(midiccionario))
#imprime  4

