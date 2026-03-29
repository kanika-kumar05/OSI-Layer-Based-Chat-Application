class BaseLayer:
    def __init__(self, name):
        self.name = name

    def process_send(self, packet):
        """Processes the packet during encapsulation (Sender)."""
        pass

    def process_receive(self, packet):
        """Processes the packet during decapsulation (Receiver)."""
        pass
    
    def log(self, message, status="OK"):
        """Utility for logging layer-specific actions."""
        return {"layer": self.name, "message": message, "status": status}
