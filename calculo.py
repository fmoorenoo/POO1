class Calculo:
    def __init__(self, num1:int, num2:int):
        self.num1 = num1
        self.num2 = num2
        self.sum = 0
        self.rest = 0
        self.multi = 0
        self.div = 0

    def suma(self) -> int:
        self.sum = self.num1 + self.num2
        return self.sum

    def resta(self) -> int:
        self.rest = self.num1 - self.num2
        return self.rest

    def multiplicacion(self) -> int:
        self.multi = self.num1 * self.num2
        return self.multi

    def division(self) -> int:
        self.div = self.num1 / self.num2
        return self.div

    def imprimir(self):
        print(f"Suma: {self.suma()}. Resta: {self.resta()}. Multiplicación: {self.multiplicacion()}. División: {self.division()}")


if __name__ == '__main__':
    calculo = Calculo(10, 5)
    calculo.imprimir()
    
    
    
