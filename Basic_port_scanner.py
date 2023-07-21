import socket

def scan_ports(target, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target_host = input("Enter the target host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    open_ports = scan_ports(target_host, start_port, end_port)

    if open_ports:
        print("Open ports:")
        print(open_ports)
    else:
        print("No open ports found.")


        