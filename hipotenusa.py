import math

def distancia(x1,y1,x2,y2):
	total=math.sqrt((x2-x1)**2+(y2+y1)**2)
	return total

x1=int(input("Valor de x1: "))
x2=int(input("Valor de x2: "))
y1=int(input("Valor de y1: "))
y2=int(input("Valor de x2: "))
print ("El valor de la hipotenusa es: ",distancia(x1,y1,x2,y2))
