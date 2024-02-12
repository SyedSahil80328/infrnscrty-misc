from EncodeAndDecode import encode
from NumericalUtilities import findFactors, determinant
from AlphabeticalUtilities import convertKeyToMatrix

import socket
import json

def startClient():
    # Create a socket object
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    host = '127.0.0.1'
    port = 12345
    clientSocket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    # Send data to the server
    plainText = input("Enter a message to send to the server: ").upper()
    keyLengths = findFactors(len(plainText))
    print("\n\tWARNINGS BEFORE ENTERING A KEY")
    print("The program will terminate if:")
    print(f"\t1. The length of key is not in {keyLengths}")
    print("\t2. It's absolute determinant is an even number (even 0)")
    print("\t3. It's absolute determinant is a multiple of 13.\nSo enter it responsibly.\n")
    key = input("Enter a key: ").upper()

    keyLength = len(key)

    if keyLength not in keyLengths:
        print("Keylength is inappropriate. So encryption fails.")
        exit(0)

    keyMatrix = convertKeyToMatrix(key)
    det = abs(determinant(keyMatrix))

    if det % 2 == 0 or det % 13 == 0:
        print(f"The gcd({det}, 26) is > 1. So modular multiplicative inverse never exists. So encryption will succeed, but decryption?")
        exit(0)

    cipherText = encode(plainText, keyMatrix)
    keyMatrixData = json.dumps(keyMatrix)
    data = {"string": cipherText, "matrix": keyMatrixData}
    processedData = json.dumps(data)
    clientSocket.sendall(processedData.encode('utf-8'))

    # Receive the echoed data from the server
    plainText = clientSocket.recv(1024).decode('utf-8')
    print(f"Received from server: {plainText}")

    # Close the connection
    clientSocket.close()

if __name__ == "__main__":
    startClient()
