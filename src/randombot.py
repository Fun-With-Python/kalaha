import random
import time

name = "RandomBot"
def init(pnumber):
	name = name + " " + str(pnumber)

def ask():
	random.seed(time.clock())
	return random.randint(1,6)
