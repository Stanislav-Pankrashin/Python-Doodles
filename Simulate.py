import random

def simulate():
	iterations = 10000
	ac = 16
	scorchingRay = []
	guidingBolt = []
	for i in range(iterations):
		#scorching Ray
		attacks = []
		for i in range(1, 4):
			attacks.append(random.randrange(1, 21) + 6)
		turnDamage = 0
		for e in attacks:
			if e == 20:
				turnDamage += random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7)
			elif e >= ac:
				turnDamage += random.randrange(1, 7) + random.randrange(1, 7)
		scorchingRay.append(turnDamage)
		
		#guiding bolt
		attack = random.randrange(1, 21) + 6
		damage = 0
		if attack == 20:
			damage += random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7)
		elif attack >= ac:
			damage += random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7) + random.randrange(1, 7)
		guidingBolt.append(damage)
		
	scorchingRayTotal = sum(scorchingRay)
	scorchingRayAvg = scorchingRayTotal / iterations
	guidingBoltTotal = sum(guidingBolt)
	guidingBoltAvg = guidingBoltTotal / iterations	
		
	outputStr = '\
	ScorchingRay:\n\
		Total: {0}\n\
		Avg: {1}\n\
	\n\
	GuidingBolt:\n\
		Total: {2}\n\
		Avg: {3}'.format(scorchingRayTotal, scorchingRayAvg, guidingBoltTotal, guidingBoltAvg)
	print(outputStr)
	input("Press Enter To Quit")
			
		
	
if __name__ == '__main__':
	simulate()
	
	