# 🏦 Sistema Bancário em Python (POO)

Este repositório contém a implementação de um **Sistema Bancário completo**, desenvolvido em **Python e Programação Orientada a Objetos**, seguindo as boas práticas e o modelo UML proposto pela DIO.

O sistema permite criar clientes, criar contas, realizar depósitos, saques e gerar extrato detalhado.

---

## 📌 Funcionalidades do Sistema

✔ Criar cliente (Pessoa Física)  
✔ Criar conta corrente  
✔ Realizar depósitos  
✔ Realizar saques (com limite diário e por operação)  
✔ Gerar extrato com histórico de transações  
✔ Registro automático das operações  
✔ Código totalmente estruturado em **POO**  
✔ Fácil de entender, estudar e expandir  

---

## 🧱 Arquitetura do Projeto (versão simplificada em um único arquivo)

Embora originalmente modelado para pastas separadas, este repositório reúne todo o código em **um único arquivo Python**, devido ao uso via celular.

O arquivo contém todas as classes abaixo:

- `Cliente`
- `PessoaFisica`
- `Conta`
- `ContaCorrente`
- `Historico`
- `Transacao` (interface)
- `Saque`
- `Deposito`
- Sistema de Menu (funções principais)

---

## 📐 Modelo UML Utilizado (DIO)

O sistema foi implementado baseado no seguinte diagrama UML:

Cliente ├── PessoaFisica | Conta ----------------> Historico │         ↑ │         │ │    ContaCorrente | Transacao (Interface) ├── Saque └── Deposito

Esse diagrama representa a estrutura orientada a objetos aplicada no código.

---

## 🚀 Como executar o sistema

1. Certifique-se de ter o **Python 3.10+** instalado.
2. Baixe o arquivo `Sistema-bancário.py`.
3. Abra o terminal e execute:

```bash
python Sistema-bancário.py
