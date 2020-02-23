############## CONDICIONALES I ###################################
#Practica "IF"

def evaluacion1(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion
print(evaluacion1(4))
#imprime  suspenso


#para que la funcion nos de resultado al ingresar un valor mediante teclado - Se usa "input"

print("Programa de Evaluacion de Notas de Alumno")

nota_alumno=input("Introduce la nota del alumno:")

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion
print(evaluacion(float(nota_alumno)))   #se tiene que especificar que el valor que se dará tiene que ser considerado como numero decimal con "float

