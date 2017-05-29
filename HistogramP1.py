'''
Histogram Maker
'''
import collections, sys

class Histogram(object):
	
	def __init__(self, rangeXLow, rangeXHigh, rangeYLow, rangeYHigh):
		self.rangeYLow = rangeYLow
		self.rangeYHigh = rangeYHigh
		self.rangeXLow = rangeXLow
		self.rangeXHigh = rangeXHigh
		self.data = dict(zip([i for i in range(rangeXLow, rangeXHigh + 1, 10)], [0 for i in range(rangeXLow, rangeXHigh + 1, 10)]))
		
	def addData(self, column, amount):
		self.data[column] = amount
		
	def printHistogram(self):
		output = ''
		
		#first output y axis
		output += '   ' + ' '.join([str(i) for i in range(self.rangeYLow, self.rangeYHigh + 1)]) + '\n\n'
		
		#then generate the rest of the histogram
		for e in [i for i in range(self.rangeXLow, self.rangeXHigh + 1, 10)]:
			output += str(e) + '\n' + '   '
			output += '* ' * int(self.data[e])
			output += '\n'
			
		print(output)

def main():
	#first, get input
	theHist = None
	
	numLines = -1
	for line in sys.stdin:
		if theHist == None:
			splitIn = line.split()
			theHist = Histogram(int(splitIn[0]), int(splitIn[1]), int(splitIn[2]), int(splitIn[3]))
		elif numLines == -1:
			numLines = int(line.strip('\n'))
		elif numLines >= 0:
			splitIn = line.split()
			theHist.addData(int(splitIn[0]), splitIn[2])
			numLines -= 1
		else:
			break
	theHist.printHistogram()

if __name__ == '__main__':
	main()