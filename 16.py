def potencia(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / potencia(x, -n)
    return x * potencia(x, n - 1)
print(potencia(5, 3))   
print(potencia(2, -3))  
print(potencia(9, 0))   

