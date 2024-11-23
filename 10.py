def elementos_duplicados(lista):
    return list({x for x in lista if lista.count(x) > 1})
print(elementos_duplicados([1, 2, 2, 3, 4, 4, 5]))
