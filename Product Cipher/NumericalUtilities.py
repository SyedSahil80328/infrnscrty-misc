import copy
def findFactors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i*i)
    return factors

def determinant(mat):
	if len(mat) == 1:
		return mat[0][0]
	if len(mat) == 2:
		return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])
	det = 0
	for i in range (len(mat)):
		power = (-1) ** (i+2)
		factor = mat[0][i] * power
		smallMatrix = copy.deepcopy(mat[1:])
		for j in range (len(smallMatrix)):
			del smallMatrix[j][i]
		det = det + (factor * determinant(smallMatrix))
	return det

def transpose(mat):
	out = [[] for i in range(len(mat[0]))]
	for i in range (len(mat)):
		for j in range (len(mat[i])):
			out[j].append(mat[i][j])
	return out

def convertEverythingToPositive(matrix):
	out = []
	for row in matrix:
		out.append([])
		for element in row:
			while (element < 0):
				element += 26
			out[len(out) - 1].append(element)
	return out	

def absoluteAdjoint(mat):
	if len(mat) == 1:
		return mat
	
	out = []
	for i in range(len(mat)):
		out.append([])
		for j in range(len(mat[i])):
			power = (-1) ** (i+j+2)
			mycopy = copy.deepcopy(mat)
			del mycopy[i]
			for k in range (len(mycopy)):
				del mycopy[k][j]
			
			out[i].append(power * determinant(mycopy))

	actualOutput = convertEverythingToPositive(out)
	
	return transpose(actualOutput)
	
def moduloMultiplicativeInverse(det):
	i = 1
	while (det * i)%26 != 1:
		i += 2	
	return i 
	
def matrixMultiplication(matrix1, matrix2):
	output = []
	for i in range (len(matrix1)):
		output.append([])
		for j in range (len(matrix2[0])):
			sum = 0
			for k in range (len(matrix1[0])):
				sum = sum + (matrix1[i][k] * matrix2[k][j])
			output[i].append(sum % 26)
	return output

def printMatrix(matrix):
	for row in matrix:
		print(row)

def printMatrices (matrices):
    i = 1
    for matrix in matrices:
        print(f"Matrix {i}:-")
        for row in matrix:
            print(row)
        i += 1

def modularInverse (matrix, determinant):
	adjoint = absoluteAdjoint(matrix)
	invDeterminant = moduloMultiplicativeInverse(determinant)

	invMatrix = []
	temp = 0
	for row in adjoint:
		invMatrix.append([])
		for element in row:
			temp = invDeterminant * element
			invMatrix[len(invMatrix) - 1].append(temp % 26)
	
	return invMatrix


