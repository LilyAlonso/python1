import math
lista = []
for n in range (0,10):
    n = int(input("Dame un numero: "))
    lista.append(n)
print("Tu lista es: ",lista)

def promedio():
    suma = sum(lista)
    cant = len(lista)
    prom = suma / cant
    return prom

def average():
    suma = sum(lista)
    cant = len(lista)
    prom = suma / cant
    x = float(math.sqrt(((suma-prom)**2)/(cant-1)))
    return x

print ("El promedio de la lista es: ",promedio())
print ("La desviacion estandar es: ",average())
