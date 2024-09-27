#1.Crea una clase Coche con atributos como
#marca, modelo, y año. Define un método llamado
#mostrar_info que imprima la información del coche.
#Luego, crea dos objetos de la clase Coche y muestra
#la información de cada uno.

class car:
    def __init__(self, marca, modelo, año) -> None:
        self.marca=marca
        self.modelo=modelo
        self.año=año
        
    def show_info(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nAño: {self.año}")
car1= car("Volkswagen", "T40", "1992")
car1.show_info()