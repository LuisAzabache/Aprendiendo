#solucion de ejercicio 1

numero_1=float(input("Introduce el primer numero:   "))
numero_2=float(input("Introduce el segundo numero:  "))

def devuelve_max(n1,n2):
    if n1>n2:
        print(n1)
    elif n2>n1:
        print(n2)
    else:
        print("son iguales")
print("el numero mas alto es:    ")

devuelve_max(numero_1, numero_2)





#solucion de ejercicio 2
nombre=(input("Introduce nombre:  "))
direccion=(input("Introduce direccion:    "))
telefono=(input("Introduce telefono:    "))

midiccionario={"Nombre":nombre, "Direccion":direccion,"Telefono":telefono}
print("Los personales son:    ")
print(midiccionario["Nombre"])
print(midiccionario["Direccion"])
print(midiccionario["Telefono"])




#solucion del tercer ejercicio:
num1=float(input("Registra el primer numero:    "))
num2=float(input("Registra el segundo numero:    "))
num3=float(input("Registra el tercer numero:    "))

def media_aritmetica(n1, n2, n3):
    media=(n1+n2+n3)/3
    return(media)
print("La media aritmetica es:   ")
print(media_aritmetica(num1,num2,num3))