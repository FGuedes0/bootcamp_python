#programa que recebe 2 inputs e retorna a soma
try:
    n1 = int(input("Digite o primeiro número a ser somado: "))

except ValueError:
    print("O valor digitado deve ser um número")
    exit()
except KeyboardInterrupt:
    print("Parece que você não quer digitar um número")
    exit()
try:
    n2 = int(input("Digite o segundo número a ser somado: "))
except ValueError:
    print("O valor digitado deve ser um número")
    exit()
except KeyboardInterrupt:
    print("Parece que você não quer digitar um número")
    exit()

print(n1+n2)