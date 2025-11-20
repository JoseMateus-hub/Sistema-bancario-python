# 🏦 Sistema Bancário Avançado em Python  
### Com Login, Múltiplas Contas, Decoradores, Geradores e Iteradores

Este projeto é uma evolução completa do sistema bancário desenvolvido durante os desafios da DIO, agora incluindo:

✔ Decorador de Log (com registro de data/hora)  
✔ Gerador de Relatórios (usando `yield`)  
✔ Iterador Personalizado para listar contas  
✔ Login seguro (CPF + senha)  
✔ Cadastro de clientes  
✔ Criação de conta corrente  
✔ Depósito, saque e extrato  
✔ Histórico das transações  
✔ Estrutura organizada e pronta para expandir  

Todo o sistema usa apenas **Python puro**, sem bancos de dados externos, ideal para estudo de lógica, funções, dicionários, decorators, iteradores e geradores.

---

## 🚀 Funcionalidades

### 👤 **Cadastro de Cliente**
- Nome completo  
- RG  
- CPF (login único)  
- Senha (oculta com `getpass`)  
- Endereço completo (rua, cidade, estado)

---

### 🔐 **Login Seguro**
- Autenticação por CPF + senha  
- Senha não aparece na tela  
- Cada cliente pode ter várias contas bancárias  

---

### 💳 **Conta Corrente**
Cada conta possui:
- Agência: **0001**
- Número automático
- Tipo: **Conta Corrente**
- Saldo
- Extrato
- Lista de transações (saques/depositos)
- Limite de saque
- Limite diário de saques

---

### 💰 **Operações Bancárias**
- **Depósito**  
- **Saque** (com validações e limite)  
- **Extrato bancário**  

Todas as transações são registradas dentro da conta.

---

## 🧾 Decorador de Log (Decorator)

Todas as funções de transações (depósito, saque, criação de conta) recebem automaticamente um log no console:
---

### 💳 **Conta Corrente**
Cada cliente pode ter uma ou mais contas:
- Agência **0001**
- Número da conta gerado automaticamente
- Tipo: **Conta Corrente**
- Limite de saque: **R$ 500**
- Limite de saques diários: **3**

---

### 💰 **Operações Bancárias**
- **Depósito**
- **Saque** (com validações)
- **Extrato Bancário**
- Histórico de movimentações

---

### 🔄 Outras Funções
- Trocar usuário (logout)
- Criar nova conta para o mesmo cliente

---

## 🧠 Como o Sistema Funciona

O sistema utiliza:
- Dicionários para representar clientes e contas  
- Listas para armazenar todos os cadastros  
- Funções organizadas por responsabilidade  
- Laços de repetição para simular o menu interativo  

Não há necessidade de banco de dados: tudo roda em memória.

---

## 🗂 Estrutura do Código
