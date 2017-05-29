"""
sieve of erathenes
"""

def main():
	numPrimes = 0
	num = 1000000
	seenDict = dict(zip([i for i in range(num)], [True for i in range(num)]))
	for i in range(2, num):
		if seenDict[i]:
			seenDict[i] = False
			numPrimes += 1
			multiplier = i
			current = i ** 2
			while current <= num:
				seenDict[current] = False
				current += multiplier
		else:
			pass
			
	print(numPrimes + 1)
		

if __name__ == '__main__':
	main()