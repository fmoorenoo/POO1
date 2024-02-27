¿Qué palabra reservada se utiliza en lugar de animal (nombre de la clase) para acceder al atributo patas?

class animal:
    patas = 0

    def caminar():
        print(f"Caminando con {animal.patas} patas")

def main():
    vaca = animal
    vaca.patas = 4
    vaca.caminar()

    pato = animal
    vaca.patas = 2
    pato.caminar

if __name__ == "__main__":
    main()