def gcd(n1, n2):
    t1, t2 = n1, n2
    while t2:
        r = t1 % t2
        t1 = t2
        t2 = r

    return t1

def generateTwoPowerLists(num):
    div = 8
    output = []
    while num:
        if num < div:
            div //= 2
        num -= div 
        output.append(div)
    
    return output

def rsa(input, powerLists, keyProduct):
    output = 1
    for val in powerLists:
        output = output * ((input ** val) % keyProduct)
    
    return output % keyProduct

p = 17
q = 11
N = p * q
phiN = (p - 1) * (q - 1)

e = 4
while gcd(e, phiN) != 1 and e < phiN:
    e += 1

d = (phiN // e) + 1

pMesLists = generateTwoPowerLists(e)
pCipLists = generateTwoPowerLists(d)

message = input("Enter a message: ")
asciiList = [ord(char) for char in message]

encryptedList = [rsa(value, pMesLists, N) for value in asciiList]
print(f"Encrypted message list is: {encryptedList}.")

decryptedList = [rsa(value, pCipLists, N) for value in encryptedList]
decryptedString = ''.join([chr(num) for num in decryptedList])
print(f"Decrypted message is: {decryptedString}.")
