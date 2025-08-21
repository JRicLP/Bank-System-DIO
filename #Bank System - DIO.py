#Bank System - DIO

menu = """

Seja bem-vindo ao Sistema de Transações Bancárias, selecione uma
opção para prosseguir:

=> [D] Depositar
=> [S] Sacar
=> [E] Extrato
=> [B] Sair

"""

#Variáveis e Constantes do Sistema

saldo = 0
limite_saque = 500
extrato = ""
saques_realizados = 0
LIMITE_SAQUES = 3

while True:

    opcao_usuario = input(menu).upper()

    if opcao_usuario == "D":
        print("Sistema de Depósito")
        valor_depositado = float(input("Digite o valor que você deseja depositar:"))
        if valor_depositado >= 0:
            saldo += valor_depositado
            print("Saldo atual = {}".format(saldo))
            extrato += f"Depósito: R${valor_depositado:.2f}"
        else:
            print("Não é possível depositar valores negativos.")    

    elif opcao_usuario == "S":
        print("Sistema de Saque")
        valor_sacado = float(input("Digite o valor que você deseja sacar [Limitado a 500R$]: "))
        if saques_realizados <= LIMITE_SAQUES:
            if valor_sacado > saldo:
                print("Você não possui saldo suficiente para realizar esta operação")
            elif 0 <= valor_sacado <= saldo:
                saldo -= valor_sacado
                print("Operação realizada com sucesso.")
                print("Você retirou: {:.2f}R$ | Saldo atual: {:.2f}R$".format(valor_sacado, saldo))
                saques_realizados += 1
                extrato += f"Saque: R${valor_sacado:.2f}"
        else:
            print("Você atingiu o limite de saques diários. [{}]".format(LIMITE_SAQUES))           

    elif opcao_usuario == "E":
        print("Exibição do Extrato:")
        print("======> Operações realizadas <======")
        if not extrato:
            print("Não foram realizadas operações")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo}")
        print("====================================")



    elif opcao_usuario == "B":
        break

    else:
        print("Opção Inválida, tente novamente.")    

