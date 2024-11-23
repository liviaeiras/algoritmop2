def numeros_primos(lista):
    return [num for num in lista if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
print(numeros_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  


