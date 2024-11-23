def subconjuntos(lista):
    if not lista:
        return [[]]
    resto = subconjuntos(lista[1:])
    return resto + [[lista[0]] + subset for subset in resto]
print(subconjuntos([1, 2])) 
