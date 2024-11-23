def combinacoes(lista, r):
    if r == 0:
        return [[]]
    if not lista:
        return []
    return [[lista[0]] + c for c in combinacoes(lista[1:], r - 1)] + combinacoes(lista[1:], r)
print(combinacoes([1, 2, 3], 2))  
