#Test Radix
import Radix
import time
import mergeSort

def test():
	with open('data.txt', 'r') as f:
		fileString = f.read()
		fileSplit = fileString.split('\n')
		fileSplit = fileSplit[ : -2 ]
	
	toSort = [int(e) for e in fileSplit]
	before = time.clock()
	sorted = Radix.radixSort(toSort)
	after = time.clock()
	print("Time for Radix is {0}".format(after - before))
	before = time.clock()
	pythonSorted = toSort.sort()
	after = time.clock()
	print("Time for timsort is {0}".format(after - before))
	
if __name__ == '__main__':
	test()