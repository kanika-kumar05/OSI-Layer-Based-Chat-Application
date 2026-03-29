import base64
from .base_layer import BaseLayer

class Layer6Presentation(BaseLayer):
    def __init__(self):
        super().__init__("Presentation Layer (L6)")

    def process_send(self, packet):
        """Encodes payload to Base64 (Simulating encryption/formatting)."""
        packet.payload = base64.b64encode(packet.payload.encode()).decode()
        packet.is_encrypted = True
        return self.log("Encoded payload (Base64)")

    def process_receive(self, packet):
        """Decodes Base64 to original format (Simulating decryption/formatting)."""
        try:
            packet.payload = base64.b64decode(packet.payload.encode()).decode()
            packet.is_encrypted = False
            return self.log("Decoded payload successfully")
        except Exception:
            return self.log("Failed to decode payload", "ERROR")
