import socket
from datetime import datetime
from random import randrange
import requests
from dotenv import load_dotenv
import os

load_dotenv()


# Constant defining the maximum size of data payload
DATA_PAYLOAD = 1024


def server(host="localhost", port=8082):
    """
    Initialize a server that listens for incoming connections and responds to specific requests.

    Args:
        host (str): The hostname or IP address to bind the server to. Defaults to 'localhost'.
        port (int): The port number to bind the server to. Defaults to 8082.
    """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print(f"Starting up server on {host} port {port}")
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(5)
    while True:
        print("Waiting to receive message from client.")
        client, address = sock.accept()
        try:
            while True:
                data = client.recv(DATA_PAYLOAD)
                decoded_data = data.decode("utf-8")
                if decoded_data == "0":
                    print("Received '0'. Closing connection.")
                    break
                elif decoded_data == "1":
                    print(f"`Function: {decoded_data}`")
                    date_result = datetime.now()
                    result = date_result.strftime("%d/%m/%Y %H:%M")
                    print(f"Result: {result}")
                    client.send(result.encode("utf-8"))
                    print()
                elif decoded_data == "2":
                    print(f"`Function: {decoded_data}`")
                    result = str(randrange(1, 100))
                    print(f"Result: {result}")
                    client.send(result.encode("utf-8"))
                    print()
                elif decoded_data == "3":
                    print(f"`Function: {decoded_data}`")
                    city = "Caçador"
                    state = "Santa Catarina"
                    country = "Brazil"
                    temp_result = get_current_temperature(city, state, country)
                    result = str(temp_result)
                    print(f"Result: {result}")
                    client.send(result.encode("utf-8"))
                    print()
                else:
                    break

        except Exception as e:
            print(f"An error occurred: {e}")
            client.close()


def get_current_temperature(city, state, country):
    """
    Retrieve the current temperature of a specified location using the OpenWeatherMap API.

    Args:
        city (str): The name of the city.
        state (str): The name of the state or region.
        country (str): The name of the country.

    Returns:
        float or str: The current temperature in Celsius if available, or "City not found" if the city is not found.
    """
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    query = f"{city},{state},{country}"
    complete_url = f"{base_url}q={query}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        current_temperature = main["temp"]
        return current_temperature
    else:
        return "City not found"


# Start the server
server()
