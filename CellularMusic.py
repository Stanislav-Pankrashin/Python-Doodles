#Elementary Cellular automation
#Stanislav Pankrashin

import winsound

RULES = ['   ', '  *', ' * ', ' **', '*  ', '* *', '** ', '***']

def makeMusic(toWrite):
	lines = toWrite.split('\n')
	lineCounts = []
	
	#Count number of # in each line
	for e in lines:
		count = 0
		for j in e:
			if j == '#':
				count += 1
		lineCounts.append(count)
		
	
				

def getInput():
	theInput = input('Enter Input(Size Rows Rule): ')
	splitInput = theInput.split()
	
	return int(splitInput[0]), int(splitInput[1]), int(splitInput[2])
	
def convertRuleToBin(rule):
	binary = bin(rule)[2:].zfill(8)
	binary = binary[ : : -1]
	return binary
	
def automate(size, rows, binary):
	lastString = ''
	outputString = ''
	finalString = ''
	#First generate first line and output it, it's best if the size is odd
	lastString = (' ' * int((size-1) / 2)) + '*' + (' ' * int((size-1) / 2))
	finalString += lastString + '\n'
	
	#Then do the automations
	for i in range(rows - 2):
		#iterate through each character in each row and apply the rule directly below them
		for j in range(len(lastString)):
			#need to get what is to the left and right of each character, can do this using index % size + and - 1
			left = (j - 1) % size
			middle = i % size
			right = (j + 1) % size
			toCheck = lastString[left] + lastString[middle] + lastString[right]
			#then check to see if that rule is active
			if RULES[toCheck] == '1':
				outputString += '*'
			else:
				outputString += ' '
		finalString += outputString + '\n'
		lastString = outputString
		outputString = ''
		
	makeMusic(finalString)

def main():
	size, rows, rule = getInput()
	bin = convertRuleToBin(rule)
	#convert rules to a dictionary to enable constant lookup time
	global RULES 
	RULES = dict(zip(RULES, bin))
	
	automate(size, rows, bin)
	
if __name__ == "__main__":
	main()