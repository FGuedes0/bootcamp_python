#digite nome

#digite salário

#digite % do bonus

#calcular valor bonus - 1000 + salário + bonus

cont_bonus = 1000

nome = input("Digite o nome: ")
salario = float(input("Digite o salário: "))
bonus = float(input("Digite a porcentagem do bonus: "))

valor_bonus = cont_bonus + salario + ((salario * bonus)/100)

#fiz antes de ver o exemplo rs
#print("O salário do usuário", nome, "é de:",salario,", o  valor do bonus do usuário", nome, "é igual a:", valor_bonus)

print(f"O salário do usuário {nome} é de: {salario}, O  valor do bonus do usuário {nome} é igual a: {valor_bonus}")
