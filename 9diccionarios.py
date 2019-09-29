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

mitupla=["España", "Francia", "Reino Unido", "Alemania"]
midiccionario={mitupla}

