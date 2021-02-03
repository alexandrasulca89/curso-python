mensaje="""
hola ,ingrese las siguientes opciones:
cuadrado=1
rectangulo=2
"""
print(mensaje)
opcion=int(input("ingrese la opcion elegida: "))


if opcion==1:
   lon= int(input("ingrese la longitud: "))
   ancho=int(input("ingrese el ancho: "))
   area=lon*ancho
   print(f"el area de cuadrado es:{area}")
elif opcion==2:
    lon= int(input("ingrese la longitud: "))
    ancho=int(input("ingrese el ancho: "))
    perimetro=(2*lon)+(2*ancho)
    print(f"el perimetro del rectangulo es: {perimetro}")
else:
    print("escoja una opcion valida")



