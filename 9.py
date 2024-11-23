def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova {origem} -> {destino}")
    else:
        torre_hanoi(n - 1, origem, auxiliar, destino)
        print(f"Mova {origem} -> {destino}")
        torre_hanoi(n - 1, auxiliar, destino, origem)
torre_hanoi(3, "A", "C", "B")  

