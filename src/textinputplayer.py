import sys

name = "Player"
def safeinputint(text):
	try:
		inp = int(input(text))
	except ValueError:
		print("Couldn\'t convert to Integer")
		return safeinputint(text)
	except KeyboardInterrupt:
		print("\n  ^C detected, terminating...")
		sys.exit()
	except EOFError:
		print("\n  ^D detected, terminating...")
		sys.exit()
	
	if inp < 1 or inp > 6:
		print ("Out of range (1 - 6)")
		return safeinputint(text)
	else:
		return inp

def init(pnumber):
	name = input("Input name for Player "+str(pnumber)+": ")

def ask():
	return safeinputint(name + ", please insert a number between 1-6: ")

