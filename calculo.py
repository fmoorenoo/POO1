class Calculo:
    def __init__(self, num1:int, num2:int):
        self.num1 = num1
        self.num2 = num2
        self.suma = 0
        self.resta = 0
        self.multi = 0
        self.div = 0

    def sumador(self):
        self.suma = self.num1 + self.num2

    def restador(self):
        self.resta = self.num1 - self.num2

    def multiplicador(self):
        self.multi = self.num1 * self.num2

    def divisor(self):
        self.div = self.num1 / self.num2

    def imprimir(self):
        print(f"Suma: {self.suma}. Resta: {self.resta}. Multiplicación: {self.multi}. División: {self.div}")



if __name__ == '__main__':
    calculo = Calculo(10, 5)
    calculo.sumador()
    calculo.restador()
    calculo.multiplicador()
    calculo.divisor()
    calculo.imprimir()
    
    
