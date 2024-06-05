from datetime import date

# Classe que representa o histórico de transações de uma conta
class Historico:
    def __init__(self):
        self.transacoes = []  # Lista de transações

    # Método para adicionar uma transação ao histórico
    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

# Interface para transações
class Transacao:
    def registrar(self, conta):
        pass  # Método que será implementado nas subclasses

# Classe para transações de depósito
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor  # Valor do depósito

    # Método para registrar um depósito na conta
    def registrar(self, conta):
        if self.valor > 0:  # Depósito deve ser positivo
            conta.saldo += self.valor
            conta.historico.adicionar_transacao(f"Depósito de {self.valor}")
            return True
        return False

# Classe para transações de saque
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor  # Valor do saque

    # Método para registrar um saque na conta
    def registrar(self, conta):
        if 0 < self.valor <= conta.saldo:  # Saque deve ser positivo e menor ou igual ao saldo
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(f"Saque de {self.valor}")
            return True
        return False

# Classe que representa um cliente do banco
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco  # Endereço do cliente
        self.contas = []  # Lista de contas do cliente

    # Método para realizar uma transação em uma conta do cliente
    def realizar_transacao(self, conta, transacao):
        if transacao.registrar(conta):
            print("Transação realizada com sucesso.")
        else:
            print("Falha na transação.")

    # Método para adicionar uma conta ao cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe que representa uma pessoa física, herda de Cliente
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)  # Chama o construtor da classe base
        self.cpf = cpf  # CPF do cliente
        self.nome = nome  # Nome do cliente
        self.data_nascimento = data_nascimento  # Data de nascimento do cliente

# Classe que representa uma conta bancária
class Conta:
    def __init__(self, saldo, numero, agencia, cliente):
        self.saldo = saldo  # Saldo inicial da conta
        self.numero = numero  # Número da conta
        self.agencia = agencia  # Agência da conta
        self.cliente = cliente  # Cliente associado à conta
        self.historico = Historico()  # Histórico de transações da conta
        cliente.adicionar_conta(self)  # Adiciona a conta ao cliente

    # Método estático para criar uma nova conta
    @staticmethod
    def nova_conta(cliente, numero, agencia):
        return Conta(0, numero, agencia, cliente)

    # Método para sacar um valor da conta
    def sacar(self, valor):
        saque = Saque(valor)
        return saque.registrar(self)

    # Método para depositar um valor na conta
    def depositar(self, valor):
        deposito = Deposito(valor)
        return deposito.registrar(self)

# Classe que representa uma conta corrente, herda de Conta
class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente)  # Chama o construtor da classe base
        self.limite = limite  # Limite de crédito da conta corrente
        self.limite_saques = limite_saques  # Limite de saques diários
