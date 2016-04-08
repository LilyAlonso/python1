word=input("¿Que palabra quieres buscar?: ")

def findword():
    cont=0
    archivo = open("palabras.txt", "r")
    cantidad = 0
    for line in archivo:
        minusculas = line.lower()
        sub=minusculas.find(word)
        while sub != -1:
            cont=cont+1
            sub =minusculas.find(word, (sub+1))
    archivo.close()
    return cont

final=findword()
print ("La palabra se repitio ", final, " veces")
