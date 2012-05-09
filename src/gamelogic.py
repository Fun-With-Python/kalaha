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

#place - int between 1-6
#player - int between 1-2
def translate(place, player):
	place = int(place)
	player = int(player)
	if not( place < 1 or place > 6 or player < 1 or player > 2 ):
		if (player == 1):
			return "D"+str(place-1)
		else:
			return "U"+str(place-1)

player1 = "Player 1"
player2 = "Player 2"
while 1:
	#Player1's turn
	print("-*-\n")
	out.output()
	print("\033[31;42m-*-\033[m \n")
	inp = safeinputint(player1 + ", please insert a number between 1-6: ")
	#do something cool
	position = translate(inp, 1)
	value = out.score[position]
	out.score[position] = 0
	for i in range(value):
		position = out.next[position]
		out.score[position] = out.score[position] + 1

	#Player1's turn
	print("\033[31;42m-*-\033[m \n")
	out.output()
	print("-*-\n")
	inp = safeinputint(player2 + ", please insert a number between 1-6: ")
	#do something cool
	position = translate(inp, 2)
	value = out.score[position]
	out.score[position] = 0
	for i in range(value):
		position = out.next[position]
		out.score[position] = out.score[position] + 1
	
	
