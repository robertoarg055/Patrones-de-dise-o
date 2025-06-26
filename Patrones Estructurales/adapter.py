import json
class ProcesadorPago:
    def procesar_pago(self, json_data):
        pass
class PagoModerno(ProcesadorPago):
    def procesar_pago(self, json_data):
#Usando json.loads para convertir el string JSON a un diccionario, como el ejemplo 1 de la clase
        data = json.loads(json_data)
        print(f"[MODERNO] Procesando pago de {data['amount']} {data['currency']} para usuario {data['user_id']}")
class ServicioPagoLegacy:
    def procesar_pago(self, json_data):
        print(f"[LEGACY] Procesando pago para cliente {json_data['cliente']} por {json_data['monto_total']} {json_data['moneda']}")
class PagoAdapter(ProcesadorPago):
    def __init__(self, servicio_legacy):
        self.servicio_legacy = servicio_legacy
    def procesar_pago(self, json_data):
        print("[JSON moderno recibido]", json_data)
        parsed_modern_data = json.loads(json_data) 
        json_data_adaptado = self.adaptar_json(parsed_modern_data) 
        print("[Adaptado a legacy]", json_data_adaptado)
        self.servicio_legacy.procesar_pago(json_data_adaptado)
    def adaptar_json(self, modern_data: dict):
        return {
            "cliente": modern_data["user_id"],
            "monto_total": modern_data["amount"],
            "moneda": modern_data["currency"]
        }
if __name__ == "__main__":
    json_input = json.dumps({
        "user_id": "u123",
        "amount": 250.0,
        "currency": "USD"
    })
    print("\n--- Uso de clase moderna ---")
    mod_processor = PagoModerno()
    mod_processor.procesar_pago(json_input)
    print("\n--- Uso de clase legacy con adaptador ---")
    legacy_service_instance = ServicioPagoLegacy()
    adapter_instance = PagoAdapter(legacy_service_instance)
    adapter_instance.procesar_pago(json_input)