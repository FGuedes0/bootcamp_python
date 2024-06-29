#Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
# Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

try:
    idade = int(input("Digite sua idade: "))
    email = str(input("Digite seu e-mail: "))
    if (idade < 18 and idade > 65):
        print("Idade fora do intervalo permitido")
    elif "@" not in email:
        print("E-mail sem arroba")
    else:
        print("Dados inválidos")
except ValueError:
    print("A idade precisa ser númerica")
finally:
    print("Fim do programa")