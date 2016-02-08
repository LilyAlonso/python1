print("El programa mostrará la temperatura de grados Fahrenheit a Celsius")
f = int(input("Ingresa la temperatura en grados Fahrenheit: "))
c = 5 * (f - 32)/9
print("Una temperatura de ", f, " Fahrenheit equivale a ", c, " grados Celsius")
if(c >= 100):
    print("El agua hierve a esta temperatura")
else:
    print("El agua no hierve a esta temperatura")
