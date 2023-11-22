from src.grafite import Grafite


class Lapiseira:

    def __init__(self, calibre:float):
        self.calibre = calibre
        self.folhas_escritas = 0

    def inserir (self, grafite: Grafite):
        return False

    def remover(self):
        return False

    def escrever(self, folhas: int):
        return False

    def getGrafite(self):
        return None

    def getCalibre(self):
        return self.calibre

    def getFolhasEscritas(self):
        return self.folhas_escritas