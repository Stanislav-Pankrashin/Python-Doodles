#Escape The Trolls
import random
import os
import msvcrt
import threading
import math
import time
from tkinter import *

class interface():
	main_window = Tk()
	text = None
	
	def __init__(self):
		self.main_window.title("Esacpe The Trolls")
		self.main_window.geometry("800x500")
		self.text = Text(self.main_window)
		self.text.config(state=DISABLED)
		self.text.config(bg="black")
		self.text.config(fg="silver")
		self.text.pack(fill=BOTH, expand=1)
		
		# Colors
		self.text.tag_config("player", foreground="Cyan")
		self.text.tag_config("troll", foreground="Yellow")
		self.text.tag_config("finish", foreground="Light Green")

	
	def out(self,output,color = None):
		self.text.config(state=NORMAL)
		if color != None:
			self.text.insert(INSERT,output,color)
		else:
			self.text.insert(INSERT,output)
		self.text.config(state=DISABLED)
	
	def clear(self):
		self.text.config(state=NORMAL)
		self.text.delete('1.0', END)
		self.text.config(state=DISABLED)
		self.out("\nWelcome to the maze, valid commands are w, a, s, d\n")
		
	def runMainLoop(self):
		self.main_window.mainloop()
		
# Global Interface
interface = interface()

class maze(object):
	
	def __init__(self):
		self.atEnd = False
		self.dead = False
		self.maze = self.generateMaze()
		#Dimensions (y, x)
		self.dimensions = (len(self.maze), len(self.maze[0]))
		#Player Location (y, x)
		self.playerLocation = self.generateLocation()
		self.playerOrientation = 'u'
		self.viewCircleRadius = 10
		self.trolls = []
		self.trollController = 0
		self.elipseR1 = 16
		self.elipseR2 = 8
		#circle system, (Yc, Xc)
	
	
	def addTrolls(self, number):
		for i in range(number):
			self.trolls.append(troll(self))
	
	def generateMaze(self):
		#made generating of maze slightly random
		file = open("maze.txt", 'r')
		fileString = file.read()
		fileList = fileString.split("\n")
		#if a variable is 1, that operation will happen
		flipVertically = random.randrange(0,2)
		flipHorizontally = random.randrange(0,2)
		if flipVertically == 1:
			fileList.reverse()
		if flipHorizontally == 1:
			for i in range(len(fileList)):
				fileList[i] = fileList[i][::-1]
		
		file.close()
		return fileList
		
	def generateLocation(self):
		while True:
			x = random.randrange(0, self.dimensions[1])
			y = random.randrange(0, self.dimensions[0])
			if self.maze[y][x] != '#':
				return (y, x)
				
	def withinCircle(self, y, x):
		a = (x - self.playerLocation[1]) ** 2
		b = (y - self.playerLocation[0]) ** 2
		d = math.sqrt(a + b)
		return d <= self.viewCircleRadius
		
	def withinElipse(self, y, x):
		a = ((x - self.playerLocation[1]) ** 2) / (self.elipseR1 ** 2)
		b = ((y - self.playerLocation[0]) ** 2) / (self.elipseR2 ** 2)
		
		return (a + b) <= 1
	
	def moveBlock(self, previousLocation, newLocation):
		#Need to configure proper positions
		fromLoc = newLocation
		toLoc = (newLocation[0] + newLocation[0] - previousLocation[0], newLocation[1] + newLocation[1] - previousLocation[1])
		previousLocation = fromLoc
		newLocation = toLoc
		#check to see if movement is allowed
		if self.maze[newLocation[0]][newLocation[1]] != "#":
			#check to see if a troll died
			for i in range(len(self.trolls)):
				if self.trolls[i].location == newLocation:
					self.trolls.pop(i)
			#move the block, first check on which axis the block is moving
			#first check y
			if previousLocation[0] != newLocation[0]:
				oldY = self.maze[previousLocation[0]]
				newY = self.maze[newLocation[0]]
				oldY = oldY[ : previousLocation[1]] + " " + oldY[previousLocation[1] + 1 : ]
				newY = newY[ : newLocation[1]] + "#" + newY[newLocation[1] + 1 : ]
				self.maze[previousLocation[0]] = oldY
				self.maze[newLocation[0]] = newY
				return True
			#then X
			else:
				#determine if going left or right
				#going right
				if previousLocation[1] < newLocation[1]:
					line = self.maze[previousLocation[0]]
					line = line[ : previousLocation[1]] + ' '  + "#" + line[newLocation[1] + 1: ]
					self.maze[previousLocation[0]] = line
					return True
				#going left
				else:
					line = self.maze[previousLocation[0]]
					line = line[ : newLocation[1]] + "#" + " " + line[previousLocation[1] + 1: ]
					self.maze[previousLocation[0]] = line
					return True
		elif self.maze[newLocation[0]][newLocation[1]] != " ":
			return False
		return False
	
	def moveTrolls(self):
		for e in self.trolls:
			e.randomMove()			
	
	def printMaze(self):
		interface.clear()
		printString = ''
		#Check to see if it is time for the trolls to move
		if self.trollController >= 50:
			self.moveTrolls()
			self.trollController = 0
		else:
			self.trollController += 1
		trollLocations = []
		for e in self.trolls:
			trollLocations.append(e.location)
		#check to see if player lost
		if self.playerLocation in trollLocations:
			interface.out("Oh no you died!")
			self.atEnd = True
			self.dead = True
			return
		
		for i in range(self.dimensions[0]):
			for j in range(self.dimensions[1]):
				if self.maze[i][j] == "#" and self.withinElipse(i, j):
					printString = printString + "█"
				elif self.maze[i][j] == "X":
					interface.out(printString)
					printString = ""
					interface.out("X","finish")
				elif self.playerLocation == (i, j):
					interface.out(printString)
					printString = ""
					if self.playerOrientation == 'u':
						interface.out("^","player")
					elif self.playerOrientation == 'l':
						interface.out("<","player")
					elif self.playerOrientation == 'r':
						interface.out(">","player")
					elif self.playerOrientation == 'd':
						interface.out("v","player")
				else:
					if (i, j) in trollLocations and self.withinElipse(i, j):
						interface.out(printString)
						printString = ""
						interface.out("T","troll")
					else:
						printString = printString + " "
						
			printString = printString + "\n"
		interface.out(printString)
		if not self.atEnd or not self.dead:
			interface.main_window.after(10, self.printMaze)
		
	def checkLocationPlayer(self, previousLocation, newLocation):
		x,y = newLocation
		if self.maze[x][y] == 'X':
			self.atEnd = True
		#return self.moveBlock(previousLocation, newLocation)
		if self.maze[x][y] == "#":
			return self.moveBlock(previousLocation, newLocation)
		return True
		#return self.maze[x][y] != "#"
	def checkLocationTroll(self, coOrds):
		x,y = coOrds
		return self.maze[x][y] != "#"
		
	
class player(object):
		
		def __init__(self, maze):
			self.location = maze.playerLocation
			self.orientation = 'u'
			self.theMaze = maze
			
			#interface.main_window.after(1000, self.theMaze.printMaze)
			interface.main_window.bind('<Key>', self.move)		
		def move(self, event):
			key = event.char
			previousPosition = self.location
			if key == 'a' and self.orientation == 'l': 	self.location = self.location[0], self.location[1] - 1
			elif key == 'd' and self.orientation == 'r': 	self.location = self.location[0], self.location[1] + 1
			elif key == 'w' and self.orientation == 'u': 	self.location = self.location[0] - 1, self.location[1]
			elif key == 's' and self.orientation == 'd': 	self.location = self.location[0] + 1, self.location[1]
			elif key == 'a' and self.orientation != 'l': 	
				self.orientation = 'l' 
				self.theMaze.playerOrientation = "l"
			elif key == 'd' and self.orientation != 'r': 	
				self.orientation = 'r'
				self.theMaze.playerOrientation = "r"
			elif key == 'w' and self.orientation != 'u': 	
				self.orientation = 'u'
				self.theMaze.playerOrientation = "u"
			elif key == 's' and self.orientation != 'd':	
				self.orientation = 'd' 
				self.theMaze.playerOrientation = "d"
			
			if self.theMaze.checkLocationPlayer(previousPosition, self.location): self.theMaze.playerLocation = self.location
			else: self.location = previousPosition

			#interface.clear()
			
			if(self.theMaze.atEnd):
				if self.theMaze.dead:
					interface.out("Oh no you died!")
				else:
					interface.out("Congratulations!")
			
			else:
				pass
				#self.theMaze.printMaze()
			
class troll(object):
		def __init__(self, maze):
			self.maze = maze
			self.location = maze.generateLocation()
			
		def randomMove(self):
			moves = ['l', 'r', 'u', 'd']
			move = moves[random.randrange(4)]
			previousPosition = self.location
			newPosition = self.move(move)
			
			if not self.maze.checkLocationTroll(newPosition):
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
class main(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		self.setupMaze()
		self.updateScreen()
	
	def setupMaze(self):
		self.theMaze = maze()
		self.theMaze.addTrolls(32)
		self.thePlayer = player(self.theMaze)
		interface.out("\nWelcome to the maze, valid commands are w, a, s, d\n")
	
	def updateScreen(self):
		self.theMaze.printMaze()
			
	def checkWinCondition(self):
		if(self.theMaze.atEnd):
			if self.theMaze.dead:
				interface.out("Oh no you died!")
			else:
				interface.out("Congratulations!")
				
if __name__ == "__main__":
	mainThread = main()
	mainThread.start()
	interface.runMainLoop()