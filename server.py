import socket

# TODO: Modificar loop while(3 chamadas não faz sentido bixo) ConnectionRefusedError: [WinError 10061] Nenhuma conexão pôde ser feita porque a máquina de destino as recusou ativamente
# TODO: Modificar mensagem
# TODO: Método de saida do terminal(control C não ta funcionando)
# TODO: adicionar ping no corpo da resposta

DATA_PAYLOAD = 4096  # The maximum amount of data to be received at once, mb 1024


def server(host="localhost", port=8082):
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_host = host
    server_port = port
    server_address = (server_host, server_port)
    print(f"Starting up server on {server_host} port {server_port}")
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(5)
    while True:
        # print(
        #         "Select a server function: \n" +
        #         "(1) To show current DateTime;\n" +
        #         "(2) Return a random number 0-100;\n" +
        #         "(3) Current temperature in Caçador - SC.\n" +
        #         "(Any input not on the list will disconnect.)\n"
        #     )
        print("Waiting to receive message from client.")
        client, address = sock.accept()
        try:
            while True:
                data = client.recv(DATA_PAYLOAD)
                decoded_data = data.decode("utf-8")
                if decoded_data == "0":
                    print("Received '0'. Closing connection.")
                    break
                elif decoded_data in ["1", "2", "3"]:
                    print(decoded_data)
                    print(type(decoded_data))
                    print(f"Data: {data}")
                    client.send(data)
                else:
                    break

        except Exception as e:
            print(f"An error occurred: {e}")
            client.close()


server()
