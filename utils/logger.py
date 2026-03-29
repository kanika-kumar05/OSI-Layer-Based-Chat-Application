import sys

class Logger:
    # ANSI Color Codes
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def print_header(text):
        print(f"\n{Logger.BOLD}{Logger.OKCYAN}{'='*60}")
        print(f"{text.center(60)}")
        print(f"{'='*60}{Logger.ENDC}")

    @staticmethod
    def print_layer_step(layer_name, message, status="OK"):
        color = Logger.OKGREEN
        prefix = "[OK]      "
        
        if status == "BLOCKED":
            color = Logger.FAIL
            prefix = "[BLOCKED] "
        elif status == "WARNING":
            color = Logger.WARNING
            prefix = "[WARN]    "
        elif status == "ERROR":
            color = Logger.FAIL
            prefix = "[ERROR]   "

        print(f"{Logger.BOLD}{layer_name:<25}{Logger.ENDC} -> {color}{prefix}{message}{Logger.ENDC}")

    @staticmethod
    def print_result(success, reason=None):
        if success:
            print(f"\n{Logger.BOLD}{Logger.OKGREEN}FINAL RESULT -> ALLOWED{Logger.ENDC}")
        else:
            print(f"\n{Logger.BOLD}{Logger.FAIL}FINAL RESULT -> BLOCKED ({reason}){Logger.ENDC}")

    @staticmethod
    def print_packet_info(packet):
        print(f"{Logger.OKBLUE}Packet Details: Src={packet.src_ip}:{packet.src_port}, Dest={packet.dest_ip}:{packet.dest_port}{Logger.ENDC}")
        print(f"{Logger.OKBLUE}Data Payload: '{packet.payload}'{Logger.ENDC}")
