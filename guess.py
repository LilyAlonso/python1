import random
x = random.randint(0,100)
y = 0
print("El programa le permitirá al usuario adivinar un número entre el 1 y 100")
num = int(input("Escoge un número: "))
while(num!=x):
    y = y + 1
    if(num<x):
        num = int(input("El número es muy bajo, vuelve a intentarlo: "))
    else:
        if(num>x):
            num = int(input("El número es muy alto, vuelve a intentarlo: "))
print("Adivinaste! El número es ", x)
print("Adivinaste el número en ", y, " oportunidades")
