import outputgametable as out
#you can also import different bots
#they only need to have a init(string) and a ask() function which returns an integer between 1-6
import randombot as p1
import textinputplayer as p2
import sys

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

## is playerX a bot?
#isp1bot = 0
#isp2bot = 1
#
#player1 = "Player 1"
#player2 = "Player 2"

def main():
	p1.init()
	p2.init()
	while 1:
		#Player1's turn
		while 1:
<<<<<<< HEAD
			print("-"+player2+"-\n")
			out.output()
			print("\033[31;42m-"+player1+"-\033[m \n")
=======
			print("-"+str(p2.name)+"-\n")
			out.output()
			print("\033[31;42m-"+str(p1.name)+"-\033[m \n")
>>>>>>> modular
			#bot or not?
			inp = p1.ask()
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
			print("Well done, "+p1.name)
			break
	
		#Player2's turn
		while 1:
<<<<<<< HEAD
			print("\033[31;42m-"+player2+"-\033[m \n")
			out.output()
			print("-"+player1+"-\n")
=======
			print("\033[31;42m-"+str(p2.name)+"-\033[m \n")
			out.output()
			print("-"+str(p1.name)+"-\n")
>>>>>>> modular
			#bot or not?
			inp = p2.ask()
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
			print("Well done, "+p2.name)
			break
main()
