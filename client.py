import socket

# TODO: Aplicação Streamlit para conectar com o server
# TODO: mostrar tempo de resposta ping 127.0.0.1
# TODO: Client(streamlit) -> Server(localhost), se possível adicionar outro server
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
                "Select a server function: \n" + 
                "(1) To show current DateTime;\n" + ""
                "(2) Return a random number 0-100;\n" +
                "(3) Current temperature in Caçador - SC.\n" +
                "(Any input not on the list will disconnect.)\n"
            )
            message = input("Select the number: ")
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
                sock.close()
                break
            print()
        # except socket.error as e:
        #     print(f"Socket error: {str(e)}")
        # except Exception as e:
        #     print(f"Other exception: {str(e)}")
        # finally:
        #     print("Closing connection to the server")
        #     


client()
