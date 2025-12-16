def gerador_transacoes(conta, tipo=None):
    for transacao, valor in conta["transacoes"]:
        if tipo is None or tipo == transacao:
            yield transacao, valor
