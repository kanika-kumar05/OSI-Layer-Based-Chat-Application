from .base_layer import BaseLayer

class Layer4Transport(BaseLayer):
    def __init__(self, allowed_ports=None, blocked_ports=None):
        super().__init__("Transport Layer (L4)")
        self.allowed_ports = allowed_ports or [80, 443, 22, 53]
        self.blocked_ports = blocked_ports or [23, 4444, 139]

    def process_send(self, packet):
        """TCP Segment Simulation: Filtering based on port numbers."""
        if packet.dest_port in self.blocked_ports:
            return self.log(f"Blocked: Port {packet.dest_port} is BANNED", "BLOCKED")
        
        if packet.dest_port not in self.allowed_ports:
            # For this simulation, we'll allow it but log a warning if not in common allowed list
            return self.log(f"Warning: Port {packet.dest_port} is uncommon", "WARNING")
            
        return self.log(f"TCP Segment Created (Port: {packet.dest_port})")

    def process_receive(self, packet):
        """Verifies segment integrity (Simulated)."""
        return self.log(f"Segment received on Port {packet.dest_port}")
