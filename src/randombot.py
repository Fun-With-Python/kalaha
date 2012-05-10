import random
import time
def ask():
	random.seed(time.clock())
	return random.randint(1,6)
