import socket

# TODO: Aplicação Streamlit para conectar com o server
# TODO: mostrar tempo de resposta ping 127.0.0.1
DATA_PAYLOAD = 4096  # The maximum amount of data to be received at once, mb 1024


def client(host="localhost", port=8082):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_host = host
    server_port = port
    server_address = (server_host, server_port)
    print(f"Connecting to {server_host} port {server_port}")
    sock.connect(server_address)
    # Send data
    while True:
        print(
            "Select a server function: \n"
            + "(1) To show current DateTime;\n"
            + "(2) Return a random number 0-100;\n"
            + "(3) Current temperature in Caçador - SC;\n"
            + "Any input that is not on the list will disconnect.\n"
        )
        message = input("Select the number: ")
        print(type(message))
        print(message)
        if message in ["1", "2", "3"]:
            print(f"Sending input: {message}")
            sock.sendall(message.encode("utf-8"))
            # Look for the response
            amount_received = 0
            amount_expected = len(message)
            while amount_received < amount_expected:
                data = sock.recv(DATA_PAYLOAD)
                amount_received += len(data)
                print(f"Received: {data}")
        else:
            message = "0"
            sock.sendall(message.encode("utf-8"))
            sock.close()
            break
        print()


client()
