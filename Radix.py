'''
Radix sort on a collection of integers
'''

def radixSort(collection):
	#first convert each element to a string, and also find the longest element
	stringCollection = [str(e) for e in collection]
	highestSigFig = len(max(stringCollection, key = len))
		
	#now start the sort
	#first create a dictionary of queues
	numbers = [str(i) for i in range(0, 10)]
	queues = [[]for i in range(0, 10)]
	queuePool = dict(zip(numbers, queues))
	
	#then begin sort
	sorted = []
	for i in range(highestSigFig):
		sorted = []
		for e in stringCollection:
			try:
				queuePool[e[-(i + 1)]].append(e)
			except:
				queuePool['0'].append(e)	
		for e in numbers:
			sorted += queuePool[e]
			queuePool[e] = []
			
		stringCollection = sorted
	#Convert Back To Int
	final = [int(e) for e in stringCollection]
	return final
	
