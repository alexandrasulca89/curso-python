opcion=int(input("ingrese una opcion:"))

def mensaje(nro):
    msj =f"""
    Hola!
    Como estas?
    La opcion que elegiste es {nro}
    Adios!"""
    
    print(msj )

if opcion==1:
    mensaje(1)
elif opcion==2:
    mensaje(2)
elif opcion==3:
    mensaje(3)
elif opcion==4:
    mensaje(4)
else :
    print("opcion incorrecta")

    


