from data.database import contas
from services.cliente_service import login, cadastrar_cliente, buscar_cliente_por_cpf
from services.conta_service import (
    selecionar_conta, criar_conta, depositar, sacar, extrato
)
from iterators.conta_iterador import ContaIterador
from generators.transacoes import gerador_transacoes

def main():
    conta_logada = None

    while True:
        if not conta_logada:
            opcao = input("""
[1] Login
[2] Cadastrar Cliente
[3] Relatório de Contas
[q] Sair
=> """)

            if opcao == "1":
                cliente = login()
                if cliente:
                    conta_logada = selecionar_conta(cliente) or criar_conta(cliente)

            elif opcao == "2":
                cadastrar_cliente()

            elif opcao == "3":
                for info in ContaIterador(contas):
                    print(info)

            elif opcao == "q":
                break

        else:
            opcao = input("""
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar nova conta
[5] Listar transações
[6] Trocar usuário
[q] Logout
=> """)

            if opcao == "1":
                depositar(conta_logada, float(input("Valor: ")))
            elif opcao == "2":
                sacar(conta_logada, float(input("Valor: ")))
            elif opcao == "3":
                extrato(conta_logada)
            elif opcao == "4":
                conta_logada = criar_conta(
                    buscar_cliente_por_cpf(input("CPF: "))
                )
            elif opcao == "5":
                for t, v in gerador_transacoes(conta_logada):
                    print(f"{t.upper()} - R$ {v}")
            elif opcao in ("6", "q"):
                conta_logada = None

if __name__ == "__main__":
    main()
