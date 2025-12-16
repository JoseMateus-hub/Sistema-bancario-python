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
            "saldo": conta["saldo"],
        }
