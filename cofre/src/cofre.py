from src.item import Item
from src.moeda import Moeda

class Cofre:

    def __init__(self, volumeMaximo: int):
        self.volumeMaximo = volumeMaximo
        self.volume = 0
        self.itens = ""
        self.cofre_quebrado = False
        self.somatorio_moedas = 0
        self.volume_restante = self.volumeMaximo - self.volume

    def getVolume(self):
        return self.volume

    def getVolumeMaximo(self):
        return self.volumeMaximo

    def getVolumeRestante(self):
        return self.volume_restante

    def addItem(self, item: Item):
        if self.volume >= self.volumeMaximo:
            return False
        else:
            if self.cofre_quebrado == False:
                if item.volume <= self.volume_restante:
                    self.volume += item.volume
                    if self.itens:
                        self.itens += print(item.descricao)
                    else:
                        self.itens += item.descricao
                    self.volume_restante = self.volumeMaximo - self.volume
                    return True


    def addMoeda(self, moeda: Moeda):
        if self.volume >= self.volume_restante:
            return False
        else:
            if self.cofre_quebrado == False:
                if moeda.volume <= self.volume_restante:
                    self.volume += moeda.volume
                    self.somatorio_moedas += moeda.valor
                    self.volume_restante = self.volumeMaximo - self.volume
                    return True

    def obterItens(self):
        if self.cofre_quebrado:
            if self.itens:
                return self.itens
            else:
                return "vazio"
        else:
            return None

    def obterMoedas(self):
        if self.cofre_quebrado == True:
            return self.somatorio_moedas
        else:
            return -1

    def taInteiro(self):
        if self.cofre_quebrado == False:
            return True

    def quebrar(self):
        if not self.cofre_quebrado:
            print("cofre quebrado")
            self.cofre_quebrado = True
            return True
        else:
            return False and print("o cofre já foi quebrado")