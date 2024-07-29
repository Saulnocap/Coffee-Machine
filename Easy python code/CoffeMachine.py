class CoffeeMachine:
    def __init__(self):
        self.coffee_amount = 100  # cantidad de café en oz
        self.sugar_amount = 50    # cantidad de azúcar en cucharadas
        self.cups = {
            'pequeño': {'size': 3, 'count': 10},
            'mediano': {'size': 5, 'count': 10},
            'grande': {'size': 7, 'count': 10}
        }

    def select_cup(self):
        while True:
            cup_type = input("Seleccione el tipo de vaso (pequeño, mediano, grande): ").lower()
            if cup_type in self.cups and self.cups[cup_type]['count'] > 0:
                return cup_type
            else:
                print("No hay vasos de ese tamaño, por favor seleccione otro tipo de vaso.")

    def select_sugar(self):
        while True:
            try:
                sugar = int(input("Seleccione la cantidad de azúcar (0, 1, 2, 3 cucharadas): "))
                if 0 <= sugar <= 3:
                    if self.sugar_amount >= sugar:
                        return sugar
                    else:
                        print(f"No hay suficiente azúcar. Solo hay {self.sugar_amount} cucharadas disponibles.")
                else:
                    print("Cantidad de azúcar no válida, por favor seleccione otra cantidad.")
            except ValueError:
                print("Entrada inválida, por favor seleccione otra cantidad.")

    def dispense_coffee(self, cup_type, sugar):
        cup_size = self.cups[cup_type]['size']
        if self.coffee_amount >= cup_size:
            self.coffee_amount -= cup_size
            self.sugar_amount -= sugar
            self.cups[cup_type]['count'] -= 1
            print(f"Dispensando café {cup_type} con {sugar} cucharadas de azúcar.")
        else:
            print(f"No hay suficiente café para llenar un vaso {cup_type}. Solo hay {self.coffee_amount} oz de café disponible.")
            choice = input("¿Desea cancelar el proceso? (si/no): ").lower()
            if choice == 'no':
                self.sugar_amount -= sugar
                self.coffee_amount = 0
                self.cups[cup_type]['count'] -= 1
                print(f"Dispensando {self.coffee_amount} oz de café {cup_type} con {sugar} cucharadas de azúcar.")

    def run(self):
        while True:
            print(f"\nCantidad de café: {self.coffee_amount} oz")
            print(f"Cantidad de azúcar: {self.sugar_amount} cucharadas")
            print("Cantidad de vasos: ", {k: v['count'] for k, v in self.cups.items()})

            cup_type = self.select_cup()
            sugar = self.select_sugar()
            self.dispense_coffee(cup_type, sugar)

            cont = input("¿Desea otra bebida? (si/no): ").lower()
            if cont != 'si':
                break

if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.run()
