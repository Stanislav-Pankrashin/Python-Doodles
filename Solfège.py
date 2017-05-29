import random
import winsound

for i in range(1000):
    winsound.Beep(random.randint(37, 32766), 500)