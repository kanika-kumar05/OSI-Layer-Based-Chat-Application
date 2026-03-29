import random
from .base_layer import BaseLayer

class Layer5Session(BaseLayer):
    def __init__(self):
        super().__init__("Session Layer (L5)")
        self.sessions = {} # Tracking session_id -> metadata

    def process_send(self, packet):
        """Assigns a Session ID and tracks the connection."""
        session_id = random.randint(1000, 9999)
        packet.session_id = session_id
        self.sessions[session_id] = {"start_ip": packet.src_ip, "status": "ACTIVE"}
        return self.log(f"Session established. ID: {session_id}")

    def process_receive(self, packet):
        """Verifies session ID on the receiver side."""
        if packet.session_id:
            return self.log(f"Validating Session ID: {packet.session_id}")
        return self.log("No Session ID found", "WARNING")
