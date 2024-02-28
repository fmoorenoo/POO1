class alumno:
    def imprimir(self):
        self.nota = 0
        self.nombre = ""  
        print(f"La nota de {self.nombre} es un {self.nota}")

    def promociona(self):
        self.nota = 0
        self.nombre = ""
        if (self.nota >= 5):
            print(f"{self.nombre} promociona.")



def main():
     pass


if __name__ == '__main__':
     main()