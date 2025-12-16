from datetime import datetime

def log_transacao(func):
    def wrapper(*args, **kwargs):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        resultado = func(*args, **kwargs)

        texto_log = (
            f"{data_hora} | Função: {func.__name__} | "
            f"Args: {args} | Kwargs: {kwargs} | Retorno: {resultado}\n"
        )

        with open("log.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(texto_log)

        return resultado
    return wrapper
