x = int(input("Dame un numero para empezar la suma "))
y = int(input("Dame otro numero hasta el cual sumar "))

z = 0
a = x
while a <= y:
    z = a + z
    a = a + 1

print(z)
