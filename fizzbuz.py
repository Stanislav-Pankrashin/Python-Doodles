if __name__ == '__main__':
	for i in range(1, 101):	
		output = 'fizz' if i % 3 == 0 else ''
		output += 'buzz' if i % 5 == 0 else ''
		print(output or i)