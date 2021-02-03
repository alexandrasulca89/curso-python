nro_mes=int(input("ingrese el numero del mes: "))
if nro_mes>=1 and nro_mes<=3:
    print("Se encuentra en el primer trimestre")
elif nro_mes>=4 and nro_mes<=6:
    print("Se encuentra en el segundo trimestre")
elif nro_mes>=7 and nro_mes<=9:
    print("Se encuentra en el tercer trimestre")
elif nro_mes>=10 and nro_mes<=12:
    print("Se encuentra en el cuarto trimestre")
else:
    print("ingrese un numero dentro del rango de 1 a 12.intentelo nuevamente")
