class ManejadorDeConexiones:
    _instancia = None
    _conectado = False
    _conexiones_abiertas = 0
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ManejadorDeConexiones, cls).__new__(cls)
        return cls._instancia
    def conectar(self):
        if not self._conectado:
            print("Conectando a la base de datos...")
            self._conectado = True
            ManejadorDeConexiones._conexiones_abiertas += 1
        else:
            print("Ya existe una conexión activa.")
    def desconectar(self):
        if self._conectado:
            print("Conexión cerrada.")
            self._conectado = False
            ManejadorDeConexiones._conexiones_abiertas -= 1
    @classmethod
    def conexiones_abiertas(cls):
        return cls._conexiones_abiertas
if __name__ == "__main__": 
    conexiones = ManejadorDeConexiones()
    conexiones.conectar()
    print(f"Conexiones abiertas: {ManejadorDeConexiones.conexiones_abiertas()}")
    conexiones.conectar()
    print(f"Conexiones abiertas: {ManejadorDeConexiones.conexiones_abiertas()}")    
    conexiones.desconectar()
    print(f"Conexiones abiertas: {ManejadorDeConexiones.conexiones_abiertas()}")    