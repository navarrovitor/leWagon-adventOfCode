f = open("day8/trees.txt", "r")
f = f.read()

arvores = list(map(lambda x: list(map(lambda y: int(y), list(x))), f.split()))

maiorX = len(arvores[0]) - 1
maiorY = len(arvores) - 1

def adjacentes(x,y):
    return {
        "esquerda": [arvores[y][i] for i in range(0,x)],
        "direita": [arvores[y][i] for i in range(x+1, maiorX + 1)],
        "cima": [arvores[i][x] for i in range(0,y)],
        "baixo": [arvores[i][x] for i in range(y+1, maiorY + 1)],
    }

arvoresVisiveis = maiorX * 2 + maiorY * 2

for y in range(1, maiorY):
    for x in range(1, maiorX):
        atual = arvores[y][x]
        arvoresAdjacentes = adjacentes(x,y)
        
        if len(arvoresAdjacentes["esquerda"]) != 0 and max(arvoresAdjacentes["esquerda"]) < atual:
            arvoresVisiveis += 1
        elif len(arvoresAdjacentes["direita"]) != 0 and max(arvoresAdjacentes["direita"]) < atual:
            arvoresVisiveis += 1
        elif len(arvoresAdjacentes["cima"]) != 0 and max(arvoresAdjacentes["cima"]) < atual:
            arvoresVisiveis += 1
        elif len(arvoresAdjacentes["baixo"]) != 0 and max(arvoresAdjacentes["baixo"]) < atual:
            arvoresVisiveis += 1

print(arvoresVisiveis)