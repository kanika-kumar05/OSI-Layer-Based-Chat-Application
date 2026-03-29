from .base_layer import BaseLayer

class Layer1Physical(BaseLayer):
    def __init__(self):
        super().__init__("Physical Layer (L1)")

    def process_send(self, packet):
        """Binary Bitstream: Converting packet payload to binary string."""
        binary_payload = ' '.join(format(ord(x), '08b') for x in str(packet.payload))
        # We'll truncate it for cleaner output
        display = binary_payload[:32] + "..." if len(binary_payload) > 32 else binary_payload
        return self.log(f"Bitstream Generated: {display}")

    def process_receive(self, packet):
        """Bitstream to Frame reconstruction (Simulated)."""
        return self.log("Bitstream synchronized and received")
