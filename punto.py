num_lista1=int(input("¿Cuantos numeros quieres en tu primera lista? "))
num_lista2=int(input("¿Cuantos numeros quieres en tu segunda lista? "))
lista1=[]
lista2=[]
vector=[]
for n in range(num_lista1):#se van a agregar los numeros a la lista1
    num=int(input("Dame el numero de la lista 1: "))
    lista1.append(num)

for n in range(num_lista2):#va agregar los numeros a la lista2
    num2=int(input("Dame el numero de la lista 2: "))
    lista2.append(num2)

def dot_product():
    if len(lista1)==len(lista2):
        for n in range(num_lista1):#multiplica elemento por elemento
            vector.append(lista1[n]*lista2[n])#multiplica las listas y las agrega a la lista vector
            result=sum(vector)#suma los elementos del vector resultante
        return result
    else:
        return float("NaN")#no hay elementos suficientes para realizar el producto punto

print("El producto punto de ", lista1, " y ", lista2, " es: ", dot_product())
