import socket
def portScan(host, port_range):
    portsOpen = []
    for port in portRange:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# This sets the timeout in seconds. Default is 1.
        socket.setdefaulttimeout(1)
# This is the attempt to connect to the host. 
        connectResult = s.connect_ex((host, port))
        if connectResult == 0:
            portsOpen.append(port)
        s.close()
    return portsOpen

# The following block will allow user input for IP address and contains the range of ports that can be scanned.
if __name__ == "__main__":
    host = input("Enter the host IP address you wish to scan. ")
    portRange = range(1, 1025)
    portsOpen = portScan(host, portRange)

    if portsOpen:
        print(f"The following ports for {host} are open: {portsOpen}")
    else:
        print(f"There were no ports found open on {host}.")