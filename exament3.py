
def imprimir(mat):
    for f in mat:
        print(f)
    print()


def validar(lab, f, c, res):
    if f < 0 or f >= len(lab):
        return False
    if c < 0 or c >= len(lab[0]):
        return False
    if lab[f][c] == 0:
        return False
    if res[f][c] == 1:
        return False
    return True


def laberinto(lab, res, f, c, vidas):


    if not validar(lab, f, c, res):
        return False

    if vidas <= 0:
        return False

    valor = lab[f][c]

    if valor == -1:
        vidas -= 1
    elif valor == -2:
        vidas -= 2

    if vidas <= 0:
        return False

    if f == 0 and c == 0:
        res[f][c] = 1
        imprimir(res)
        print(f"Vidas restantes: {vidas}")
        return True

    if validar(lab, f, c, res):

        res[f][c] = 1
        imprimir(res)
        print(f"Vidas restantes: {vidas}")

        # Abajo
        if laberinto(lab, res, f + 1, c, vidas):
            return True

        # Derecha
        elif laberinto(lab, res, f, c + 1, vidas):
            return True

        # Arriba
        elif laberinto(lab, res, f - 1, c, vidas):
            return True

        # Izquierda
        elif laberinto(lab, res, f, c - 1, vidas):
            return True

        else:
            res[f][c] = 0
            return False

    return False


lab = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [-2, 0, 0, -1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, -1, 0, 0, 0, -1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0],
    [-1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, -1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, -1, 1, 1, 1, 0, 1, 1]
]

res = [[0 for _ in range(9)] for _ in range(9)]

print("LABERINTO ORIGINAL")
for fila in lab:
    print(fila)

print("\nBuscando salida...\n")

if laberinto(lab, res, 8, 0, 3):
    print("SALIO DEL LABERINTO")
    print("CAMINO ENCONTRADO:")
    imprimir(res)
else:
    print("NO SE PUDO SALIR DEL LABERINTO")