repetir=0
resp=1
while repetir==0:
    n= int(input("Numero para saber el factorial: "))
    if n<0:
        print("Elige un numero positivo: ")
        repetir=0
    else:
        repetir=1
        cont=0
        while cont<n:
            cont=cont+1
            resp=cont*resp
print("El factorial de ",n," es: ",resp)
