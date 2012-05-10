import gamelogic as game

p1bot = input('Is Player 1 a bot? (y/n) ')
if p1bot == 'y':
	game.isp1bot = 1
else:
	game.isp1bot = 0

p2bot = input('Is Player 2 a bot? (y/n) ')
if p2bot == 'y':
	game.isp2bot = 1
else:
	game.isp2bot = 0

if p1bot == 'n':
	game.player1 = input('Input name for Player 1: ')
else:
	game.player1 = "Bot 1"

if p2bot == 'n':
	game.player2 = input('Input name for Player 2: ')
else:
	game.player2 = "Bot 2"

game.main()
