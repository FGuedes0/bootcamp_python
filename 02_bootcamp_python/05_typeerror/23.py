#Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas.
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try:
    n1 = float(input("digite o primeiro númmero: "))
except:
    print("A entrada fornecida precisa ser um número")
    exit()

try:
    n2 = float(input("digite o segundo númmero: "))
except:
    print("A entrada fornecida precisa ser um número")
    exit()

op = input(f"""
digite o operador:
[1] + Soma
[2] - Subtração
[3] * Multiplicação
[4] / Divisão
""")

match op:
    case "1":
        print(n1 + n2)
    case "2":
        print(n1 - n2)
    case "3":
        print(n1 * n2)
    case "4":
        try:
            print(n1 / n2)
        except ZeroDivisionError:
            print("não é possível dividir por 0")
    case _:
            print("O operador selecionado não é válido")
        