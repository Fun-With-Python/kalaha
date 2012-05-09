import outputgametable as out
import sys
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

player1 = "Player 1"
player2 = "Player 2"
while 1:
	print("*")
	out.output()
	print("\033[31;42m*\033[m")
	inp = safeinputint(player1 + ", please insert a number between 1-6: ")
	
