class alumno:
    def __init__(self, nombre, nota):
        self.nota = nota
        self.nombre = nombre


    def imprimir(self):
        print(f"La nota de {self.nombre} es un {self.nota}")


    def promociona(self):
        if (self.nota >= 5):
            print(f"{self.nombre} promociona.")
        else:
            print(f"{self.nombre} no promociona.")



def main():
     pass


if __name__ == '__main__':
     main()