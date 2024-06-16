#Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".

try:
    n1 = float(input("Digite um número: "))
    if  n1 % 2 == 0:
        resto = "par"
    else:
        resto = "impar"

    if n1 < 0:
        maior_menor_zero = "menor do que 0"
    elif n1 > 0:
        maior_menor_zero = "maior do que 0"
    else:
        maior_menor_zero = "o número é 0"
    print(f"""o número {n1:.0f} é {resto} e é {maior_menor_zero}""")

except ValueError:
    print("a entrada fornecida deve ser um número")