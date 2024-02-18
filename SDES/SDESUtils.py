import random
permutationTen = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
permutationEight = [6, 3, 7, 4, 8, 5, 10, 9]
initialPermutation = [2, 6, 3, 1, 4, 8, 5, 7]
expandPermutation = [4, 1, 2, 3, 2, 3, 4, 1]
permutationFour = [2, 4, 3, 1]
inversePermutation = [4, 1, 3, 5, 7, 2, 8, 6]

xorTable = {'00': '0', '01': '1', '10': '1', '11': '0'}
binToDecTable = {'00': 0, '01': 1, '10': 2, '11': 3}
decToBinTable = {0: '00', 1: '01', 2: '10', 3: '11'}

sZero = [[1,0,3,2], [3,2,1,0], [0,2,1,3], [3,1,3,2]]
sOne = [[0,1,2,3], [2,0,1,3], [3,0,1,0], [2,1,0,3]]

def getTwoBitsFromSBox (bits, sBox):
    row = binToDecTable[bits[0] + bits[3]]
    col = binToDecTable[bits[1] + bits[2]]

    return decToBinTable[sBox[row][col]]

def generatePermutation(input, permutation, length):
    permutedInput = ""
    for i in range(length):
        permutedInput += input[permutation[i] - 1]
    
    return permutedInput

def shiftLeftKeys(key, shift):
    key1 = key[shift:5]
    key1 += key[0:shift]
    key2 = key[5+shift:]
    key2 += key[5:5+shift]

    return key1 + key2

def generateKeys(key):
    permutationKey = generatePermutation(key, permutationTen, 10)

    leftShiftKey1 = shiftLeftKeys(permutationKey, 1)
    key1 = generatePermutation(leftShiftKey1, permutationEight, 8)
    leftShiftKey2 = shiftLeftKeys(leftShiftKey1, 2)
    key2 = generatePermutation(leftShiftKey2, permutationEight, 8)

    return [key1, key2]

def getValidatedInput(inputType, length):
    loop = True
    binaryText = ""
    while loop:
        fault = 0
        binaryText = input(f"Enter {length} bit binary {inputType} without space: ")
        j = 0
        for i in binaryText:
            if i not in ['0', '1']:
                fault = 1
                break
            j += 1
        
        if fault:
            print(f"Your {inputType} is invalid. It contains characters other than 0 and 1. Enter it again correctly.\n")
        elif j != length:
            print(f"Your {inputType} has not exactly {length} characters. Enter it again correctly.\n")
        else:
            loop = False
    
    return binaryText

def bitwiseXOR(input1, input2):
    output = ''
    for i in range(len(input1)):
        output += xorTable[input1[i] + input2[i]]

    return output

def printBoxes():
    print("\nS0: ")
    for i in sZero:
        print(i)
    print("\nS1: ")
    for i in sOne:
        print(i)