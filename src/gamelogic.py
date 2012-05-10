import outputgametable as out
#you can also import different bots
#they only need to have a ask askbot() function which returns an integer between 0-6
import bot as p1bot
import randombot as p2bot
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


# is playerX a bot?
isp1bot = 0
isp2bot = 1

player1 = "Player 1"
player2 = "Player 2"

def main(): 
	while 1:
		#Player1's turn
		while 1:
			print("-*-\n")
			out.output()
			print("\033[31;42m-*-\033[m \n")
			#bot or not?
			if isp1bot:
				inp = p1bot.askbot()
				print ("Bot 1 sowed the seeds from house: "+str(inp))
			else:
				inp = safeinputint(player1 + ", please insert a number between 1-6: ")
			#do something cool
			position = translate(7-inp, 1)
			value = out.score[position]
			out.score[position] = 0
			#dirstribute the points
			for i in range(value):
				position = out.next[position]
				out.score[position] = out.score[position] + 1
			#exit condition for Player1's turn
			if inp != value:
				#capturing seeds ?
				if out.score[position] == 1 and out.side[position]==1 and out.score[position.replace("D","U")]>0:
					out.score["R_"] = out.score["R_"] + out.score[position] + out.score[position.replace("D","U")]
					out.score[position] = 0
					#opposit house
					out.score[position.replace("D","U")] = 0
				break
		#win condition for Player1, a player wins if he/she has more than the half of all possible points
		if out.score["R_"] > out.sph*6:
			print("Well done, "+player1)
			break
	
		#Player2's turn
		while 1:
			print("\033[31;42m-*-\033[m \n")
			out.output()
			print("-*-\n")
			#bot or not?
			if isp2bot:
				inp = p2bot.askbot()
				print ("Bot 2 sowed the seeds from house: "+str(inp))
			else:
				inp = safeinputint(player2 + ", please insert a number between 1-6: ")
			position = translate(inp, 2)
			value = out.score[position]
			out.score[position] = 0
			#dirstribute the points
			for i in range(value):
				position = out.next[position]
				out.score[position] = out.score[position] + 1
			#exit condition for Player2's turn
			if inp != value:
				#capturing seeds ?
				if out.score[position] == 1 and out.side[position]==2 and out.score[position.replace("U","D")]>0:
					out.score["L_"] = out.score["L_"] + out.score[position] + out.score[position.replace("U","D")]
					out.score[position] = 0
					#opposit house
					out.score[position.replace("U","D")] = 0
				break
		#win condition for Player2, a player wins if he/she has more than the half of all possible points
		if out.score["L_"] > out.sph*6:
			print("Well done, "+player2)
			break
	
#bottest
