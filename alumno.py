class alumno:
    def __init__(self):
        self.nota = 0
        self.nombre = ""


    def imprimir(self):
        print(f"La nota de {self.nombre} es un {self.nota}")


    def promociona(self):
        if (self.nota >= 5):
            print(f"{self.nombre} promociona.")



def main():
     pass


if __name__ == '__main__':
     main()