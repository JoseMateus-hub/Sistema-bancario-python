import itertools
import getpass

clientes = []
contas = []
gerador_id = itertools.count(1)


# ===========================
# CLIENTE
# ===========================
def cadastrar_cliente():
    print("\n====== CADASTRO DE CLIENTE ======")
    nome = input("Nome completo: ")
    rg = input("RG: ")
    cpf = input("CPF (login): ")

    if buscar_cliente_por_cpf(cpf):
        print("\nJá existe um cliente com esse CPF!")
        return None

    senha = getpass.getpass("Crie sua senha: ")

    endereco = input("Endereço: ")
    cidade = input("Cidade: ")
    estado = input("Estado (UF): ")

    cliente = {
        "id": next(gerador_id),
        "nome": nome,
        "rg": rg,
        "cpf": cpf,
        "senha": senha,
        "endereco": endereco,
        "cidade": cidade,
        "estado": estado,
    }

    clientes.append(cliente)
    print("\nCliente cadastrado com sucesso!")
    return cliente


def buscar_cliente_por_cpf(cpf):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None


# ===========================
# LOGIN
# ===========================
def login():
    print("\n====== LOGIN ======")
    cpf = input("CPF: ")
    senha = getpass.getpass("Senha: ")

    cliente = buscar_cliente_por_cpf(cpf)

    if not cliente:
        print("\nCliente não encontrado.")
        return None

    if cliente["senha"] != senha:
        print("\nSenha incorreta.")
        return None

    print(f"\nBem-vindo, {cliente['nome']}!")
    return cliente


# ===========================
# CONTA
# ===========================
def criar_conta(cliente):
    print("\n====== CRIAÇÃO DE CONTA ======")

    conta = {
        "agencia": "0001",
        "numero_conta": len(contas) + 1,
        "cliente_id": cliente["id"],
        "tipo": "Conta Corrente",
        "saldo": 0,
        "extrato": "",
        "limite": 500,
        "saques_realizados": 0,
        "LIMITE_SAQUES": 3
    }

    contas.append(conta)

    print("\nConta criada com sucesso!")
    print(f"Agência: {conta['agencia']}")
    print(f"Número: {conta['numero_conta']}")
    return conta


def selecionar_conta(cliente):
    for conta in contas:
        if conta["cliente_id"] == cliente["id"]:
            return conta
    return None


# ===========================
# OPERAÇÕES BANCÁRIAS
# ===========================
def depositar(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado!")
    else:
        print("Valor inválido.")


def sacar(conta, valor):
    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > conta["limite"]
    excedeu_saques = conta["saques_realizados"] >= conta["LIMITE_SAQUES"]

    if excedeu_saldo:
        print("Saldo insuficiente.")
    elif excedeu_limite:
        print("Valor excede o limite.")
    elif excedeu_saques:
        print("Limite de saques atingido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["saques_realizados"] += 1
        print("Saque realizado!")
    else:
        print("Valor inválido.")


def extrato(conta):
    print("\n====== EXTRATO ======")
    print(conta["extrato"] if conta["extrato"] else "Nenhuma movimentação.")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")
    print("======================")


# ===========================
# MENU PRINCIPAL
# ===========================
def main():
    conta_logada = None

    menu_principal = """
====== MENU PRINCIPAL ======
[1] Login
[2] Cadastrar Cliente
[q] Sair
=> """

    menu_conta = """
====== MENU DA CONTA ======
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Nova Conta
[5] Trocar Usuário
[q] Logout
=> """

    while True:
        if not conta_logada:
            opcao = input(menu_principal)

            if opcao == "1":
                cliente = login()
                if cliente:
                    conta_logada = selecionar_conta(cliente)
                    if not conta_logada:
                        print("\nNenhuma conta encontrada. Criando primeira conta:")
                        conta_logada = criar_conta(cliente)

            elif opcao == "2":
                cadastrar_cliente()

            elif opcao == "q":
                print("Saindo do sistema.")
                break

            else:
                print("Opção inválida.")

        else:
            opcao = input(menu_conta)

            if opcao == "1":
                valor = float(input("Valor do depósito: "))
                depositar(conta_logada, valor)

            elif opcao == "2":
                valor = float(input("Valor do saque: "))
                sacar(conta_logada, valor)

            elif opcao == "3":
                extrato(conta_logada)

            elif opcao == "4":
                cpf = input("Seu CPF: ")
                cliente = buscar_cliente_por_cpf(cpf)
                conta_logada = criar_conta(cliente)

            elif opcao == "5":
                conta_logada = None

            elif opcao == "q":
                print("Logout realizado.")
                conta_logada = None

            else:
                print("Opção inválida.")


main()
