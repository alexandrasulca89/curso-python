print("por favor ingrese el lado del cuadrado")
lado = input()
#area = float(lado)**2 es igual a lo de abajo, el round lo coloco para redondear y el 2 es el numero ...
# de decimales que quiero,el pow es para hacer potencias
area = round(pow(float(lado),2),2)
print ("el area del cuadrado es :"+str(area))
