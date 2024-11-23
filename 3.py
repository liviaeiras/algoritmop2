def rotacionar_lista(lista, k):
    k = k % len(lista)
    return lista[-k:] + lista[:-k]
print(rotacionar_lista([1, 2, 3, 4, 5], 2))  
