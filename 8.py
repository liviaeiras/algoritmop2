def eh_palindromo(s):
    return s == s[::-1]

def contar_palindromos(lista):
    return sum(eh_palindromo(s) for s in lista)
print(contar_palindromos(["anna", "banana", "arara", "ovo"]))  
