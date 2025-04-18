from datetime import datetime, timedelta

class SistemaBancario:
    def __init__(self):
        self.saldo = 0.0
        self.transacoes = []  # Lista para armazenar transações
        self.saques_diarios = 0
        self.limite_saque_diario = 3
        self.limite_valor_saque = 500.0
        self.horario_inicio = timedelta(hours=8)  # Horário de início das operações
        self.horario_fim = timedelta(hours=18)   # Horário de fim das operações

    def depositar(self, valor):
        """Realiza um depósito na conta."""
        if valor > 0:
            self.saldo += valor
            self.transacoes.append({"tipo": "depósito", "valor": valor, "data_hora": datetime.now()})
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("❌ Valor inválido para depósito. Por favor, insira um valor positivo.")

    def sacar(self, valor):
        """Realiza um saque na conta."""
        hora_atual = datetime.now().time()
        if not (self.horario_inicio <= timedelta(hours=hora_atual.hour) <= self.horario_fim):
            print("❌ Operação fora do horário permitido (8h às 18h).")
            return

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
            self.transacoes.append({"tipo": "saque", "valor": valor, "data_hora": datetime.now()})
            self.saques_diarios += 1
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")

    def exibir_extrato(self, data_inicio=None, data_fim=None):
        """Exibe o extrato da conta, podendo filtrar por período."""
        print("\n=================== Extrato Bancário ====================")
        print("📌 Transações:")

        transacoes_filtradas = self.transacoes
        if data_inicio and data_fim:
            data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
            data_fim = datetime.strptime(data_fim, "%Y-%m-%d")
            transacoes_filtradas = [
                t for t in self.transacoes
                if data_inicio <= t["data_hora"].date() <= data_fim
            ]

        if transacoes_filtradas:
            for transacao in transacoes_filtradas:
                data_formatada = transacao["data_hora"].strftime("%d/%m/%Y %H:%M:%S")
                print(f"   - {transacao['tipo'].capitalize()}: R$ {transacao['valor']:.2f} em {data_formatada}")
        else:
            print("   Nenhuma transação encontrada no período especificado.")

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
            print("Deseja filtrar por período? (s/n)")
            filtrar = input().strip().lower()
            if filtrar == "s":
                data_inicio = input("Digite a data de início (YYYY-MM-DD): ")
                data_fim = input("Digite a data de fim (YYYY-MM-DD): ")
                sistema.exibir_extrato(data_inicio, data_fim)
            else:
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