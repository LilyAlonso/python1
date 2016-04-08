num=int(input("¿Cuantos numeros quieres en tu lista?: "))
lista=[]
for n in range(0,num):
    n = int(input("Dame un numero para tu lista: "))
    lista.append(n)

def find_threes():
    newlist=[]
    for x in lista:
        res=x%3
        if res==0:
            newlist.append(x)
            suma=sum(newlist)
    return suma

print("La suma de los numeros de tu lista divisibles por 3 es: ",find_threes())
