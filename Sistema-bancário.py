from abc import ABC, abstractmethod
from datetime import datetime


# ============================================================
#                        CLASSE HISTÓRICO
# ============================================================

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
        )

    def extrato(self):
        print("\n===== EXTRATO =====")
        if not self.transacoes:
            print("Nenhuma movimentação registrada.")
        else:
            for t in self.transacoes:
                print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
        print("====================")


# ============================================================
#                          CONTA
# ============================================================

class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    @staticmethod
    def nova_conta(cliente, numero):
        return Conta(cliente, numero)

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False

        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False

        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False

        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        return True


# ============================================================
#                     CONTA CORRENTE
# ============================================================

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saques:
            print("Limite de saques diários atingido.")
            return False

        if valor > self.limite:
            print("Valor excede o limite por operação.")
            return False

        sucesso = super().sacar(valor)

        if sucesso:
            self.saques_realizados += 1

        return sucesso


# ============================================================
#                     CLASSE CLIENTE
# ============================================================

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)


# ============================================================
#                   CLASSE PESSOA FÍSICA
# ============================================================

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


# ============================================================
#                     INTERFACE TRANSAÇÃO
# ============================================================

class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


# ============================================================
#                      SAQUE E DEPÓSITO
# ============================================================

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)
        return sucesso


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)
        return sucesso


# ============================================================
#                     BANCO / MENU PRINCIPAL
# ============================================================

clientes = []
contas = []


def buscar_cliente(cpf):
    for c in clientes:
        if c.cpf == cpf:
            return c
    return None


def buscar_conta(numero):
    for conta in contas:
        if conta.numero == numero:
            return conta
    return None


def criar_cliente():
    print("\n=== NOVO CLIENTE ===")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    nasc = input("Data nascimento (dd/mm/aaaa): ")
    end = input("Endereço: ")

    cliente = PessoaFisica(nome, cpf, nasc, end)
    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!\n")


def criar_conta():
    print("\n=== NOVA CONTA ===")
    cpf = input("CPF do cliente: ")

    cliente = buscar_cliente(cpf)
    if not cliente:
        print("Cliente não encontrado!\n")
        return

    numero = len(contas) + 1
    conta = ContaCorrente(cliente, numero)

    cliente.adicionar_conta(conta)
    contas.append(conta)

    print(f"Conta criada com sucesso! Número: {numero}\n")


def depositar():
    print("\n=== DEPÓSITO ===")
    num = int(input("Número da conta: "))
    valor = float(input("Valor: "))

    conta = buscar_conta(num)
    if not conta:
        print("Conta não encontrada!\n")
        return

    Deposito(valor).registrar(conta)


def sacar():
    print("\n=== SAQUE ===")
    num = int(input("Número da conta: "))
    valor = float(input("Valor: "))

    conta = buscar_conta(num)
    if not conta:
        print("Conta não encontrada!\n")
        return

    Saque(valor).registrar(conta)


def extrato():
    print("\n=== EXTRATO ===")
    num = int(input("Número da conta: "))

    conta = buscar_conta(num)
    if not conta:
        print("Conta não encontrada!\n")
        return

    conta.historico.extrato()
    print(f"Saldo atual: R$ {conta.saldo:.2f}\n")


def main():
    while True:
        print("""
===== SISTEMA BANCÁRIO =====
[1] Criar cliente
[2] Criar conta
[3] Depositar
[4] Sacar
[5] Extrato
[0] Sair
""")
        op = input("Opção: ")

        if op == "1":
            criar_cliente()
        elif op == "2":
            criar_conta()
        elif op == "3":
            depositar()
        elif op == "4":
            sacar()
        elif op == "5":
            extrato()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")


if __name__ == "__main__":
    main()
