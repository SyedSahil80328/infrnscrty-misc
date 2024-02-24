import DESUtils

def dataEncryptionStandard(binaryText, keysList):
    permutedBinaryText = DESUtils.generatePermutation(binaryText, DESUtils.initialPermutation)
    print(f"Text after initial permutation: {permutedBinaryText}.\n")
    
    leftHalf = permutedBinaryText[:32]
    rightHalf = permutedBinaryText[32:]

    for i in range(16):    
        print(f"Iteration {i+1}:- ")
        print("Halves before round function:-")
        print(f"Left half: {leftHalf}.")
        print(f"Right half: {rightHalf}.\n")
        permutedRightHalf = DESUtils.generatePermutation(rightHalf, DESUtils.expansionPermutation)
        print(f"Expanded Right half: {permutedRightHalf}.")
        xorRightHalf = DESUtils.bitwiseXOR(permutedRightHalf, keysList[i])
        print(f"XOR({permutedRightHalf}, {keysList[i]}) = {xorRightHalf}.\n")

        xorRightLeftHalf = xorRightHalf[:24]
        xorRightRightHalf = xorRightHalf[24:]
        print(f"Divided halves: {xorRightLeftHalf} and {xorRightRightHalf}.\n")

        sBoxText = ""
        for j in range (8):
            text = xorRightHalf[6*j:6*j + 7]
            sBoxText += DESUtils.getFourBitsFromSBox(text, DESUtils.substitutionBoxes[j])

        print(f"Generated S Box text: {sBoxText}.")
        permutedSBoxText = DESUtils.generatePermutation(sBoxText, DESUtils.straightPermutation)
        print(f"Permuted S Box text: {permutedSBoxText}.")
        xorSBoxText = DESUtils.bitwiseXOR(leftHalf, permutedSBoxText)
        print(f"XOR({leftHalf}, {permutedSBoxText}) = {xorSBoxText}.\n")

        print

        (leftHalf, rightHalf) = (rightHalf, xorSBoxText)
        print("Halves after round function:-")
        print(f"Left half: {leftHalf}.")
        print(f"Right half: {rightHalf}.\n")
        print(f"Iteration {i+1} ended.\n")

    (leftHalf, rightHalf) = (rightHalf, leftHalf)
    print("Swapped Halves:-")
    print(f"Left half: {leftHalf}.")
    print(f"Right half: {rightHalf}.")
    modifiedText = DESUtils.generatePermutation(leftHalf + rightHalf, DESUtils.inversePermutation)
    print(f"After inverse permutation: {modifiedText}.\n")
    return modifiedText

plainText, key = DESUtils.readCredentials("Credentials.txt")

print(f"Plain text from the file: {plainText}.")
print(f"Key used for Cryptography process: {key}.\n")

print(f"Permutation for shrinking 64 bit key to 56 bit:-\n{DESUtils.permutationChoiceOne}.\n")
print(f"Permutation for generating round keys:-\n{DESUtils.permutationChoiceTwo}.")
keysList = DESUtils.generateKeys(key)
print("Generated Keys List:-")
for i, keyIterator in enumerate(keysList):
    print(f"Key for round {i+1}: {keyIterator}.")

print(f"\nInitial permutation for transpositioning text:-\n{DESUtils.initialPermutation}.\n")
print(f"Expansion permutation for expansion respective to round keys:-\n{DESUtils.expansionPermutation}.\n")
print(f"\nPermuatation for transpostioning contracted S Box Text:-\n{DESUtils.straightPermutation}.\n")
print(f"Inverse permutation for transposition:-\n{DESUtils.expansionPermutation}.\n")
print("S Boxes for contraction:-")
DESUtils.printBoxes()

print("\nEncryption Process.")
cipherText = dataEncryptionStandard(plainText, keysList)
print("Decryption Process.")
decryptedText = dataEncryptionStandard(cipherText, keysList[::-1])

print(f"Your {plainText} is encrypted to {cipherText}.")
print(f"Your {cipherText} is decrypted to {decryptedText}.")