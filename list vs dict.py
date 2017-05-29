"""
List vs theDictionary Indexing
"""
import time

def main():
	list = [i for i in range(1000000)]
	theDict = dict(zip([i for i in range(1000000)], [i for i in range(1000000)]))
	listTimes = []
	theDictTimes = []
	
	#test times and add to lists
	
	#first list
	for i in range(len(list)):
		start = time.clock()
		var = list[i]
		stop = time.clock()
		listTimes.append(stop - start)
		
	#then theDict
	for i in range(len(theDict)):
		start = time.clock()
		var = theDict[i]
		stop = time.clock()
		theDictTimes.append(stop - start)
		
	#print averages
	
	print("average times for indexing every element")
	print('List:', sum(listTimes) / len(listTimes))
	print('theDict:', sum(theDictTimes) / len(theDictTimes))
if __name__ == '__main__':
	main()