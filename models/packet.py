class Packet:
    def __init__(self, src_ip, dest_ip, src_port, dest_port, payload, src_mac=None, dest_mac=None):
        self.src_ip = src_ip
        self.dest_ip = dest_ip
        self.src_port = src_port
        self.dest_port = dest_port
        self.payload = payload
        
        # Layer-specific data (headers/footers)
        self.headers = {}
        self.session_id = None
        self.is_encrypted = False
        
        # Addresses
        self.src_mac = src_mac or "00:00:00:00:00:00"
        self.dest_mac = dest_mac or "FF:FF:FF:FF:FF:FF"

    def __repr__(self):
        return f"Packet(Src: {self.src_ip}:{self.src_port}, Dest: {self.dest_ip}:{self.dest_port}, Payload: {self.payload})"
