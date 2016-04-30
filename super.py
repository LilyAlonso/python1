a=int(input("Dame el numero de la base: "))
b=int(input("Dame el numero de la potencia a elevar: "))

def potencia():
	if b==0:
		return 1
	else:
	  x=1
	  y=a
	  while x<b:
	    y=y*a
	    x=x+1
	  return y

print("El resultado es: ", potencia())
