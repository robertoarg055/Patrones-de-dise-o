from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class NotificationInterface:
    def send(self):
        pass

class AbstractNotification(NotificationInterface):
    def __init__(self):
        self.receiver_name = None

    def set_receiver(self, name):
        self.receiver_name = name.upper()

class EmailNotification(AbstractNotification):
    def __init__(self):
        super().__init__()
        self.email_address = None

    def set_receiver(self, name, email_address):
        super().set_receiver(name)
        self.email_address = email_address

    def send(self):
        return f"Sent to {self.receiver_name} email to {self.email_address}"

class PhoneNotification(AbstractNotification):
    def __init__(self):
        super().__init__()
        self.phone = None
        self.area = None

    def set_receiver(self, name, phone, area):
        super().set_receiver(name)
        self.phone = phone
        self.area = area

class SmsNotification(PhoneNotification):
    def send(self):
        return f"Sent to {self.receiver_name} SMS to {self.area}-{self.phone}"

class WhatsappNotification(PhoneNotification):
    def send(self):
        return f"Sent to {self.receiver_name} WhatsApp message to {self.area}-{self.phone}"

class NotificationHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _send_error(self, message, status=400):
        self._set_headers(status)
        self.wfile.write(json.dumps({"error": message}).encode())

    def create_notification(self, notif_type, name, data):
        notif_config = {
            "email": {
                "class": EmailNotification,
                "required_fields": ["email_address"],
            },
            "sms": {
                "class": SmsNotification,
                "required_fields": ["phone", "area"],
            },
            "whatsapp": {
                "class": WhatsappNotification,
                "required_fields": ["phone", "area"],
            },
        }

        config = notif_config.get(notif_type)
        if not config:
            return None, "Invalid notification type"

        missing_fields = [f for f in config["required_fields"] if f not in data]
        if missing_fields:
            return None, f"Missing fields: {', '.join(missing_fields)}"

        notification = config["class"]()

        try:
            params = [data[f] for f in config["required_fields"]]
            notification.set_receiver(name, *params)
        except Exception as e:
            return None, str(e)

        return notification, None

    def do_POST(self):
        if self.path != "/send":
            self._send_error("Not Found", 404)
            return

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data)
            name = data.get("name")
            notif_type = data.get("type")

            if not name or not notif_type:
                self._send_error("Missing name or type")
                return

            notification, error = self.create_notification(notif_type, name, data)
            if error:
                self._send_error(error)
                return

            result = notification.send()
            self._set_headers(200)
            self.wfile.write(json.dumps({"message": result}).encode())

        except json.JSONDecodeError:
            self._send_error("Invalid JSON")

def run():
    server_address = ('', 3000)
    httpd = HTTPServer(server_address, NotificationHandler)
    print("Servidor corriendo en http://localhost:3000")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
