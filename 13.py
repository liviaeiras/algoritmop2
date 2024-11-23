def soma_lista(lista):
    return sum(soma_lista(x) if isinstance(x, list) else x for x in lista)
print(soma_lista([1, [2, 3], 4]))  
