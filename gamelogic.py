import outputgametable as out
import sys

player1 = "Player 1"
player2 = "Player 2"
out.output()
while 1:
	try:
		inp = int(input(player1 + ", please insert a number between 1-6: "))
	except ValueError:
		print("Couldn\'t convert to Integer")
		continue
	except KeyboardInterrupt:
		print("\n  ^C detected, terminating...")
		sys.exit()
	except EOFError:
		print("\n  ^D detected, terminating...")
		sys.exit()
	
	if inp < 1 or inp > 6:
		print ("Out of range (1 - 6)")
		continue
