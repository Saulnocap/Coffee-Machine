class Cafetera:
    def __init__(self, cantidadCafe):
        self.cantidadCafe = cantidadCafe

    def setCantidadDeCafe(self, cantidadCafe):
        self.cantidadCafe = cantidadCafe

    def getCantidadDeCafe(self):
        return self.cantidadCafe

    def hasCafe(self, cantidadCafe):
        return self.cantidadCafe >= cantidadCafe

    def giveCafe(self, cantidadCafe):
        if self.hasCafe(cantidadCafe):
            self.cantidadCafe -= cantidadCafe
            return cantidadCafe
        else:
            disponible = self.cantidadCafe
            self.cantidadCafe = 0
            return disponible


class Azucarero:
    def __init__(self, cantidadDeAzucar):
        self.cantidadDeAzucar = cantidadDeAzucar

    def setCantidadDeAzucar(self, cantidadDeAzucar):
        self.cantidadDeAzucar = cantidadDeAzucar

    def getCantidadDeAzucar(self):
        return self.cantidadDeAzucar

    def hasAzucar(self, cantidadDeAzucar):
        return self.cantidadDeAzucar >= cantidadDeAzucar

    def giveAzucar(self, cantidadDeAzucar):
        if self.hasAzucar(cantidadDeAzucar):
            self.cantidadDeAzucar -= cantidadDeAzucar
            return cantidadDeAzucar
        else:
            disponible = self.cantidadDeAzucar
            self.cantidadDeAzucar = 0
            return disponible


class Vaso:
    def __init__(self, cantidadVasos, contenido):
        self.cantidadVasos = cantidadVasos
        self.contenido = contenido

    def setCantidadVasos(self, cantidadVasos):
        self.cantidadVasos = cantidadVasos

    def getCantidadVasos(self):
        return self.cantidadVasos

    def setContenido(self, contenido):
        self.contenido = contenido

    def getContenido(self):
        return self.contenido

    def hasVasos(self, cantidadVasos):
        return self.cantidadVasos >= cantidadVasos

    def giveVasos(self, cantidadVasos):
        if self.hasVasos(cantidadVasos):
            self.cantidadVasos -= cantidadVasos
            return cantidadVasos
        else:
            disponible = self.cantidadVasos
            self.cantidadVasos = 0
            return disponible


class MaquinaDeCafe:
    def __init__(self, cafe, vasosPequenos, vasosMedianos, vasosGrandes, azucar):
        self.cafe = cafe
        self.vasosPequenos = vasosPequenos
        self.vasosMedianos = vasosMedianos
        self.vasosGrandes = vasosGrandes
        self.azucar = azucar

    def getTipoVaso(self, tipoDeVaso):
        if tipoDeVaso == "pequeño":
            return self.vasosPequenos
        elif tipoDeVaso == "mediano":
            return self.vasosMedianos
        elif tipoDeVaso == "grande":
            return self.vasosGrandes
        else:
            return None

    def getVasoDeCafe(self, tipoDeVaso, cantidadDeVasos, cantidadDeAzucar):
        vaso = self.getTipoVaso(tipoDeVaso)
        if vaso is None:
            print("Tipo de vaso no válido.")
            return False

        if not vaso.hasVasos(cantidadDeVasos):
            print(f"No hay suficientes vasos {tipoDeVaso}.")
            return False

        if not self.azucar.hasAzucar(cantidadDeAzucar):
            print(f"No hay suficiente azúcar. Solo hay {self.azucar.getCantidadDeAzucar()} cucharadas disponibles.")
            return False

        cantidadCafeNecesaria = vaso.getContenido() * cantidadDeVasos
        if not self.cafe.hasCafe(cantidadCafeNecesaria):
            print(f"No hay suficiente café. Solo hay {self.cafe.getCantidadDeCafe()} oz de café disponible.")
            choice = input("¿Desea cancelar el proceso? (si/no): ").lower()
            if choice == 'si':
                return False

        self.cafe.giveCafe(cantidadCafeNecesaria)
        vaso.giveVasos(cantidadDeVasos)
        self.azucar.giveAzucar(cantidadDeAzucar)
        print(f"Dispensando café en vaso {tipoDeVaso} con {cantidadDeAzucar} cucharadas de azúcar.")
        return True


if __name__ == "__main__":
    cafe = Cafetera(100)  # cantidad de café en oz
    vasosPequenos = Vaso(10, 3)  # 10 vasos de 3 oz
    vasosMedianos = Vaso(10, 5)  # 10 vasos de 5 oz
    vasosGrandes = Vaso(10, 7)  # 10 vasos de 7 oz
    azucar = Azucarero(50)  # cantidad de azúcar en cucharadas

    maquina = MaquinaDeCafe(cafe, vasosPequenos, vasosMedianos, vasosGrandes, azucar)

    while True:
        print(f"\nCantidad de café: {cafe.getCantidadDeCafe()} oz")
        print(f"Cantidad de azúcar: {azucar.getCantidadDeAzucar()} cucharadas")
        print("Cantidad de vasos: ", {
            "pequeño": vasosPequenos.getCantidadVasos(),
            "mediano": vasosMedianos.getCantidadVasos(),
            "grande": vasosGrandes.getCantidadVasos()
        })

        tipoDeVaso = input("Seleccione el tipo de vaso (pequeño, mediano, grande): ").lower()
        cantidadDeVasos = 1  # Asumimos que el cliente quiere un vaso a la vez
        try:
            cantidadDeAzucar = int(input("Seleccione la cantidad de azúcar (0, 1, 2, 3 cucharadas): "))
        except ValueError:
            print("Cantidad de azúcar no válida.")
            continue

        maquina.getVasoDeCafe(tipoDeVaso, cantidadDeVasos, cantidadDeAzucar)

        cont = input("¿Desea otra bebida? (si/no): ").lower()
        if cont != 'si':
            break
