#Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.
numeros = [20, 40, 50, 10, 30]
minimo = min(numeros)
maximo = max(numeros)
normalizados = sorted([(x - minimo) / (maximo - minimo) for x in numeros])

print(normalizados)