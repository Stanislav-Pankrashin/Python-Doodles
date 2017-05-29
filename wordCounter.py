'''
Counts the number of words in a given input string
'''

def main():
	#super simple brute force
	theInput = input('Enter word to be checked: ')
	
	theDict = []
	with open('enable1.txt', 'r') as f:
		theDict = f.read()
		theDict = theDict.split('\n')
		
	count = 0
	for e in theDict:
		if e in theInput:
			count += 1
			
	print('Count:', count)

if __name__ == '__main__':
	main()