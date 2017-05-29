"""
Collatz Conjecture
"""

def main():
	nOriginal = int(input('Please enter a number n>1: '))
	count = 0
	n = nOriginal
	while n != 1:
		n = n/2 if n%2 == 0 else (n*3) + 1
		count += 1
		
	print('The number of steps to reach 1 for n =', nOriginal, 'is', count, 'steps.')

if __name__ == '__main__':
	main()