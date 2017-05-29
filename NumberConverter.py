"""
Number Names
"""
NUMBERS = ['' ,'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
TEENS = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
TENS = ['', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
GROUPS = ['Million', 'Thousand', '']

def printOutput(output):
	
	if len(output) > 1:
		finalOutput = output[1:]
		finalOutput = ', '.join(finalOutput[::-1])
		finalOutput = finalOutput + ' And ' + output[0] if output[0] != '' else finalOutput
	else:
		finalOutput = output[0]
	finalOutput = finalOutput.strip('-')
	print(finalOutput)

def convertHundreds(hundred):
	output = ''
	#first check to see if it is a 'compound'
	if not hundred[1] == '0':
		if hundred[1] == '1':
			output += convertTeens(hundred[1:])
		else:
			output += convertTens(hundred[1:])
	elif not hundred[2] == '0':
		output += convertOnes(hundred[2])
		
	if not output:
		output = convertOnes(hundred[0]) + '-Hundred'
		if output == '-Hundred':
			output = ''
	else:
		output = convertOnes(hundred[0]) + '-Hundred' + '-And-' + output
		if output[0] == '-':
			outputSplit = output.split('-')
			output = outputSplit[-1].strip('-')
	
	return output
	
def convertTeens(teens):
	return TEENS[int(teens[1])]
	
def convertTens(tens):
	output = TENS[int(tens[0]) - 1] + '-' + convertOnes(int(tens[1]))
	return output
	
def convertOnes(ones):
	return NUMBERS[int(ones)]

def convertBlock(element, denominator):
	output = ''
	if len(element) == 1:
		output += convertOnes(element)
	elif len(element) == 2:
		if element[0] == '1':
			output += convertTeens(element)
		else:
			output += convertTens(element)
	elif len(element) == 3:
		output += convertHundreds(element)
	
	output = output + '-' + denominator if denominator and not output == '' else output
	return output
		
def processNumber(number):
	#Number Format
	#0 000 000
	number = number
	#first break number up into smaller parts
	numList = []
	for i in range(len(number) // 3):
		numList.append(number[ - 3:])
		number = number[:-3]
	numList.append(number)
	
	output = []
	#convert Number
	try:
		numList.remove('')
	except:
		pass
	for i in range(len(numList)):
		output.append(convertBlock(numList[i], GROUPS[-(i + 1)]))
		
	printOutput(output)
	
def main():
	toEnd = False
	while not toEnd:
		theInput = input('Enter Number To Be Converted: ')
		if theInput.upper() == 'END':
			toEnd = True
			break
		
		processNumber(theInput)

if __name__ == '__main__':
	main()