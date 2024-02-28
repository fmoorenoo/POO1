class Persona:
    def __init__(self, nombre, años):
        self.años = años
        self.nombre = nombre

    def imprimir(self):
        print(f"{self.nombre} tiene {self.años} años")

    def cumpleaños(self):
        self.años = self.años + 1
        print(f"Es el cumpleaños de {self.nombre}. Ahora tiene {self.años} años.")


def main():
     pass


if __name__ == '__main__':
     main()