def intersecao_listas(lista1, lista2):
    return list(set(lista1) & set(lista2))
print(intersecao_listas([1, 2, 3], [2, 3, 4]))  
