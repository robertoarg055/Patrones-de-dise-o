class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
class Orden:
    def __init__(self, usuario, productos, direccion, metodo_de_pago, descuento):
        self.usuario = usuario
        self.productos = productos
        self.direccion = direccion
        self.metodo_de_pago = metodo_de_pago
        self.descuento = descuento
        self.total = None
    def __str__(self):
        productos_str = ", ".join(f"{p.nombre} (${p.precio})" for p in self.productos)
        return (
            f"Orden de: {self.usuario}\n"
            f"Productos: {productos_str}\n"
            f"Dirección: {self.direccion}\n"
            f"Pago: {self.metodo_de_pago}\n"
            f"Descuento: {self.descuento}%\n"
            f"Total a pagar: ${self.total}"
        )
class OrdenBuilder:
    def __init__(self):
        self.orden = Orden("", [], "", "", 0)
    def con_usuario(self, usuario):
        self.orden.usuario = usuario
        return self
    def agregar_producto(self, nombre, precio):
        self.orden.productos.append(Producto(nombre, precio))
        return self
    def con_direccion(self, direccion):
        self.orden.direccion = direccion
        return self
    def con_metodo_de_pago(self, metodo_de_pago):
        self.orden.metodo_de_pago = metodo_de_pago
        return self
    def con_descuento(self, descuento):
        self.orden.descuento = descuento
        return self
    def construir(self):
        return self.orden
class CalculadorDeTotal:
    def calcular(self, orden):
        total = sum(p.precio for p in orden.productos)
        if orden.descuento:
            total -= total * orden.descuento / 100
        return total
builder = OrdenBuilder()
orden = (
    builder.con_usuario("Roberto Argueta")
            .agregar_producto("Asus Zephyrus G14", 1300)
            .agregar_producto("Logitech", 40)
            .con_direccion("El Salvador, San Salvador")
            .con_metodo_de_pago("Trasnferencia bancaria")
            .con_descuento(15)
            .construir()
)
calculador = CalculadorDeTotal()
orden.total = calculador.calcular(orden)
print(orden)