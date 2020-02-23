#print es una funcion para imprimir en pantalla
print("hello world")
#ctrl+D sirve para duplicar la ultima linea
#todo sirve para anotar cosas que se dejan pospuestas o inconclusas
#ctrl+S sirve para guardar
#ctrl+shift+f10 sirve para correr programa
#alt+shift+C sirve para abrir un cuadro con pequeño historial
#shift+F9 sirve para realizar el DEBUG


############################   INICIO DE CLASES PILDORAS INFORMATICAS   ################################################
#el ; es un caracter que no se utiliza pero sirve para separar dos funciones en una misma linea
print ('hola alumnos'); print ('adios alumnos')
#cabe senalar que tanto las comillas dobles como las simples sirven para indicar que se trata de un texto
mi_nombre= "mi nombre es Luis"
print (mi_nombre)
mi_nombre= "mi nombre es\
 Luis"#aqui se dejo espacio debido a que tras la barra invertida no da espacio
print (mi_nombre)
#la  barra invertida sirve para dar salto a la siguiente linea en caso que el codigo sea muy largo.

#IDENTACION #3
#es hacer una tabulacion para distinuir lo que forma parte de un bloque (bucle, condicionales)
a=0 #acordarse que para declarar variables tanto el simbolo 'igual' como el valor van sin espacio; sino no reconoce
for i in range (5):
    a+=1
    print (a)




#TIPOS, OPERADORES Y VARIABLES #4
#ARITMETICOS: ###################
#suma +
#resta -
#multiplicacion *
#division /
#modulo %    es el resto de una division (10/3=3) sobrando 1 <--- ese seria el resto
#division entera //  devuelve el valor entero de division en numero entero
#exponente **
#comparacion:#####################
#igual que ==
#diferente que !=
#mayor que >
#menor que <
#mayor igual que >=
#menor igual que <=
#LOGICOS:#########################
#AND
#OR
#NOT
#ASIGNACION:######################
#igual =
#incremento +=
#decremento -=
#*=
#/=
#%=
#**=
#//=
#ESPECIALES:######################
#IS
#IS NOT
#IN
#NOT IN

#VARIABLE es un espacio en la memoria RAM del ordenador

mi_nombre="Luis"   #incluso para declarar una variable string es necesaria las comillas
print (mi_nombre)
numero=5
type (numero) #si digitamos type() en consola nos da a detalle de que tipo de variable es (int)

mensaje="""este es un mensaje
con tres saltos
de linea"""  #las triple comillas sirven para realizar saltos de linea en el codigo sin necesidad de la barra invertida
print(mensaje)
numero1=5   #operador de asignacion
numero2=7
if numero1>numero2:    #operador de comparacion tambien pudo haber sido ==
    print("el numero1 es mayor")
else:
    print("el numero2 es mayor")



#FUNCIONES #5
#sINTAXIS:

#def nombre_funcion():
#   Instrucciones de la fucion
#   return (opcional)

#def nombre_funcion(parametros):
#   Instrucciones de la fucion
#   return (opcional)

def mensaje():             #declaracion de la funcion
    print("Estamos aprendiendo pyton")
    print("Estamos aprendiendo pyton")
    print("Estamos aprendiendo pyton")

mensaje()                   #llamada a la funcion con la que en consola se imprime los tres mensajes


