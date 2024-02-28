class animal:
    def caminar(self): #método
        self.patas = 0 #atributo
        print(f"Caminando con {self.patas} patas")

def main():
    vaca = animal()
    vaca.patas = 4
    vaca.caminar()

    pato = animal()
    pato.patas = 2
    pato.caminar()

    vaca.caminar()

if __name__ == "__main__":
    main()