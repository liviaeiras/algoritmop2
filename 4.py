def soma_digitos(n):
    if n < 10:
        return n
    return n % 10 + soma_digitos(n // 10)
print(soma_digitos(123))  
print(soma_digitos(9))    
