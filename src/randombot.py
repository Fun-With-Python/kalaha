import random
import time
	
def init(pnumber):
	global name
	name = "RandomBot " + str(pnumber)

def ask():
	random.seed(time.clock())
	return random.randint(1,6)
