# Security Encryption
I have developed this repository to post some piece of python programs which were used for encryption and decryption with an interactive client and server architecture (Only for Hill and Product Cipher).

The working is the input is given on client program and that input is encrypted with some key given by the user. Then it is sent to server along with the key. Finally the server decrypts the cipher text and sends to client.

# Encryption Algorithms put so far
1. Hill Cipher.
2. Product Cipher (Combination of Rail fence and Hill).
3. Simple Data Encryption Standard.

# Usage
To download only specified directory, go to [DownGit](https://minhaskamal.github.io/DownGit/#/home) and specify the path of that directory. For whole repository, you can git clone it.

After downloading, open two command prompt windows and run server program on one window and client on other.

For Hill Cipher, the client program is named as `Client.py` and server program as `Server.py`.

For Product Cipher, the client program is named as `ClientProduct.py` and server program as `ServerProduct.py`.

Note: 
1. Server program should be run first in one window followed by client program in another window.
2. Input is given on client program.
3. Provide exit on the string input to exit.

# Sample input and output
Here, I have demonstrated the way of usage of my Hill cipher program.

## Client.py

```
PS D:\semester_6\Information Security\implementations> python Client.py

Connected to server at 127.0.0.1:12345
Enter a message to send to the server: safemessages

        WARNINGS BEFORE ENTERING A KEY
You will be Reprompted to enter a key if:
        1. The length of key is not in [1, 4, 9, 16, 36, 144]
        2. It's absolute determinant is an even number (even 0)
        3. It's absolute determinant is a multiple of 13.
So enter it responsibly.

Enter a key: ciphering
Received from server: SAFEMESSAGES

Connected to server at 127.0.0.1:12345
Enter a message to send to the server: cometorajamhallatnoon

        WARNINGS BEFORE ENTERING A KEY
You will be Reprompted to enter a key if:
        1. The length of key is not in [1, 9, 49, 441]
        2. It's absolute determinant is an even number (even 0)
        3. It's absolute determinant is a multiple of 13.
So enter it responsibly.

Enter a key: ciphering
Received from server: COMETORAJAMHALLATNOON

Connected to server at 127.0.0.1:12345
Enter a message to send to the server: exit
Program Terminated.
```

## Server.py

```
PS D:\semester_6\Information Security\implementations> python Server.py
Server listening on 127.0.0.1:12345

Accepted connection from ('127.0.0.1', 64084)
Received Cipher Text: HDSIOEYQOCAA

Accepted connection from ('127.0.0.1', 64093)
Received Cipher Text: KOKGEZNMITLQTXBJLNXLI

Accepted connection from ('127.0.0.1', 63635)
Client wants to exit. Shutting down the server.
```
In the same way, the remaining algorithms is run depending on the input requirements.

