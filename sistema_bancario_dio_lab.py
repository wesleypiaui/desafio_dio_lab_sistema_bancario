class SistemaBancario:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []  # Lista para armazenar os depósitos
        self.saques = []     # Lista para armazenar os saques
        self.saques_diarios = 0  # Contador de saques diários
        self.limite_saque_diario = 3  # Limite de saques por dia
        self.limite_valor_saque = 500.0  # Limite de valor por saque

    def depositar(self, valor):
        """Realiza um depósito na conta."""
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("❌ Valor inválido para depósito. Por favor, insira um valor positivo.")

    def sacar(self, valor):
        """Realiza um saque na conta."""
        if self.saques_diarios >= self.limite_saque_diario:
            print("❌ Você atingiu o limite de saques diários (3 saques).")
        elif valor > self.limite_valor_saque:
            print(f"❌ Limite de saque excedido! O valor máximo por saque é R$ {self.limite_valor_saque:.2f}.")
        elif valor > self.saldo:
            print("❌ Saldo insuficiente para realizar o saque.")
        elif valor <= 0:
            print("❌ Valor inválido para saque. Por favor, insira um valor positivo.")
        else:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_diarios += 1
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        """Exibe o extrato da conta."""
        print("\n=================== Extrato Bancário ====================")
        print("📌 Depósitos:")
        if self.depositos:
            for deposito in self.depositos:
                print(f"   - R$ {deposito:.2f}")
        else:
            print("   Nenhum depósito realizado.")

        print("\n📌 Saques:")
        if self.saques:
            for saque in self.saques:
                print(f"   - R$ {saque:.2f}")
        else:
            print("   Nenhum saque realizado.")

        print(f"\n💰 Saldo atual: R$ {self.saldo:.2f}")
        print("=======================================================")

    def resetar_saques_diarios(self):
        """Reseta o contador de saques diários."""
        self.saques_diarios = 0
        print("✅ Contador de saques diários foi resetado.")

def exibir_menu():
    """Exibe o menu principal."""
    print("\n--- Sistema Bancário ---")
    print("1️⃣ Depositar")
    print("2️⃣ Sacar")
    print("3️⃣ Exibir Extrato")
    print("4️⃣ Resetar Saques Diários")
    print("5️⃣ Reiniciar Sistema")
    print("6️⃣ Sair")

def main():
    """Função principal para executar o sistema bancário."""
    sistema = SistemaBancario()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor = float(input("Digite o valor para depositar: "))
                sistema.depositar(valor)
            except ValueError:
                print("❌ Entrada inválida. Por favor, insira um valor numérico.")
        elif opcao == "2":
            try:
                valor = float(input("Digite o valor para sacar: "))
                sistema.sacar(valor)
            except ValueError:
                print("❌ Entrada inválida. Por favor, insira um valor numérico.")
        elif opcao == "3":
            sistema.exibir_extrato()
        elif opcao == "4":
            sistema.resetar_saques_diarios()
        elif opcao == "5":
            print("🔄 Reiniciando o sistema...")
            sistema = SistemaBancario()
        elif opcao == "6":
            print("👋 Obrigado por usar o sistema bancário. Até logo!")
            break
        else:
            print("❌ Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()