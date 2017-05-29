"""
Ricochet
"""
import sys
class Grid(object):
	def __init__(self, height, width, velocity):
		self.height = int(height)
		self.width = int(width)
		self.velocity = int(velocity)
		self.corners = [[self.height, 0], [0, self.width], [self.height, self.width]]
		self.positionalDict = dict(zip([str(e) for e in self.corners], ['LL', 'UR', 'LR']))
		self.position = [0, 0]
		self.rebounds = 0
		self.turns = 0
		
	def simulate(self):
		heightIncrement = 1
		widthIncrement = 1
		
		while True:
			self.turns += 1 / self.velocity
			self.position[0] += heightIncrement
			self.position[1] += widthIncrement
			if self.position in self.corners:
				return self.positionalDict[str(self.position)] + ' ' + str(self.rebounds) + ' ' + str(int(self.turns))
			if self.position[0] == 0 or self.position[0] == self.height:
				self.rebounds += 1
				heightIncrement = -heightIncrement
			if self.position[1] == 0 or self.position[1] == self.width:
				self.rebounds += 1
				widthIncrement = -widthIncrement

def main():
	for line in sys.stdin:
		if 'end' in line.lower():
			return
		lineSplit = line.split()
		theGrid = Grid(lineSplit[0], lineSplit[1], lineSplit[2])
		print(theGrid.simulate())

if __name__ == '__main__':
	main()
	
	