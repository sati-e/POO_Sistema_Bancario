# Simulação sistema bancário

class Conta(object):

    # define os dados da conta
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    # calcula o depósito feito na conta
    def deposito(self):
        comando = input("DESEJA DEPOSITAR NA CONTA? sim OU nao: ")  # pergunta se quer depositar
        if comando == "sim":
            Dep = int(input("Deposito: "))
            if Dep > 0:  # verifica se o valor é válido, maior que 0
                self.saldo = Dep + self.saldo
                return None
            else:
                raise ValueError("O valor do depósito deve ser positivo.")

    # calcula a retirada de um valor da conta
    def retirada(self, valor):
        nvalor = self.saldo - valor  # calcula o novo valor depois da retirada
        if nvalor >= 0:  # verifica se o saldo é suficiente p/ a retirada
            self.saldo = nvalor  # atualiza o saldo
            print("Retirada: ", valor)
            print("Novo valor: ", nvalor)
        else:
            print("mpossível completar a retirada.")
        return None

    # mostra dados
    def __str__(self):
        mostra = f"Nome: {self.nome} \nSaldo: {self.saldo}"
        return mostra


# subclasse pessoa fisica
class P_fisica(Conta):

    # define os dados da pessoa fisica
    def __init__(self, nome, saldo, genero, cpf):
        super().__init__(nome, saldo)
        self.cpf = cpf
        self.tax = 2
        self.genero = genero

    # calcula a returada de dinheiro com taxa da pessoa fisica
    def retirada(self, valor):
        valor_total = valor + self.tax
        super().retirada(valor_total)
        print(f"Valor total retirado (com taxa): {valor_total}")

    def __str__(self):
        return super().__str__() + f"\nGênero: {self.genero} \nCnpj: {self.cpf}\n"


# subclasse pessoa juridica
class P_juridica(Conta):

    ##define os dados da pessoa juridica
    def __init__(self, nome, saldo, modalidade, cnpj):
        super().__init__(nome, saldo)
        self.tax = 5
        self.modalidade = modalidade
        self.cnpj = cnpj

    # calcula a retirada de dinheiro com tava da pessoa juridica
    def retirada(self, valor):
        valor_total = valor + self.tax
        super().retirada(valor_total)
        print(f"Valor total retirado (com taxa): {valor_total}")
        # pai + filho
        return super().retirada(valor)

    # mostra dados
    def __str__(self):
        return super().__str__() + f"\nModalidade {self.modalidade} \nCpf: {self.cnpj}\n"


if __name__ == '__main__':
    # testes

    # exemplo de uso da classe Conta
    c1 = Conta("Marco", 7000)
    print("Conta criada: ")
    print(c1)

    # exemplo de depósito na conta
    c1.deposito()
    print("Depósito da conta: ")
    print(c1)

    # exemplo de retirada da conta
    c1.retirada(500)
    print("Retirada da conta: ")
    print(c1)

    # exemplo de uso da subclassse pessoa fisica
    pf = P_fisica("Mat", 8000, "Masculino", "123.456.789-00")
    print("Pessoa física: ")
    print(pf)

    # exemplo de depósito na conta de pessoa física
    pf.deposito()
    print("Depósito realizado pela pessoa física: ")
    print(pf)

    # exemplo de retirada na conta da pessoa fisica
    pf.retirada(3000)
    print("Retirada realizada pela pessoa física: ")
    print(pf)

    # exemplo de uso da subclassse pessoa juridica
    pj = P_juridica("Nilo", 10000, "Empresa X", "12.345.678/0001-90")
    print("Pessoa jurídica: ")
    print(pj)

    # exemplo de deposito na conta da pessoa juridica
    pj.deposito()
    print("Depósito realizado pela pessoa juridica: ")
    print(pj)

    # exemplo de retirada na conta da pessoa juridica
    pj.retirada(5000)
    print("retirada realizada pela pessoa jurídica: ")
    print(pj)

    print(vars(pf))
    print(vars(pj))
