class Vehiculo:
    def crear(self):
        pass
class Motor:
    def encender(self):
        pass
class Carro(Vehiculo):
    def crear(self):
        print("Creando vehículo terrestre: Carro")
class MotorCombustion(Motor):
    def encender(self):
        print("Usando motor: Motor de combustión")
class Lancha(Vehiculo):
    def crear(self):
        print("Creando vehículo acuático: Lancha")
class MotorNautico(Motor):
    def encender(self):
        print("Usando motor: Motor náutico")
class Avion(Vehiculo):
    def crear(self):
        print("Creando vehículo aeronáutico: Avión")
class MotorJet(Motor):
    def encender(self):
        print("Usando motor: Motor de jet")
class FabricaVehiculos:
    def crear_vehiculo(self): pass
    def crear_motor(self): pass
class FabricaTerrestre(FabricaVehiculos):
    def crear_vehiculo(self):
        return Carro()
    def crear_motor(self):
        return MotorCombustion()
class FabricaAcuatica(FabricaVehiculos):
    def crear_vehiculo(self):
        return Lancha()
    def crear_motor(self):
        return MotorNautico()
class FabricaAeronave(FabricaVehiculos):
    def crear_vehiculo(self):
        return Avion()
    def crear_motor(self):
        return MotorJet()
def construir_vehiculo(factory: FabricaVehiculos):
    vehiculo = factory.crear_vehiculo()
    motor = factory.crear_motor()
    vehiculo.crear()
    motor.encender()        
if __name__ == "__main__":
    construir_vehiculo(FabricaTerrestre())
    construir_vehiculo(FabricaAcuatica())     
    construir_vehiculo(FabricaAeronave())