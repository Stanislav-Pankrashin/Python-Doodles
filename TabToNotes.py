'''
Tab to Note name converter
'''
import sys

NOTES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", 'F', "F#", "G", "G#"]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
OCTAVES = [4, 3, 3, 3, 2, 2]
STRINGS = ['E', 'B', 'G', 'D', 'A', 'E']

def getTab():
	tab = ''
	print('Please enter tab to be converted:')
	strings = 1
	for e in sys.stdin:
		if 'end' in e.lower():
			return e
		elif strings < 6:
			tab += e
			strings += 1
		elif strings == 6:
			tab += e
			return tab
		else:
			return tab
		
def getNote(currentStringIndex, fret):
	currentOctave = OCTAVES[currentStringIndex]
	if int(fret) >= 12:
		currentOctave += 1
	if int(fret) == 24:
		currentOctave += 1
	#check to see if it passes c
	for i in range(int(fret)):
		if NOTES[(NOTES.index(STRINGS[currentStringIndex]) + int(fret)) % 12] == 'C':
			currentOctave += 1
			break
	note = NOTES[(NOTES.index(STRINGS[currentStringIndex]) + int(fret)) % 12] + str(currentOctave)
	return note

def processTab(tab):
	output = ''
	splitTab = tab.split('\n')
	splitTab = splitTab[ : 6]
	tabLen = len(splitTab[1])
	currentIndex = 0
	while currentIndex < tabLen:
		for i in range(len(splitTab)):
			try:
				if splitTab[i][currentIndex : currentIndex + 2] in NUMBERS:
					currentString = splitTab[i][0]
					fret = splitTab[i][currentIndex: currentIndex + 2]
					output += getNote(i, fret) + ' '
					currentIndex += 1
				elif splitTab[i][currentIndex] in NUMBERS:
					currentString = splitTab[i][0]
					fret = splitTab[i][currentIndex]
					output += getNote(i, fret) + ' '
					currentIndex += 1
					continue
			except:
				pass
		currentIndex += 1
	print(output)
				
def main():
	tab = getTab()
	if 'end' in tab.lower():
		return True
	
	processTab(tab)

if __name__ == '__main__':
	done = False
	while not done:
		end = main()
		if end:
			done = True