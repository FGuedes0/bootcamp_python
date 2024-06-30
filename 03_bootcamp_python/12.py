# Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.


numero = int(input("Digite um número de 1 a 10: "))
while numero < 1 or numero > 10:
    print("Número inválido")
    numero = int(input("Digite um número de 1 a 10: "))
print(f"Entrada {numero} válda ")