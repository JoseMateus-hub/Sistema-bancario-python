# 🏦 Sistema Bancário em Python (Com Login e Conta Corrente)

Este projeto é um **Sistema Bancário completo**, desenvolvido em **Python puro**, utilizando **dicionários**, **funções**, e um modelo simples de **armazenamento em memória**.

O sistema permite cadastro de clientes, criação de contas, login seguro com senha, depósitos, saques, extrato bancário e múltiplas contas por cliente.

---

## 🚀 Funcionalidades

### 👤 **Cadastro de Cliente**
- Nome completo  
- RG  
- CPF (utilizado como login)  
- Senha (oculta usando `getpass`)  
- Endereço  
- Cidade  
- Estado  

---

### 🔐 **Login Seguro**
- Acesso usando **CPF + senha**
- Senha não aparece na tela durante digitação

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
