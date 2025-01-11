import socket

def scan_ports(host, port_range):
    open_ports = []
    for port in port_range:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Timeout of 1 second
        result = s.connect_ex((host, port))  # Tries to connect to the host and port
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports

def get_host_info(user_input):
    try:
        # Attempt to resolve input as hostname
        host_ip = socket.gethostbyname(user_input)
        host_name = user_input
    except socket.gaierror:
        # Assume input is IP address if hostname resolution fails
        host_ip = user_input
        try:
            host_name = socket.gethostbyaddr(host_ip)[0]
        except socket.herror:
            host_name = "Unknown"
    return host_name, host_ip

if __name__ == "__main__":
    user_input = input("Enter the host name or IP address to scan: ")
    host_name, host_ip = get_host_info(user_input)

    print(f"\nScanning host: {host_name} ({host_ip})")
    port_range = range(1, 1025)  # Check ports 1 to 1024
    open_ports = scan_ports(host_ip, port_range)
    
    if open_ports:
        print(f"Open ports on {host_name} ({host_ip}): {open_ports}")
    else:
        print(f"No open ports found on {host_name} ({host_ip}).")