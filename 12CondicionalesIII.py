###########  CONDICIONALES III   #########################################################
# Concatenadores de operadores de comparacion
#operadores logicos  "and" y "or"
#operador "in"

edad=-7
if 0<edad<100:    #concatenacion de operadores
    print("La edad es correcta")
else:
    print("Edad incorrecta")
#imprime Es incorrecta


############################################################################################

salario_presidente=int(input("Introduce salario presidente: "))
print("salario presidente:  " + str(salario_presidente))   #utilizacion de funcion "str" (que convierte el valor en string

salario_director=int(input("Introduce salario director: "))
print("salario director:  " + str(salario_director))

salario_jefe_area=int(input("Introduce salario jefe de area: "))
print("salario jefe_area:  " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario administrativo: "))
print("salario administrativo:  " + str(salario_administrativo))


if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo huele mal")

#Imprime lo siguinet:
#Introduce salario presidente:  5000
#salario presidente:  5000
#Introduce salario director:  3500
#salario director:  3500
#Introduce salario jefe de area:  25000   <-----  aqui el jefe de area gana mas que su director y no se cumple las condiciones concatenadas
#salario jefe_area:  25000
#Introduce salario administrativo:  150
#salario administrativo:  150
#Algo huele mal

