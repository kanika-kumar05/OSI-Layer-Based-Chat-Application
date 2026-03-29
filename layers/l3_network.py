from .base_layer import BaseLayer
from algorithms.bloom_filter import BloomFilter

class Layer3Network(BaseLayer):
    def __init__(self, banned_ips=None):
        super().__init__("Network Layer (L3)")
        self.bloom_filter = BloomFilter(size=2048, hash_count=7)
        self.banned_ips = banned_ips or ["10.0.0.5", "192.168.1.100", "1.1.1.1"]
        for ip in self.banned_ips:
            self.bloom_filter.add(ip)

    def process_send(self, packet):
        """IP Filtering: Checks the Destination IP against the Bloom Filter."""
        if self.bloom_filter.contains(packet.dest_ip):
            # Bloom Filter has false positives, but for simple simulation, we'll assume it's blocked
            return self.log(f"Blocked: Destination IP {packet.dest_ip} is BANNED (Bloom Filter)", "BLOCKED")
            
        return self.log(f"IP Packet Header Created (Dest: {packet.dest_ip})")

    def process_receive(self, packet):
        """Routing check (Simulated)."""
        return self.log(f"Packet received from {packet.src_ip}")
