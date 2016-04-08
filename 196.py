mini=int(input("Numero con el que deseas iniciar la secuencia: "))
maxi=int(input("Numero con el que deseas terminar la secuencia: "))
lista=list(range(mini,maxi+1))

for n in lista:
    reversa=int(str(n)[::-1])
    suma=reversa+n
    rev_sum=int(str(suma)[::-1])
    if n==reversa:
        print(n, " es un palindromo")
    elif suma==rev_sum:
        print(n, " no es un numero lychrel")
    else:
        print(n, " es un numero lychrel") 
