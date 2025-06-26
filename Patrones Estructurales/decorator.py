class Bebida:
    def get_description(self):
        return "Bebida base"
    def get_price(self):
        return 0.00
class Cafe(Bebida):
    def get_description(self):
        return "Café"
    def get_price(self):
        return 1.00
class DecoradorBebida(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida
    def get_description(self):
        return self.bebida.get_description() 
    def get_price(self):
        return self.bebida.get_price()
class LecheDescremada(DecoradorBebida):
    def get_description(self):
        return self.bebida.get_description() + ", Leche descremada"
    def get_price(self):
        return self.bebida.get_price() + 0.50
class LecheSoya(DecoradorBebida):
    def get_description(self):
        return self.bebida.get_description() + ", Leche de soya"
    def get_price(self):
        return self.bebida.get_price() + 0.75
class LecheCoco(DecoradorBebida):
    def get_description(self):
        return self.bebida.get_description() + ", Leche de coco"
    def get_price(self):
        return self.bebida.get_price() + 1.00   
class Canela(DecoradorBebida):
    def get_description(self):
        return self.bebida.get_description() + ", Canela"
    def get_price(self):
        return self.bebida.get_price() + 0.25
class CremaBatida(DecoradorBebida):
    def get_description(self):
        return self.bebida.get_description() + ", Crema batida"
    def get_price(self):
        return self.bebida.get_price() + 1.50
class Saborizante(DecoradorBebida):
    def __init__(self, bebida, cantidad=1):
        super().__init__(bebida)
        self.cantidad = cantidad
    def get_description(self):
        return self.bebida.get_description() + f", Saborizante x{self.cantidad}"
    def get_price(self):
        return self.bebida.get_price() + (1.25 * self.cantidad)
class BebidaMediana(DecoradorBebida):
    def __init__(self, bebida, cantidad=1):
        super().__init__(bebida)
        self.cantidad = cantidad
    def get_description(self):
        return self.bebida.get_description() + ", Bebida Mediana"
    def get_price(self):
        return self.bebida.get_price() + (1.00 * self.cantidad)
class BebidaGrande(DecoradorBebida):
    def __init__(self, bebida, cantidad=1):
        super().__init__(bebida)
        self.cantidad = cantidad
    def get_description(self):
        return self.bebida.get_description() + ", Bebida Grande" 
    def get_price(self):
        return self.bebida.get_price() + (2.00 * self.cantidad)
if __name__ == "__main__":
    bebida = Cafe()
    bebida = LecheDescremada(bebida)
    bebida = Canela(bebida)
    bebida = CremaBatida(bebida)
    bebida = Saborizante(bebida, cantidad=2)
    bebida = BebidaGrande(bebida)
    print("Descripción:", bebida.get_description())
    print("Precio total: $", round(bebida.get_price(), 2))