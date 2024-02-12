def encodeFence(text, key):
	rail = [['\n' for _ in range(len(text))] for _ in range(key)]
	
	dirDown = False
	row, col = 0, 0
	
	for i in range(len(text)):
		if (row == 0) or (row == key - 1):
			dirDown = not dirDown
		
		rail[row][col] = text[i]
		col += 1
		
		if dirDown:
			row += 1
		else:
			row -= 1
	result = []
	for i in range(key):
		for j in range(len(text)):
			if rail[i][j] != '\n':
				result.append(rail[i][j])
	return("" . join(result))
	
def decodeFence(cipher, key):
	rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
	
	dirDown = None
	row, col = 0, 0
	
	for i in range(len(cipher)):
		if row == 0:
			dirDown = True
		if row == key - 1:
			dirDown = False
		
		rail[row][col] = '*'
		col += 1
		
		if dirDown:
			row += 1
		else:
			row -= 1
			
	index = 0
	for i in range(key):
		for j in range(len(cipher)):
			if ((rail[i][j] == '*') and (index < len(cipher))):
				rail[i][j] = cipher[index]
				index += 1
		
	result = []
	row, col = 0, 0
	for i in range(len(cipher)):
		if row == 0:
			dirDown = True
		if row == key-1:
			dirDown = False
			
		if (rail[row][col] != '*'):
			result.append(rail[row][col])
			col += 1
			
		if dirDown:
			row += 1
		else:
			row -= 1
	return("".join(result))
