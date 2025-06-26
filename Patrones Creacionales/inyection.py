class Logger:
    def log(self, mensaje):
        print(f"[LOG] {mensaje}")
class EmailService:
    def enviar(self, mensaje):
        print(f"[EMAIL] Enviando email: {mensaje}")
class CuentaBancaria:
    def __init__(self, logger, email):
        self.logger = logger
        self.email = email
    def transferir(self, monto):
        self.logger.log(f"Se transfirieron ${monto}")
        self.email.enviar(f"Se transfirieron ${monto} a su cuenta")
if __name__ == "__main__":
    logger = Logger()
    email = EmailService()
    cuenta1 = CuentaBancaria(logger, email)          
    cuenta2 = CuentaBancaria(logger, email)
    cuenta1.transferir(100)      
    cuenta2.transferir(200)