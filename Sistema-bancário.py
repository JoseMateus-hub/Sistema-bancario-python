import itertools
import getpass
from datetime import datetime

clientes = []
contas = []
gerador_id = itertools.count(1)


# ==============================
# DECORADOR DE LOG (NOVO)
# ==============================
def log_transacao(func):
    def wrapper(*args, **kwargs):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        resultado = func(*args, **kwargs)

        texto_log = (
            f"{data_hora} | "
            f"Função: {func.__name__} | "
            f"Args: {args} | "
            f"Kwargs: {kwargs} | "
            f"Retorno: {resultado}\n"
        )

        with open("log.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(texto_log)

        return resultado

    return wrapper


# ==============================
# GERADOR DE RELATÓRIOS
# ==============================
def gerador_transacoes(conta, tipo=None):
    for transacao, valor in conta["transacoes"]:
        if tipo is None or tipo == transacao:
            yield transacao, valor


# ==============================
# ITERADOR PERSONALIZADO
# ==============================
class ContaIterador:
    def __init__(self, contas):
        self.contas = contas
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.contas):
            raise StopIteration

        conta = self.contas[self.index]
        self.index += 1

        return {
            "conta": conta["numero_conta"],
            "agencia": conta["agencia"],
            "saldo": conta["saldo"]
        }


# ==============================
# CLIENTES
# ==============================
def cadastrar_cliente():
    print("\n====== CADASTRO DE CLIENTE ======")
    nome = input("Nome completo: ")
    rg = input("RG: ")
    cpf = input("CPF (login): ")

    if buscar_cliente_por_cpf(cpf):
        print("Já existe um cliente com esse CPF!")
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

    print("Cliente cadastrado com sucesso!")
    return cliente


def buscar_cliente_por_cpf(cpf):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None


# ==============================
# LOGIN
# ==============================
def login():
    print("\n====== LOGIN ======")
    cpf = input("CPF: ")
    senha = getpass.getpass("Senha: ")

    cliente = buscar_cliente_por_cpf(cpf)

    if not cliente:
        print("Cliente não encontrado.")
        return None

    if cliente["senha"] != senha:
        print("Senha incorreta.")
        return None

    print(f"Bem-vindo, {cliente['nome']}!")
    return cliente


# ==============================
# CONTAS
# ==============================
@log_transacao
def criar_conta(cliente):
    print("\n====== CRIAÇÃO DE CONTA ======")

    conta = {
        "agencia": "0001",
        "numero_conta": len(contas) + 1,
        "cliente_id": cliente["id"],
        "tipo": "Conta Corrente",
        "saldo": 0,
        "extrato": "",
        "transacoes": [],
        "limite": 500,
        "saques_realizados": 0,
        "LIMITE_SAQUES": 3,
    }

    contas.append(conta)

    print(f"Conta criada: Agência 0001 | Conta {conta['numero_conta']}")
    return conta


def selecionar_conta(cliente):
    for conta in contas:
        if conta["cliente_id"] == cliente["id"]:
            return conta
    return None


# ==============================
# OPERAÇÕES BANCÁRIAS
# ==============================
@log_transacao
def depositar(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        conta["transacoes"].append(("deposito", valor))
        print("Depósito realizado!")
    else:
        print("Valor inválido.")


@log_transacao
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
        conta["transacoes"].append(("saque", valor))
        conta["saques_realizados"] += 1
        print("Saque realizado!")
    else:
        print("Valor inválido.")


def extrato(conta):
    print("\n====== EXTRATO ======")
    print(conta["extrato"] if conta["extrato"] else "Nenhuma movimentação.")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")
    print("======================")


# ==============================
# MENU PRINCIPAL
# ==============================
def main():
    conta_logada = None

    menu_principal = """
====== MENU PRINCIPAL ======
[1] Login
[2] Cadastrar Cliente
[3] Relatório de Contas (Iterador)
[q] Sair
=> """

    menu_conta = """
====== MENU DA CONTA ======
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar nova conta
[5] Listar transações (gerador)
[6] Trocar usuário
[q] Logout
=> """

    while True:
        if not conta_logada:
            opcao = input(menu_principal)

            if opcao == "1":
                cliente = login()
                if cliente:
                    conta_logada = selecionar_conta(cliente) or criar_conta(cliente)

            elif opcao == "2":
                cadastrar_cliente()

            elif opcao == "3":
                print("\n=== TODAS AS CONTAS ===")
                for info in ContaIterador(contas):
                    print(info)

            elif opcao == "q":
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        else:
            opcao = input(menu_conta)

            if opcao == "1":
                depositar(conta_logada, float(input("Valor: ")))

            elif opcao == "2":
                sacar(conta_logada, float(input("Valor: ")))

            elif opcao == "3":
                extrato(conta_logada)

            elif opcao == "4":
                conta_logada = criar_conta(buscar_cliente_por_cpf(input("CPF: ")))

            elif opcao == "5":
                tipo = input("Filtrar por (deposito/saque) ou Enter: ") or None
                print("\n=== TRANSAÇÕES ===")
                for t, v in gerador_transacoes(conta_logada, tipo):
                    print(f"{t.upper()} - R$ {v}")

            elif opcao == "6":
                conta_logada = None

            elif opcao == "q":
                conta_logada = None

            else:
                print("Opção inválida.")


main()
