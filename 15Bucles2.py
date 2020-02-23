#############################################  BUCLES II  #############################################################


for i in ["pildoras","informaticas",3]:

    print("hola", end="")  #<--- argumento "end=""" se le dice que finalice la impresion sin salto de linea
#Imprime_
#holaholahola

#el mismo ejemplo anterior pero dejando una separacion entre cada "hola"
for i in ["pildoras","informaticas",3]:

    print("hola", end=" ")  #se le agrega espacio en blanco en el interior de las comillas para dar separacion a cada "hola"
#Imprime:
#hola hola hola


for i in "ing.azabache@gmail.com":                  #<-----  imprimirá tantos caracteres tenga"ing.azabache@gmail.com"
    print("hola", end=" ")
#Imprinme:
#hola hola hola hola hola hola hola hola hola hola hola hola hola hola hola hola hola hola hola hola hola hola         #imprimio 22 como el numero de caracteres



#evaluando si un email es correcto o no en funcion a la presencia del @

email=False

for i in "ing.azabache@gmail.com":
    if(i=="@"):
        email=True
if email==True:
    print("El email es correcto")
else:
    print("El email es incorrecto")


#haciendo que te pida correos electronicos para evaluar si son correctas:

email=False

mi_email=input("Introduce tu correo electronico:   ")

for i in mi_email:
    if(i=="@" and i=="hotmail" and i=="."):
        mi_email=True
if mi_email==True:
    print("Direccion electronica correcta")
else:
    print("Direccion electronica incorrecta")
#Al imprimir pide en orden estricto el "@" el "hotmail" y luego el "."



#otra manera de efectuarlo seria:
contador=0

mi_email=input("Ingresa tu cuenta de correo:  ")
for i in mi_email:
    if (i=="@" or i=="."):
        contador==contador + 1
if contador==2:
    print("Su Correo es correcto")
else:
    print("Su correo es incorrecto")

