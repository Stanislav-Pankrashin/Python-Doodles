def main():
	theInput = input('Enter word to be checked: ')
	print('Palindrome!'*(theInput == theInput[::-1]) or 'Not Palindrome')

if __name__ == '__main__':
	while True:
		main()
