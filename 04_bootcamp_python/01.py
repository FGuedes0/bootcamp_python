# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado
lista : list = []

for i in range(1, 11):
    lista.append(i)
    #print(lista)
    
for i in lista:
    print(i ** 2)