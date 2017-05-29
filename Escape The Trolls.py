#Escape The Trolls
import random
import os
import msvcrt

class maze(object):
	
	def __init__(self):
		self.atEnd = False
		self.dead = False
		self.maze = self.generateMaze()
		#Dimensions (y, x)
		self.dimensions = (len(self.maze), len(self.maze[0]))
		#Player Location (y, x)
		self.playerLocation = self.generateLocation()
		self.trolls = []
	
	def addTrolls(self, number):
		for i in range(number):
			self.trolls.append(troll(self))
	
	def generateMaze(self):
		file = open("maze.txt", 'r')
		fileString = file.read()
		fileList = fileString.split("\n")
		file.close()
		return fileList
		
	def generateLocation(self):
		while True:
			x = random.randrange(0, self.dimensions[1])
			y = random.randrange(0, self.dimensions[0])
			if self.maze[y][x] != '#':
				return (y, x)

	#Clear console, to make it a bit smoother
	def cls(self):
		os.system('cls' if os.name=='nt' else 'clear')		
	
	def printMaze(self):
		self.cls()
		printString = ''
		for e in self.trolls:
			e.randomMove()
		trollLocations = []
		for e in self.trolls:
			trollLocations.append(e.location)
		#check to see if player lost
		if self.playerLocation in trollLocations:
			print("Oh no you died!")
			self.atEnd = True
			self.dead = True
			return
		
		for i in range(self.dimensions[0]):
			for j in range(self.dimensions[1]):
				if self.maze[i][j] == "#":
					printString = printString + "#"
				elif self.maze[i][j] == "X":
					printString = printString + "X"
				elif self.playerLocation == (i, j):
					printString = printString + "P"
				else:
					if (i, j) in trollLocations:
						printString = printString + "T"
					else:
						printString = printString + " "
			printString = printString + "\n"
			
		print(printString)
		
	def checkLocation(self, coOrds):
		x,y = coOrds
		if self.maze[x][y] == 'X':
			self.atEnd = True
		return self.maze[x][y] != "#"
			
	
class player(object):
		
		def __init__(self, maze):
			self.location = maze.playerLocation
					
		def move(self, input):
			key = input
			try:
				key = key
			except:
				print("Please enter a valid value")
				return self.location

			if key == b'a':
				self.location = self.location[0], self.location[1] - 1
				return (self.location)
			elif key == b'd':
				self.location = self.location[0], self.location[1] + 1
				return (self.location)
			elif key == b'w':
				self.location = self.location[0] - 1, self.location[1]
				return (self.location)
			elif key == b's':
				self.location = self.location[0] + 1, self.location[1]
				return (self.location)
			else:
				return self.location
				
				
class troll(object):
		def __init__(self, maze):
			self.maze = maze
			self.location = maze.generateLocation()
			
		def randomMove(self):
			moves = ['l', 'r', 'u', 'd']
			move = moves[random.randrange(4)]
			previousPosition = self.location
			newPosition = self.move(move)
			
			if not self.maze.checkLocation(newPosition):
				self.location = previousPosition	
			
		def move(self, input):
			key = input
			if key == 'l':
				self.location = self.location[0], self.location[1] - 1
				return (self.location)
			elif key == 'r':
				self.location = self.location[0], self.location[1] + 1
				return (self.location)
			elif key == 'u':
				self.location = self.location[0] - 1, self.location[1]
				return (self.location)
			elif key == 'd':
				self.location = self.location[0] + 1, self.location[1]
				return (self.location)
			else:
				return self.location			

				
if __name__ == "__main__":
	theMaze = maze()
	theMaze.addTrolls(8)
	thePlayer = player(theMaze)
	print("Welcome to the maze, valid commands are l, r, u, d")
	while not theMaze.atEnd:
		theMaze.printMaze()
		print("Next move: ")
		nextMove = msvcrt.getch()
		if nextMove.lower() == b'e':
			break
		previousPosition = thePlayer.location
		newPosition = thePlayer.move(nextMove)
		if theMaze.checkLocation(newPosition):
			theMaze.playerLocation = newPosition
		else:
			thePlayer.location = previousPosition
	if theMaze.dead:
		print("Oh no you died!")
	else:
		print("Congratulations!")
	input("Press Enter To Close")