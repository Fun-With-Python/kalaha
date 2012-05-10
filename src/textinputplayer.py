name = "Player"
def init(pnumber):
	name = input("Input name for Player "+str(pnumber)+": ")

def ask():
	random.seed(time.clock())
	return random.randint(1,6)
