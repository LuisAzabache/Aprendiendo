#FUNCIONES II

def suma():
    num1=5
    num2=7
    print(num1+num2)

suma()   #se llama la funcion cuantas veces quiera


def suma(num1,num2):   #en esta funcion damos parametros a ser reemplazados en el futuro
    print(num1+num2)

suma(5,7)

suma(8,7)

suma(-14,85)


#funciones quedevuelven un valor con instruccion return

def suma(num1,num2):
    resultado=num1+num2
    return resultado
print(suma(11,24))

print (suma(1,8))

print (suma(50,-4))

#imprime en consola los 3 resultados llamando a la funcion suma


almacena_resultado=suma(5,10)    #le asigne a una variable la funcion suma
print (almacena_resultado)       #imprime en consola la variable con valor funcion suma






