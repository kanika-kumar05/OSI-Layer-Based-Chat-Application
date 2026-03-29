from .base_layer import BaseLayer

class Layer2DataLink(BaseLayer):
    def __init__(self):
        super().__init__("Data Link Layer (L2)")

    def process_send(self, packet):
        """Ethernet Framing: Adding MAC address headers."""
        return self.log(f"Ethernet Frame Created (MAC: {packet.src_mac} -> {packet.dest_mac})")

    def process_receive(self, packet):
        """Verifying MAC destination (Simulated)."""
        return self.log(f"MAC Verification successful (Dest: {packet.dest_mac})")
