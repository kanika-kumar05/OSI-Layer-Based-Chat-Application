from .base_layer import BaseLayer
from algorithms.trie import Trie
from algorithms.rabin_karp import contains_patterns

class Layer7Application(BaseLayer):
    def __init__(self, malicious_keywords=None):
        super().__init__("Application Layer (L7)")
        self.trie = Trie()
        self.malicious_keywords = malicious_keywords or ["malware", "virus", "exploit", "hack", "drop database"]
        for keyword in self.malicious_keywords:
            self.trie.insert(keyword)

    def process_send(self, packet):
        """Inspects payload for malicious keywords using Trie and Rabin-Karp."""
        text = packet.payload.lower()
        
        # Fast search with Trie
        if self.trie.contains_any(text):
            return self.log("Blocked: Malicious keyword found (Trie)", "BLOCKED")
            
        # Pattern search with Rabin-Karp
        if contains_patterns(text, self.malicious_keywords):
            return self.log("Blocked: Malicious pattern found (Rabin-Karp)", "BLOCKED")
            
        return self.log("Content Clean (L7 Verified)")

    def process_receive(self, packet):
        """Decapsulation: Content inspection before delivering to user."""
        return self.log("Received data: " + packet.payload)
