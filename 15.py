def numero_palindromo(n):
    s = str(n)
    return s == s[::-1]
print(numero_palindromo(121))  
print(numero_palindromo(123))  