n1 = int(input("Teclea un numero: "))
n2 = int(input("Teclea otro numero: "))

def resta(n1,n2):
    r = n1 - n2
    return r

def mul(n1,n2):
    d = n1 * n2
    return d

def div(n1,n2):
    t = n1 // n2
    return t

def res(n1,n2):
    o = n1 % n2
    return o

print("La resta de los numeros es: ", resta(n1,n2))
print("La multiplicacion de los numeros es: ", mul(n1,n2))
print("La division de los numeros es: ", div(n1,n2))
print("El rresiduo de los numeros es: ", res(n1,n2))
