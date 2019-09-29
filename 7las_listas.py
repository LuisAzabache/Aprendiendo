#LISTAS - sintaxis
#nos permite almacenar un grupo de valores adiferencia de las variables que almacena solo un valor

#sintaxis:
#nombrelista=[element1, element2, element3...]
#      indice   0          1         2     ...

milista=["Maria", "Pepe", "Martha", "Antonio"]

print(milista[:])   #imprime todos los elementos de la lista

print(milista[2])   #imprime el indice 2 de la lista que es Martha

print(milista[0])   #acordarse que el primer elemento es de indice 0


#cuando la lista es demasiada larga se puede acceder a una PORCION de lista:

print(milista[0:3])  #accede a los 3 primeros indices    desde el 0 excluyendo al indice 3
#imprime [Maria, Pepe, Martha]
print(milista[:3])   #incluso se puede obviar escribir el 0
#imprime [Maria, Pepe, Martha]
print(milista[1:2])  #incluye indice1 = Pepe y excluye indice2=Martha
#imprime [Pepe]

#se puede agregar mas elementos al final de la lista:
milista.append("Carlos")
print(milista[:])
#imprime ['Maria', 'Pepe', 'Martha', 'Antonio', 'Carlos']

milista.insert(2,"Carlos")   #insert pide incluir el indice y el elemento
print(milista[:])
#se imprime ['Maria', 'Pepe', 'Carlos', 'Martha', 'Antonio', 'Carlos']

#se puede agregar unalista a la existente:
milista.extend(["Paty", "Ana", "Jorge"])  #se agrega los elementos dentro de corchetes
print(milista[:])
#se imprime ['Maria', 'Pepe', 'Carlos', 'Martha', 'Antonio', 'Carlos', 'Paty', 'Ana', 'Jorge']

#para consultar en que indice se encuentra un elemento se usa la funcion index
print(milista.index("Antonio"))
#esto me imprime 4          debido a que Antonio se encuentra en el indice 4

#si necesito saber si un elemento se encuetra en mi lista se usa la funcion "in"
print("Pepe" in milista)
#Imprime True si es cierto y False si no esta en la lista

miLista=["Maria", 5, True, 38.45]      #la lista puede contener distintos tipos de elementos
print(miLista[3])
#Imprime el elemento 38.45

Milista=["Maria", 5, True, 38.45]
Milista.extend(["Javier", "Nicolasa", "Andrea"])
Milista.remove("Nicolasa")
print(Milista[:])
#queda impreso ['Maria', 5, True, 38.45, 'Javier', 'Andrea']

#Para eliminar el ultimo elemento de una lista se usa la funcion "pop"
Milista=["Maria", 5, True, 38.45]
Milista.pop()
print(Milista[:])
#se imprime ['Maria', 5, True]

#Para unir dos listas declaradas diferentes:
milista1=["Ana", "Maria", "Jorge", 58, False, 15.12]
milista2=["gatitos", "perritos", 135, True]
milista3=milista1+milista2
print(milista3[:])
#imprime ['Ana', 'Maria', 'Jorge', 58, False, 15.12, 'gatitos', 'perritos', 135, True]
milista1=["Ana", "Maria", "Jorge", 58, False, 15.12]*3     #este operados repite la lista 3 veces en lamisma linea
print(milista1[:])
#imprime ['Ana', 'Maria', 'Jorge', 58, False, 15.12, 'Ana', 'Maria', 'Jorge', 58, False, 15.12, 'Ana', 'Maria', 'Jorge', 58, False, 15.12]
