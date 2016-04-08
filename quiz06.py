n1=int(input("Numero 1: "))
n2=int(input("Numero 2: "))

def euclid(n1,n2):
    if n1==n2:
        return n2
    else:
        if n1>n2:
            return (euclid(n1-n2,n2))
        else:
            return (euclid(n1,n2-n1))

print ("El maximo comun divisor es: ",euclid(n1,n2))
