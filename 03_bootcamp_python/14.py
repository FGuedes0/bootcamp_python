# Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

limite = 10
tentativa = 1
while tentativa <= limite:
    print(f"tentando reconexão, tentativa {tentativa} de {limite}")
    #if True:
    #   print("Conexão bem sucedida")
    #    break
    tentativa +=1
#else:
    if tentativa > limite:
        print("Falha de conexão, número máximo de tentativas excedido")