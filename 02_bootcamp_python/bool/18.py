#Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#booleano = bool(input("Insira a expressão booleana: "))
#resultado = not booleano
#print(resultado)

#O python considera qualquer input como true, o programa só retorna false. Algo assim funcionaria um pouco melhor:
def v_ou_f():
    v_ou_f = str(input("Insira a expressão booleana: "))
    if v_ou_f == "True":
        return print("False") 
    else:
        return print("True")
    
v_ou_f()