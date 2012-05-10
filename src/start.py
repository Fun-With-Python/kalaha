import gamelogic as game

# Asks if Player 1 is a bot and sets the respective variable in gamelogic.py
p1bot = input('Is Player 1 a bot? (y/n) ')
if p1bot == 'y':
	isp1bot = 1
else:
	isp1bot = 0

# Asks if Player 2 is a bot and sets the respective variable in gamelogic.py
p2bot = input('Is Player 2 a bot? (y/n) ')
if p2bot == 'y':
	isp2bot = 1
else:
	isp2bot = 0

# Asks for the name for Player 1 if he isn't a bot, else it will be set to 'Bot 1'
if p1bot == 'n':
	p1name = input('Input name for Player 1: ')
else:
	p1name = "Bot 1"

# Asks for the name for Player 1 if he isn't a bot, else it will be set to 'Bot 1'
if p2bot == 'n':
	p2name = input('Input name for Player 2: ')
else:
	p2name = "Bot 2"

# Starts gamelogic and sets the previously prompted values
game.main(isp1bot, isp2bot, p1name, p2name)
