import socket
import threading 


# Seting the server ip and port

server_ip = "127.0.0.1"
server_port = 4444

# creating the socket used by the server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bindoing it and putting it in listenning mode 

server.bind((server_ip,server_port))
server.listen(5)
print(f"[*] Server is running on {server_ip}:{server_port}")

# creating the client-hanling thread to allow multiple client connection 

def handle_client(client_socket):
    
    request = client_socket.recv(1024)
    print("[*] receivde :" %request)

    client_socket.send("ACK!")
    client_socket.close()


while True:

    client,addr = server.accept()

    print ("[*] Accepted connection from: %s:%d" %(addr[0],addr[1]))

    client_handler = threading.Thread(target=handle_client,args = (client,))
    client_handler.start()


