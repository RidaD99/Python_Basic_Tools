import socket
import threading 

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



def Port_Thread(target,port_batch):
    start_P, end_P = port_batch
    open_ports = scan_ports(target,start_P,end_P)
    print (f"OPEN ports in the range of {start_P} and {end_P}: {open_ports}")



def main():
    target_host = input("Enter the target host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    port_batches = [(i,min(i+9, end_port)) for i in range(start_port, end_port+1,10)]
    threads = []
    for port_batch in port_batches:
        thread = threading.Thread(target=Port_Thread, args=(target_host, port_batch) )
        threads.append(thread)
    
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()