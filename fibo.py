num=int(input("¿De que numero quieres saber el fibonacci? "))

def fibo(num):
  if num==0:
    return 0
  elif num==1:
    return 1
  else:
      r=fibo(num-1)+fibo(num-2)
      return r

print("El fibonaci de ", num, " es ", fibo(num))
