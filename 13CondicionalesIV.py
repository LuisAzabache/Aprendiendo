##########################################   CONDICIONALES IV  #########################################################
#Se creara un programa si el alumno que entra a un colegio tiene derecho a beca o no

print("############# P R O G R A M A   D E    B E C A S    2 0 1 9  #######################")

distancia_escuela=float(input("Introduce la distancia a la escuela en kilometros:  "))
print("Distancia a la escuela es de " + str(distancia_escuela) + " kilometros")

numero_hermanos=int(input("Introduce el numero de hermanos del alumno:  "))
print("Tiene " + str(numero_hermanos) + " hermanos")

salario_familial=float(input("Introduce el monto de salario familial: "))
print("El salario familial es de " + str(salario_familial) + " soles")

if distancia_escuela>40 and numero_hermanos>2 and salario_familial<2000:
    print("############################  EL ALUMNO OBTIEN BECA  #################################")
else:
    print("##########################  EL ALUMNO NO OBTIENE BECA  ###############################")
#imprime
############# P R O G R A M A   D E    B E C A S    2 0 1 9  #######################
#Introduce la distancia a la escuela en kilometros:  51651
#Distancia a la escuela es de 51651.0 kilometros
#Introduce el numero de hermanos del alumno:  516
#Tiene 516 hermanos
#Introduce el monto de salario familial: 5616
#El salario familial es de 5616.0 soles
##########################  EL ALUMNO NO OBTIENE BECA  ###############################


###################################################################################################################


print("############# P R O G R A M A   D E    B E C A S    2 0 1 9  #######################")

distancia_escuela=float(input("Introduce la distancia a la escuela en kilometros:  "))
print("Distancia a la escuela es de " + str(distancia_escuela) + " kilometros")

numero_hermanos=int(input("Introduce el numero de hermanos del alumno:  "))
print("Tiene " + str(numero_hermanos) + " hermanos")

salario_familial=float(input("Introduce el monto de salario familial: "))
print("El salario familial es de " + str(salario_familial) + " soles")

if distancia_escuela>40 and numero_hermanos>2 or salario_familial<2000:    #o si nada de lo anterior se cumple (el "or" tiene mayor peso)
    print("############################  EL ALUMNO OBTIENE BECA  #################################")
else:
    print("##########################  EL ALUMNO NO OBTIENE BECA  ###############################")
#imprime
############# P R O G R A M A   D E    B E C A S    2 0 1 9  #######################
#Introduce la distancia a la escuela en kilometros:  2
#Distancia a la escuela es de 2.0 kilometros
#Introduce el numero de hermanos del alumno:  0
#Tiene 0 hermanos
#Introduce el monto de salario familial: 500
#El salario familial es de 500.0 soles
############################  EL ALUMNO OBTIEN BECA  #################################




#ejemplo con asignaturas a escoger

print("ASIGNATURAS OPTATIVAS ANIO 2019")
print("Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

asignatura=input("Escriba la asignatura escogida:  ")

if asignatura in ("Informatica grafica", "Pruebas de software", "Usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("La asignatura escogida no esta contemplada")

#Imprime
#ASIGNATURAS OPTATIVAS ANIO 2019
#Informatica grafica - Pruebas de software - Usabilidad y accesibilidad
#Escriba la asignatura escogida:  Algebra
#La asignatura escogida no esta contemplada


#puede que se de que al momento de ingresar la asignatura a asignarse se escriba con minuscula o mayusculay sea distindo a lo declarado en el programa.
#paraesto se puede usar las funciones "lower" o "upper" transforma elvalor a mayuscula o minuscula
print("ASIGNATURAS OPTATIVAS ANIO 2019")
print("Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

opcion=input("Escriba la asignatura escogida:  ")
asignatura=opcion.lower()

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("La asignatura escogida no esta contemplada")
#IMPRIME
#ASIGNATURAS OPTATIVAS ANIO 2019
#Informatica grafica - Pruebas de software - Usabilidad y accesibilidad
#Escriba la asignatura escogida:  PRUEBAS DE SOFTWARE
#Asignatura elegida: pruebas de software