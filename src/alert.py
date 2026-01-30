import time


RED = "\033[91m"
BOLD = "\033[1m"
BLINK = "\033[5m"
RESET = "\033[0m"


def flash_alert(message, flashes=3):
    for _ in range(flashes):
        print(f"{BLINK}{BOLD}{RED}🚨 ALERT 🚨 {message}{RESET}")
        time.sleep(0.3)
        print(" " * 80, end="\r")
        time.sleep(0.3)
