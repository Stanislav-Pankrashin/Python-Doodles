"""
manual creation vs list comprehension
"""
import time

def main():
	timeStart = time.clock()
	theList1 = [i for i in range(10000000)]
	timeStop = time.clock()
	print('comprehension: ')
	print(timeStop - timeStart)
	timeStart = time.clock()
	theList2 = []
	for i in range(10000000):
		theList2.append(i)
	timeStop = time.clock()
	print('loop: ')
	print(timeStop - timeStart)
	
	
if __name__ == '__main__':
	main()