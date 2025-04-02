# Desafio Dio - Lab: Sistema Bancário V1.1 🚀

Este é um **sistema bancário simples** desenvolvido em Python. Ele foi projetado para atender aos requisitos básicos de um banco, permitindo que o usuário realize operações de **depósito**, **saque** e **extrato**, com algumas funcionalidades adicionais para tornar o sistema mais robusto e amigável.

## 📋 Funcionalidades

O sistema bancário implementa as seguintes operações:

- **Depósito**:
  - Permite realizar depósitos de valores positivos.
  - Atualiza o saldo da conta.
  - Armazena o histórico dos depósitos realizados.

- **Saque**:
  - Permite realizar no máximo **3 saques diários**.
  - Limita o valor máximo por saque a **R$ 500,00**.
  - Verifica se há saldo suficiente antes de realizar o saque.
  - Armazena o histórico dos saques realizados.

- **Extrato**:
  - Lista todos os depósitos e saques realizados.
  - Exibe o saldo atual da conta no formato `R$ xxx.xx`.

- **Resetar Saques Diários**:
  - Permite reiniciar o contador de saques diários.

- **Reiniciar Sistema**:
  - Zera todas as informações da conta (saldo, depósitos e saques) e reinicia o sistema.

## 🛠️ Tecnologias Utilizadas

- Linguagem: **Python 3.10+**
- Estruturas de controle e listas
- Programação orientada a objetos (POO)

## ⚙️ Estrutura do Código

### 1. Classe `SistemaBancario`

A classe encapsula toda a lógica do sistema bancário. Abaixo estão os principais métodos e suas responsabilidades:

#### **`__init__`**
Inicializa os atributos da conta:
- `saldo`: Saldo atual da conta.
- `depositos`: Lista para armazenar os depósitos realizados.
- `saques`: Lista para armazenar os saques realizados.
- `saques_diarios`: Contador de saques realizados no dia.
- `limite_saque_diario`: Limite de saques diários (3).
- `limite_valor_saque`: Limite de valor por saque (R$ 500,00).

#### **`depositar(valor)`**
- Verifica se o valor é positivo.
- Adiciona o valor ao saldo e registra o depósito na lista de depósitos.
- Exibe uma mensagem de sucesso ou erro.

#### **`sacar(valor)`**
- Verifica:
  - Se o limite de saques diários foi atingido.
  - Se o valor do saque excede o limite de R$ 500,00.
  - Se há saldo suficiente para realizar o saque.
  - Se o valor do saque é válido (positivo).
- Deduz o valor do saldo e registra o saque na lista de saques.
- Incrementa o contador de saques diários.

#### **`exibir_extrato()`**
- Exibe todos os depósitos e saques realizados, além do saldo atual.
- Formata os valores no estilo `R$ xxx.xx`.

#### **`resetar_saques_diarios()`**
- Reseta o contador de saques diários.

### 2. Função `exibir_menu()`
- Exibe o menu principal com as opções disponíveis para o usuário.

### 3. Função `main()`
- Controla o fluxo principal do sistema.
- Permite que o usuário escolha as operações no menu.
- Gerencia entradas inválidas e reinicializações do sistema.

## 🚀 Como Executar o Sistema

Siga as etapas abaixo para executar o sistema bancário:

1. Certifique-se de ter o Python 3.10 ou superior instalado.
2. Clone este repositório:
   ```bash
   git clone https://github.com/wesleypiaui/dio-lab-sistema-bancario.git
   ```
3. Navegue até o diretório do projeto:
   ```bash
   cd dio-lab-sistema-bancario
   ```
4. Execute o arquivo principal:
   ```bash
   python dio-lab-sistema-bancario.py
   ```

## 📖 Exemplo de Uso

### Menu Principal
Ao executar o sistema, você verá o seguinte menu:

```
--- Sistema Bancário ---
1️⃣ Depositar
2️⃣ Sacar
3️⃣ Exibir Extrato
4️⃣ Resetar Saques Diários
5️⃣ Reiniciar Sistema
6️⃣ Sair
```

### Operação de Depósito
Quando você escolher a opção de depósito, insira o valor desejado:

```
Escolha uma opção: 1
Digite o valor para depositar: 1000
✅ Depósito de R$ 1000.00 realizado com sucesso!
```

### Operação de Saque
Escolha o valor do saque. O sistema verificará os limites e o saldo:

```
Escolha uma opção: 2
Digite o valor para sacar: 500
✅ Saque de R$ 500.00 realizado com sucesso!
```

### Operação de Extrato
Exibe o histórico de depósitos e saques, além do saldo atual:

```
Escolha uma opção: 3

--- Extrato Bancário ---
📌 Depósitos:
   - R$ 1000.00

📌 Saques:
   - R$ 500.00

💰 Saldo atual: R$ 500.00
------------------------
```

### Resetar Saques Diários
Restaura o limite de 3 saques diários:

```
Escolha uma opção: 4
✅ Contador de saques diários foi resetado.
```

### Reiniciar Sistema
Zera todas as informações e reinicia o sistema:

```
Escolha uma opção: 5
🔄 Reiniciando o sistema...
```

## 🛡️ Validações Implementadas

- **Depósito**: Apenas valores positivos são aceitos.
- **Saque**:
  - Limite de 3 saques diários.
  - Limite máximo de R$ 500,00 por saque.
  - Verificação de saldo insuficiente.
  - Rejeita valores negativos ou inválidos.
- **Entradas Inválidas**: O sistema lida com entradas não numéricas e exibe mensagens claras.

## 📈 Melhorias Futuras

- Adicionar suporte para múltiplos usuários (com contas separadas).
- Implementar persistência de dados (salvar informações em banco de dados ou arquivos).
- Criar uma interface gráfica ou API para acesso remoto.
- Adicionar relatórios financeiros e gráficos.

## 🧑‍💻 Autor

Desenvolvido por [Wesley Sousa](https://github.com/wesleypiaui).

## 📄 Licença

Este projeto não está licenciado.