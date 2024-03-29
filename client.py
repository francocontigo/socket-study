import socket
import time

# The maximum amount of data to be received at once
DATA_PAYLOAD = 1024


def client(host="localhost", port=8082):
    """
    Connects to a server and interacts with it based on user input.

    Args:
        host (str): The hostname or IP address of the server. Defaults to 'localhost'.
        port (int): The port number of the server. Defaults to 8082.
    """
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, port)
    print(f"Connecting to {host} port {port}")
    start_time = time.time()
    sock.connect(server_address)
    end_time = time.time()

    # Send data and receive responses
    while True:
        print(
            "Select a server function: \n"
            + "(1) To show current DateTime;\n"
            + "(2) Return a random number 0-100;\n"
            + "(3) Current temperature in Caçador - SC;\n"
            + "Any input that is not on the list will disconnect.\n"
        )
        message = input("Select the number: ")
        if message in ["1", "2", "3"]:
            print(f"Sending input: {message}")
            sock.sendall(message.encode("utf-8"))

            while True:
                rtt_ms = (end_time - start_time) * 1000
                data = sock.recv(DATA_PAYLOAD)
                print(f"Connection time {host}:{port} successful. RTT: {rtt_ms:.2f} ms")
                print(f"Received: {data}")
                if data:
                    break

        else:
            message = "0"
            sock.sendall(message.encode("utf-8"))
            sock.close()
            break
        print()


client()
