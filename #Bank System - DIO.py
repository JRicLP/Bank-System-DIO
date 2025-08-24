# Bank System - DIO

saldo = 0
extrato = ""
saques_realizados = 0
usuarios = []
contas = []
agencia = ""
numero_conta = 0

LIMITE_VALOR = 500
LIMITE_SAQUES = 3
AGENCIA = "0001"

def menu():

    return """\n
    Seja bem-vindo ao Sistema de Transações Bancárias, selecione uma
    opção para prosseguir:
    =============================================
    => [D] Depositar
    => [S] Sacar
    => [E] Extrato
    => [C] Criar usuario
    => [A] Criar conta
    => [L] Listar contas
    => [B] Sair
    =============================================
    """

def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
        Agência: \t{conta['agencia']}
        Número da Conta: \t{conta['numero_conta']}
        Titular da conta: \t{conta['usuario']['nome']}
        """

        print(linha)

def criar_conta(agencia, numero_conta, usuarios):
    
    cpf = input("Informe o CPF para verificação Pré-Conta:")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso - Você agora possui uma associação Usuário/Conta")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    else:
        print("A conta não pode ser criada devido a uma inconsistência nos seus dados - Processo encerrado")

def filtrar_usuarios(cpf, usuarios):
    
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf ]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_usuario(usuarios):
    
    cpf = input("Digite o seu CPF [Apenas números]:")
    
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("Já existe um usuário com esse CPF")
        return
    
    nome = input("Informe seu nome completo:")
    data_nascimento = input("Informe sua data de nascimento - [Formato dd/mm/aaaa]:")
    endereco = input("Informe seu endereço - [Formato: Logradouro - Num. - Bairro - Cidade/Sigla do Estado]: ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})

    print("Usuário adicionado ao sistema - Sucesso na operação")

def depositar(saldo, extrato, /):
    print("\n=> Sistema de Depósito:")
    valor = float(input("Digite o valor que você deseja depositar: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito realizado com sucesso! Saldo atual = R$ {saldo:.2f}")
    else:
        print("Não é possível depositar valores negativos ou nulos.")

    return saldo, extrato


def sacar(* ,saldo, extrato, saques_realizados, LIMITE_SAQUES, LIMITE_VALOR):
    print("\n=> Sistema de Saque")
    valor = float(input(f"Digite o valor que você deseja sacar [Limite: R$ {LIMITE_VALOR:.2f}]: "))

    if saques_realizados >= LIMITE_SAQUES:
        print(f"Você atingiu o limite de saques diários ({saques_realizados}/{LIMITE_SAQUES}).")

    elif valor > LIMITE_VALOR:
        print(f"O valor máximo por saque é de R$ {LIMITE_VALOR:.2f}.")

    elif valor > saldo:
        print("Você não possui saldo suficiente para realizar esta operação.")

    elif valor > 0:
        saldo -= valor
        saques_realizados += 1
        extrato += f"Saque: R$ {valor:.2f}\n"
        print(f"Saque realizado com sucesso! Você retirou R$ {valor:.2f}. Saldo atual: R$ {saldo:.2f}")

    else:
        print("Valor inválido para saque.")

    return saldo, extrato, saques_realizados


def exibir_extrato(saldo, /, * , extrato):
    print("\n======== Extrato Bancário ========")
    if not extrato:
        print("Não foram realizadas operações.")
    else:
        print(extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("====================================")

while True:
    opcao = input(menu()).upper()

    if opcao == "D":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "S":
        saldo, extrato, saques_realizados = sacar(saldo = saldo, extrato = extrato, saques_realizados = saques_realizados, LIMITE_SAQUES = LIMITE_SAQUES, LIMITE_VALOR = LIMITE_VALOR)

    elif opcao == "E":
        exibir_extrato(saldo, extrato = extrato)

    elif opcao == "C":
        criar_usuario(usuarios)

    elif opcao == "A":

        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif opcao == "L":
        listar_contas(contas)

    elif opcao == "B":
        print("Obrigado por utilizar nosso sistema bancário!")
        print("Encerrando o sistema")
        break

    else:
        print("Opção inválida. Tente novamente.")
