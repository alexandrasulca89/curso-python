#escribimos el tipo de cambio
#tipo_cambio=0.27
#monto=input("ingrese el monto en soles:")
#mont_usd= float(monto)*tipo_cambio

#print(f"el monto en dolares es:{mont_usd}")

#mensaje = """
#HOLA,este es un conversor de moneda
#ingrese cualquiera de estas 3 opciones
#1=soles-dolares
#2=euros-dolares
#3=cop-dolares
#"""
#print(mensaje)
#opcion = int(input("Ingrese su opcion"))
#if opcion ==1 :
#    monto=input("ingrese el monto en soles:")
#    mont_usd= round(float(monto)*0.27,2)
#    print(f"el monto en dolares es:{mont_usd}")
#elif opcion==2:
#    monto=input("ingrese el monto en euros:")
#    mont_euros= round(float(monto)*1.21,2)
#    print(f"el monto en dolares es:{mont_euros}")
#elif opcion==3:
#    monto=input("ingrese el monto en cop:")
#    mont_cop= round(float(monto)*0.00028,2)
#    print(f"el monto en dolares es:{mont_cop}")
#else:
#    print("ingrese una opcion valida")

def convertir_moneda(tipo_cambio,moneda):
     monto=input(f"ingrese el monto en {moneda}:")
     mont_usd= round(float(monto)*tipo_cambio,2)
     print(f"el monto en dolares es:{mont_usd}")
    

mensaje = """
HOLA,este es un conversor de moneda
ingrese cualquiera de estas 3 opciones
1=soles-dolares
2=euros-dolares
3=cop-dolares
"""
print(mensaje)
opcion=int(input("ingrese la opcion:"))
if opcion ==1 :
    convertir_moneda(0.27,"soles")
elif opcion==2:
    convertir_moneda(1.21,"euros")
elif opcion==3:
    convertir_moneda(0.00028,"cop")
else:
    print("ingrese una opcion valida")

