"""
Free Time Checker
"""

def getTimes(personDict, days, times):
	for e in days:
		print(e + ':')
		for i in range(len(times)):
			free = input(times[i] + ': ')
			if not free.upper() == 'Y':
				personDict[e][i] = False
				
def findFreeTimes(person1DaysDict, person2DaysDict, days, times):
	print('Free Times\n')
	for e in days:
		print(e)
		for i in range(len(times)):
			if person1DaysDict[e][i] and person2DaysDict[e][i]:
				print(times[i])
	
def main():
	days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
	times = ['9-10', '10-11', '11-12', '12-13','13-14' , '14-15', '15-16', '16-17']
	#if a slot is free, it will be true
	person1DaysDict = dict(zip(days, [[True for e in times] for e in times]))
	person2DaysDict = dict(zip(days, [[True for e in times] for e in times]))
	
	print("person 1")
	getTimes(person1DaysDict, days, times)
	print("person 2")
	getTimes(person2DaysDict, days, times)
	
	findFreeTimes(person1DaysDict, person2DaysDict, days, times)
	
if __name__ == '__main__':
	main()