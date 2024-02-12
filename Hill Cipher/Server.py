from EncodeAndDecode import decode
from NumericalUtilities import determinant

import socket
import json

def start_server():
    # Create a socket object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    host = '127.0.0.1'
    port = 12345
    serverSocket.bind((host, port))

    # Listen for incoming connections (max queue of 5)
    serverSocket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        # Wait for a connection from the client
        clientSocket, clientAddress = serverSocket.accept()
        print(f"Accepted connection from {clientAddress}")

        # Handle the client's request
        handle_client(clientSocket)

        # Close the connection
        clientSocket.close()

def handle_client(clientSocket):
    # Receive data from the client
    rawData = clientSocket.recv(1024).decode('utf-8')
    print(rawData)
    data = json.loads(rawData)
    cipherText = data["string"]
    keyMatrix = json.loads(data["matrix"])

    print(f"Received Cipher Text: {cipherText}")

    det = determinant(keyMatrix)

    plainText = decode(cipherText, keyMatrix, det)
    # Echo the data back to the client
    clientSocket.sendall(plainText.encode('utf-8'))

if __name__ == "__main__":
    start_server()
