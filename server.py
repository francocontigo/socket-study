import socket

# TODO: Modificar loop while(3 chamadas não faz sentido bixo) ConnectionRefusedError: [WinError 10061] Nenhuma conexão pôde ser feita porque a máquina de destino as recusou ativamente
# TODO: Modificar mensagem
# TODO: Método de saida do terminal(control C não ta funcionando)
# TODO: adicionar ping no corpo da resposta

DATA_PAYLOAD = 1024 #The maximum amount of data to be received at once

def server(host = 'localhost', port=8082):
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_host = host
    server_port = port
    server_address = (server_host, server_port)
    print(f"Starting up echo server on {server_host} port {server_port}")
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(5) 
    i = 0
    while True: 
        print("Waiting to receive message from client")
        client, address = sock.accept() 
        data = client.recv(DATA_PAYLOAD) 
        if data:
            print(f"Data: {data}")
            client.send(data)
            print(f"sent {data} bytes back to {address}")
            # end connection
            client.close()
            i+=1
            if i>=3: break           
server()