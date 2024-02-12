from AlphabeticalUtilities import convertStringToMatrix, convertMatrixToString
from NumericalUtilities import matrixMultiplication, modularInverse

def encode(string, keyMatrix):
    stringMatrix = convertStringToMatrix(string, len(keyMatrix))
    encodedMatrix = []
    for matrix in stringMatrix:
        encodedMatrix.append(matrixMultiplication(keyMatrix, matrix))
    
    encodedString = convertMatrixToString(encodedMatrix)
    return encodedString

def decode(string, keyMatrix, det):
    inverseKeyMatrix = modularInverse(keyMatrix, det)
    return encode(string, inverseKeyMatrix) #Remaining process of Decryption is same as Encryption
