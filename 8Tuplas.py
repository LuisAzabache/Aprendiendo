#TUPLAS####################################
#son listas INMUTABLES
#se ejecuta mas rapido que las listas
#SINTAXIS:
#nombretupla=(elemen1, elemen2, elemen3...)    Van solo entre parentesis en comparacion con las listas que iban en corchetes

mitupla=("Juan", 5, True, 12.7)
print(mitupla[2])
#imprime True


#se puede convertir tuplas en listas con la funcion "list()"
milista=list(mitupla)
print(milista)
#imprimne ['Juan', 5, True, 12.7]     <--- imprime entre corchetes las listas

print(mitupla)
#imprime ('Juan', 5, True, 12.7)   <---- imprime en parentesis las tuplas


#Tambien se puede convertir listas en tuplas con a funcion "tuple()"
milista2=["Javier", 2, False]
print(milista2[:])
#imprime ['Javier', 2, False]   <---- entre corchetes por ser una lista

mitupla2=tuple(milista2)
print(mitupla2[:])
#imprime ('Javier', 2, False)    <-----entre parentesis por ser una tupla

print("JAvier" in mitupla2)   #usando la funcion "in" se puede consultar si un elemento se encuentra dentro de la tupla
#imprime False debido a que escrib[i JAvier con la a mayuscula y debio coincidir con el elemento real

#para averiguar cuantos elementos se encuentran dentro de una tupla usand la funcion "count"
milista2=["Javier", 2, False]
mitupla2=tuple(milista2)
print(mitupla2.count("Javier"))  #aqui se usa el metodo count para averiguar cuantas veces est[a presente el elemento Javier
#imprime 1

#Para averiguar la longitud de la tupla se usa el metodo "len"
milista3=["Javier", 2, False, True, "Angie", 35578.2]
mitupla3=tuple(milista3)
print(len(mitupla3))      #aqui se uso el metodo "len"
#imprime 3 debido a que la longitud de la tupla es de 3 elementos


#existen tuplas unitarias
mitupla4=("Anibal",)        #es importante que tras el primer elemento vaya una coma
print(len(mitupla4))
#imprime 1  por ser una lista unitaria efecivamente


#  DESEMPAQUETADO DE TUPLAS
mitupla=("Juan", 15, 1, 1995)
nombre, dia, mes, agno=mitupla           #aqui almaceno dentro de las variables un valor correspondiente dentro de la tupla
print(nombre)
#imprime Juan ya que se pidio imprimir la variable nombre que se le asigno como Juan

print(nombre)
print(dia)
print(mes)
print(agno)
#imrpime:
#Juan
#15
#1
#1995

print(mitupla.index("Juan"))
#imprime 0 debido a que Juan pertenece al indice 0