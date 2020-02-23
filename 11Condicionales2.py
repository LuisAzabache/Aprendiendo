##### CONSTRUCCION ES  "ELSE" "ELIF"

print("Verificacion de Acceso")

edad_usuario=int(input("introduce tu edad por favor:    "))
if edad_usuario<18:
    print("No puedes pasar")
else:
    print("Puedes pasar")
print("El programa ha finalizado")
#imprime    Verificacion de Acceso
#           introduce tu edad por favor:    18
#           Puedes pasar
#           El programa ha finalizado



#el "else" funciona leyendo al if msa cercano, en caso se quiera declarar mas condicionales se usa "ELIF"
print("Verificacion de Acceso")

edad_usuario=int(input("introduce tu edad por favor:    "))
if edad_usuario<18:
    print("No puedes pasar")
elif edad_usuario>100:               #Elif para añadir otra condicional
    print("Edad incorrecta")
else:
    print("Puedes pasar")
print("El programa ha finalizado")



#ejemplo con notas
print("Verificacion de Notas")

nota_usuario=float(input("introduce tu nota por favor:    "))
if edad_usuario<=5:
    print("Insuficiente")
elif edad_usuario>8:
    print("sobresaliente")
else:
    print("Suficiente")
print("El programa ha finalizado")



#para darle mas opciones de respuesta se agrega mas condicionales con "elif"
print("Verificacion de Notas")

nota_usuario=float(input("introduce tu nota por favor:    "))
if nota_usuario<=5:
    print("Insuficiente")
elif nota_usuario<6:
    print("Suficiente")
elif nota_usuario<7:
    print("Bien")
elif nota_usuario<9:
    print("Notable")
else:
    print("sobresaleinte")
print("El programa ha finalizado")