import time
from models.packet import Packet
from layers.l7_application import Layer7Application
from layers.l6_presentation import Layer6Presentation
from layers.l5_session import Layer5Session
from layers.l4_transport import Layer4Transport
from layers.l3_network import Layer3Network
from layers.l2_data_link import Layer2DataLink
from layers.l1_physical import Layer1Physical
from utils.logger import Logger

class MultiLayerFilteringSystem:
    def __init__(self):
        # Initialize layers
        self.l7 = Layer7Application()
        self.l6 = Layer6Presentation()
        self.l5 = Layer5Session()
        self.l4 = Layer4Transport()
        self.l3 = Layer3Network()
        self.l2 = Layer2DataLink()
        self.l1 = Layer1Physical()
        
        # Transmission chain (Sender: 7 down to 1)
        self.sender_layers = [self.l7, self.l6, self.l5, self.l4, self.l3, self.l2, self.l1]
        
        # Reception chain (Receiver: 1 up to 7)
        self.receiver_layers = [self.l1, self.l2, self.l3, self.l4, self.l5, self.l6, self.l7]

    def process_packet(self, packet, packet_num):
        Logger.print_header(f"Processing Packet {packet_num}")
        Logger.print_packet_info(packet)
        
        print(f"\n{Logger.BOLD}SENDER SIDE (Encapsulation){Logger.ENDC}")
        for layer in self.sender_layers:
            time.sleep(0.3) # Simulate processing time
            result = layer.process_send(packet)
            Logger.print_layer_step(layer.name, result["message"], result["status"])
            
            if result["status"] == "BLOCKED":
                Logger.print_result(False, layer.name)
                return False
                
        print(f"\n{Logger.BOLD}RECEIVER SIDE (Decapsulation){Logger.ENDC}")
        for layer in self.receiver_layers:
            time.sleep(0.3)
            result = layer.process_receive(packet)
            Logger.print_layer_step(layer.name, result["message"], result.get("status", "OK"))
            
        Logger.print_result(True)
        return True

def run_simulation():
    system = MultiLayerFilteringSystem()
    
    test_packets = [
        # Packet 1: Normal Traffic
        Packet("192.168.1.5", "8.8.8.8", 1234, 443, "Hello World! This is a secure message."),
        
        # Packet 2: Malicious Application Content (Layer 7 Block)
        Packet("192.168.1.10", "1.2.3.4", 5678, 80, "I want to drop database and exploit your vulnerabilities."),
        
        # Packet 3: Banned Port (Layer 4 Block)
        Packet("192.168.1.15", "9.9.9.9", 8888, 4444, "Unauthorized access attempt."),
        
        # Packet 4: Banned IP (Layer 3 Block)
        Packet("10.0.0.1", "1.1.1.1", 443, 443, "Normal message but from/to a banned IP."),
    ]
    
    for i, packet in enumerate(test_packets, 1):
        system.process_packet(packet, i)
        print("\n" + "-"*60)

if __name__ == "__main__":
    try:
        run_simulation()
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
