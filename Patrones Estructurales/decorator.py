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
        return "Leche descremada"
    def get_price(self):
        return 0.50
class LecheSoya(DecoradorBebida):
    def get_description(self):
        return "Leche de soya"
    def get_price(self):
        return 0.75
class LecheCoco(DecoradorBebida):
    def get_description(self):
        return "Leche de coco"
    def get_price(self):
        return 1.00
class Canela(DecoradorBebida):
    def get_description(self):
        return "Canela"
    def get_price(self):
        return 0.25
class CremaBatida(DecoradorBebida):
    def get_description(self):
        return "Crema batida"
    def get_price(self):
        return 1.50
class Saborizante(DecoradorBebida):
    def get_description(self):
        return "Saborizante"
    def get_price(self):
        return 1.25 
class Mediana(DecoradorBebida):
    def get_description(self):
        return "Bebida mediana"
    def get_price(self):
        return 1.00
class Grande(DecoradorBebida):
    def get_description(self):
        return "Bebida grande"
    def get_price(self):
        return 2.00
mi_cafe= Cafe()
print(mi_cafe.get_description(), ":", mi_cafe.get_price())
cafe_con_leche= LecheDescremada(mi_cafe)
print(cafe_con_leche.get_description(), ":", cafe_con_leche.get_price())
