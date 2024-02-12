import math
import random

letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(' ')

def convertStringToMatrix(string, keyLength):
    stringMatrix = []
    j = -1
    i = 0
    while i < len(string):
        if i % keyLength == 0:
            stringMatrix.append([])
            j += 1
        stringMatrix[j].append([ord(string[i]) - 65])
        i += 1
    return stringMatrix

def convertMatrixToString(stringMatrix):
    string = ""
    for matrix in stringMatrix:
        for row in matrix:
            for element in row:
                string += chr(element + 65)
    return string

def convertKeyToMatrix(key):
    rows = int(math.sqrt(len(key)))
    key = key.upper()

    keyMatrix = []
    for i in range(rows):
        keyMatrix.append([])
        for j in range(rows):
            keyMatrix[i].append(ord(key[i*rows + j]) - 65)
    
    return keyMatrix



    
