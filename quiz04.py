import math

num=int(input("Dame un numero hasta cual detener el programa: "))
def euler_calc(num):
    cont=0
    acum=0
    for n in range (num+1):
        fact=math.factorial(cont)
        resultado=1/fact
        cont = cont + 1
        acum=acum+resultado
        print(acum)
    return acum

print(euler_calc(num))
