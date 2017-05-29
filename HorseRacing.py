import Radix as r


def processInput(alist):
	theList = [int(e) for e in alist[1:-1].split(',')]
	return theList

def main():
	theInput = input("Enter collection to be sorted: ")
	theInput = processInput(theInput)
	theInputUnsorted = theInput.copy()
	theInput.sort()
	
	numIterations = 0
	while theInput != theInputUnsorted:
		numIterations += 1
		theInputUnsorted = theInputUnsorted[5:] + r.radixSort(theInputUnsorted[:5])
		print(theInputUnsorted)
	print('numIterations:', numIterations)

if __name__ == "__main__":
	main()