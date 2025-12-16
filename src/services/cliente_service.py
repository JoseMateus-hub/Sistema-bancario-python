from data.database import clientes, gerador_id
from utils.auth import pedir_senha

def buscar_cliente_por_cpf(cpf):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None


def cadastrar_cliente():
    nome = input("\nNome completo: ")
    rg = input("RG: ")
    cpf = input("CPF (login): ")

    if buscar_cliente_por_cpf(cpf):
        print("Já existe um cliente com esse CPF!")
        return None

    senha = pedir_senha("Crie sua senha: ")
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


def login():
    cpf = input("\nCPF: ")
    senha = pedir_senha()

    cliente = buscar_cliente_por_cpf(cpf)

    if not cliente:
        print("Cliente não encontrado.")
        return None

    if cliente["senha"] != senha:
        print("Senha incorreta.")
        return None

    print(f"Bem-vindo, {cliente['nome']}!")
    return cliente
