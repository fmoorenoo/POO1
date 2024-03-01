class Crypto:
    def __init__(self, nombre:str, euros:float):
        self.nombre = nombre
        self.euros = euros

    def stopLoss(self, min:float, max:float):
        self.min = min
        self.max = max

    def imprimir(self):
        print(f"El valor de {self.nombre} es de {self.euros} €")


if __name__ == '__main__':
    bitcoin = Crypto("Bitcoin", 57000)
    bitcoin.imprimir()