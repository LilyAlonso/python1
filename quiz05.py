x = input("Palabra: ")
def is_palindrome(x):
    y = x[::-1]
    if (x==y):
        return x, "Es un palindromo"
    else:
        return x, "No es un palindromo"

print(is_palindrome(x))
