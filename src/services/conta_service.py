from data.database import contas
from decorators.logger import log_transacao

def selecionar_conta(cliente):
    for conta in contas:
        if conta["cliente_id"] == cliente["id"]:
            return conta
    return None


@log_transacao
def criar_conta(cliente):
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


@log_transacao
def depositar(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        conta["transacoes"].append(("deposito", valor))
        print("Depósito realizado!")
        return True
    print("Valor inválido.")
    return False


@log_transacao
def sacar(conta, valor):
    if valor > conta["saldo"]:
        print("Saldo insuficiente.")
    elif valor > conta["limite"]:
        print("Valor excede o limite.")
    elif conta["saques_realizados"] >= conta["LIMITE_SAQUES"]:
        print("Limite de saques atingido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["transacoes"].append(("saque", valor))
        conta["saques_realizados"] += 1
        print("Saque realizado!")
        return True
    print("Valor inválido.")
    return False


def extrato(conta):
    print("\n====== EXTRATO ======")
    print(conta["extrato"] or "Nenhuma movimentação.")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")
