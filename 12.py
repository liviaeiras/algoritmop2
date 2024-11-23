def frequencia_palavras(lista):
    return {palavra.lower(): lista.count(palavra) for palavra in set(map(str.lower, lista))}
print(frequencia_palavras(["batata", "batata", "queijo", "queijo", "queijo"]))  

