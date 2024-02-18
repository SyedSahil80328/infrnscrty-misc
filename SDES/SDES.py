import SDESUtils

def simpleStandardEncryptionStandard(binaryText, keysList):
    print(f"Initial permutation is defined as: {SDESUtils.initialPermutation}.")
    permutedBinaryText = SDESUtils.generatePermutation(binaryText, SDESUtils.initialPermutation, 8)
    print(f"Text after initial permutation: {permutedBinaryText}.\n")
    
    leftHalf = permutedBinaryText[:4]
    rightHalf = permutedBinaryText[4:]
    print(f"Two halves: {leftHalf} and {rightHalf}.")
    print(f"Expansion permutation is defined as: {SDESUtils.expandPermutation}")
    permutedRightHalf = SDESUtils.generatePermutation(rightHalf, SDESUtils.expandPermutation, 8)
    print(f"Expanded Right half: {permutedRightHalf}.")
    xorRightHalf = SDESUtils.bitwiseXOR(permutedRightHalf, keysList[0])
    print(f"XOR({permutedRightHalf}, {keysList[0]}) = {xorRightHalf}.\n")

    xorRightLeftHalf = xorRightHalf[:4]
    xorRightRightHalf = xorRightHalf[4:]
    print(f"Divided halves: {xorRightLeftHalf} and {xorRightRightHalf}.")
    print(f"S Boxes are defined as:")
    SDESUtils.printBoxes()

    sBoxText = SDESUtils.getTwoBitsFromSBox(xorRightLeftHalf, SDESUtils.sZero) + SDESUtils.getTwoBitsFromSBox(xorRightRightHalf, SDESUtils.sOne)
    print(f"Generated S Box text: {sBoxText}")
    print(f"Permuatation for S Box Text is defined as: {SDESUtils.permutationFour}.")
    permutedSBoxText = SDESUtils.generatePermutation(sBoxText, SDESUtils.permutationFour, 4)
    print(f"Permuted S Box text: {permutedSBoxText}.")
    xorSBoxText1 = SDESUtils.bitwiseXOR(leftHalf, permutedSBoxText)
    print(f"XOR({leftHalf}, {permutedSBoxText}) = {xorSBoxText1}. (Kept for doing IP^-1 with another S Box text.)\n")

    permutedLeftHalf = SDESUtils.generatePermutation(xorSBoxText1, SDESUtils.expandPermutation, 8)
    xorLeftHalf = SDESUtils.bitwiseXOR(permutedLeftHalf, keysList[1])
    print(f"XOR({permutedLeftHalf}, {keysList[1]}) = {xorLeftHalf}.\n")

    xorLeftLeftHalf = xorLeftHalf[:4]
    xorLeftRightHalf = xorLeftHalf[4:]
    print(f"Divided halves: {xorLeftLeftHalf} and {xorLeftRightHalf}.")

    sBoxText = SDESUtils.getTwoBitsFromSBox(xorLeftLeftHalf, SDESUtils.sZero) + SDESUtils.getTwoBitsFromSBox(xorLeftRightHalf, SDESUtils.sOne)
    print(f"Generated S Box text: {sBoxText}")
    permutedSBoxText = SDESUtils.generatePermutation(sBoxText, SDESUtils.permutationFour, 4)
    print(f"Permuted S Box text: {permutedSBoxText}.")
    xorSBoxText2 = SDESUtils.bitwiseXOR(rightHalf, permutedSBoxText)
    print(f"XOR({rightHalf}, {permutedSBoxText}) = {xorSBoxText2}.\n")

    print(f"Inverse Permutation is defined as: {SDESUtils.inversePermutation}.")
    modifiedText = SDESUtils.generatePermutation(xorSBoxText2 + xorSBoxText1, SDESUtils.inversePermutation, 8)
    print(f"After inverse permutation: {modifiedText}.\n")
    return modifiedText

plainText = SDESUtils.getValidatedInput("plain text", 8)
key = SDESUtils.getValidatedInput("key", 10)

print(f"Permutation for key generation is defined as: {SDESUtils.permutationTen}")
keysList = SDESUtils.generateKeys(key)
print(f"Generated Keys: {keysList}\n")

print("Encryption Process.")
cipherText = simpleStandardEncryptionStandard(plainText, keysList)
print("Decryption Process.")
decryptedText = simpleStandardEncryptionStandard(cipherText, [keysList[1], keysList[0]])

print(f"Your {plainText} is encrypted to {cipherText}.")
print(f"Your {cipherText} is decrypted to {decryptedText}.")