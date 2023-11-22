class Conta:

    def __init__(self, numero:int, saldo:float):
        self.numero = numero
        self.limite = 100
        self.saldo = saldo + 100
        self.lista_extrato = []

    def getNumero(self):
        return self.numero

    def getSaldo(self):
        return self.saldo

    def getLimite(self):
        return self.limite

    def sacar(self, valor: float):
        if self.saldo - valor < 0 or valor < 0 or len(self.lista_extrato) >= 10:
            return False
        else:
            self.saldo -= valor
            self.lista_extrato.append(float(-valor))
            return True

    def depositar(self, valor: float):
        if self.saldo <= 0 and len(self.lista_extrato) >= 10:
            return False
        else:
            if valor < 0:
                return False
            else:
                self.limite = 0
                self.saldo += valor - (self.limite*2)
                self.lista_extrato.append(float(+valor))
                return True


    def transferir(self, destino, valor:float):
        if self.saldo - valor < 0 or valor < 0 or len(self.lista_extrato) >= 10:
            return False
        elif not isinstance(destino, Conta):
            return False
        else:
            if valor > self.saldo - self.limite:
                self.limite = self.limite - (valor - (self.saldo - self.limite))
            self.saldo -= valor
            self.lista_extrato.append(float(-valor))
            destino.depositar(valor)
        return True

    def verExtrato(self):
        return self.lista_extrato