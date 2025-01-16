import socket
import tkinter as tk

root = tk.Tk()
root.title("Network Device Scan")

# Label for greeting user
label = tk.Label(root, text="Hello, User!")
label.pack()

def scan_ports(host, portRange):
    openPorts = []
    for port in portRange:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Timeout in seconds. 1 second is set by default. 
        result = s.connect_ex((host, port))  # Attempting to connect to host and port. 
        if result == 0:/Users/michaelhuff/Documents/Cybersecurity/Visual TK Python Network Connections Info Scan.py
            openPorts.append(port)
        s.close()
    return openPorts

def get_host_info(userInput):
    try:
        # Attempt to resolve input as hostname
        hostIP = socket.gethostbyname(userInput)
        hostName = userInput
    except socket.gaierror:
        # Shift input criteria to IP address if hostname resolution fails
        hostIP = userInput
        try:
            hostName = socket.gethostbyaddr(hostIP)[0]
        except socket.herror:
            hostName = "Unknown"
    return hostName, hostIP

if __name__ == "__main__":
    userInput = input("Enter the host name or IP address to scan: ")
    hostName, hostIP = get_host_info(userInput)

    print(f"\nScanning host: {hostName} ({hostIP})")
    portRange = range(1, 1025)  # Port range Python will check is 1 to 1024
    openPorts = scan_ports(hostIP, portRange)
    
    if openPorts:
        print(f"Open ports on {hostName} ({hostIP}): {openPorts}")
    else:
        print(f"No open ports found on {hostName} ({hostIP}).")
