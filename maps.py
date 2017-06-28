from sys import exit
from random import randint
import wSize
import clsw
import time


class Inventory(object):

    def __init__(self):
        self.gold = 50
        self.inv = ['Rusty sword', 'Torch']
        self.chest = []

    def inventoryList(self):
        for i in self.inv:
            print i

    def chestList(self):
        if not self.chest:
            print '<empty>'
        for i in self.chest:
            print i


playerCharacter = Inventory()

class store(object):

    def __init__(self):
        self.inv = {'Health potion': 120,
         'Barbed sword': 350,
         'Ration': 50,
         'Torch': 20}


playerStore = store()

class gameItems(object):
    ItemVal = {'Health potion': 120,
     'Barbed sword': 350,
     'Ration': 50,
     'Rusty sword': 70,
     'Torch': 20,
	 'Troll key': None,
	 'Rope': None}


class windowAction(object):

    def __init__(self):
        time.sleep(1)
        clsw.RefreshWindow()


class Choice(object):

    def __init__(self):
        self.pChoice = raw_input('> ')


class lists(object):
	enter = ['enter', 'Enter', 'forward', 'Forward', 'go in', 'Go in', 'go on',
				'Go on','continue', 'Continue' ,'go forward', 'Go through', 'go through', 
				'walk in', 'Walk in', 'go down', 'Go down', 'descend', 'Descend']
	back = ['back', 'Back', 'Leave', 'leave', 'no', 'No']
	townList = ['town', 'Town', 'back', 'go back', 'leave', 'Leave']
	storeList = ['left', 'Left', 'go left', 'store', 'Store']
	houseList = ['right', 'Right', 'go right', 'house', 'House']
	dungeonList = ['dungeon', 'Dungeon', 'forward', 'entrance', 'go entrance', 
					'descend', 'go down', 'enter', 'Enter', 'walk in', 'Walk in', 'Go in', 'go in']
	buyChoice = ['Health potion', 'Barbed sword', 'Ration', 'Rusty sword', 'Torch']
	house = [	['Chest', 'chest', 'open chest', 'Open chest'], 
				['Bed', 'bed', 'sleep', 'Sleep']
				]
	battle = [	['attack', 'Attack'], 
				['sword', 'swing sword', 'use sword'],
				['legs', 'leg', 'kick', 'Kick'],
				['hands', 'hand', 'punch', 'Punch', 'fists', 'fist', 'Fists', 'Hands', 'Hand']
				]
	battleLog = []
	gnollState = [True]
	trollState = [True]
	orcState = [True]
	knightState = [True]
	gargState = [False]
	gargStoned = True
	dungeon2 = [['open', 'Open', 'open door', 'use key'],
				['forward', 'continue', 'walk forward', 'walk'],
				['descend', 'Descend', 'Jump down', 'jump', 'Jump', 'jump down'],
				['loot', 'Loot', 'take key', 'Take key', 'take', 'Take', 'key', 'Key']]
	goldRoomState = [True, True]
	goldRoom = ['take sack', 'open sack', 'take', 'Take']
	dungeon3path = [['North', 'north'], 
					['South', 'south'], 
					['East', 'east'], 
					['West', 'west']]
	chosenPath = []
	dungeon3 = [['Left', 'left'], ['Right', 'right']]
	orcLoot = ['loot', 'Loot', 'take rope', 'Take rope', 'take', 'Take', 'rope', 'Rope']
	damagePC = []
	positionSwitch = False
	dungeon4 = [['swing at joint', 'attack joint', 'Swing at joint', 'Attack joint'],
				['forward', 'continue', 'walk forward', 'walk'],
				['take', 'Take', 'take chalice', 'Take chalice', 'Chalice', 'chalice']]
	plate = False
	

class Dead(object):

	def Gnoll(self):
		print 'You squander your chance to do anything useful. The gnoll drives the pickaxe through your chest!'
		print 'You dieded...'
		exit(1)

	def Troll(self):
		print 'The troll has slain you!'
		exit(1)

	def Orc(self):
		print 'The orc clubs you to death!'
		exit(1)
	
	def Knight(self):
		print 'The knight cuts you down where you stand!'
		exit(1)
	
	def Gargoyle(self):
		print 'The gargoyle swings his tail and snaps you in half!'
		exit(1)
	
class Intro(object):

	def enter(self):
		while True:
			clsw.RefreshWindow()
			game = raw_input('Start game? (Y/N)> ')
			if game == 'y' or game == 'Y':
				return 'Dungeon5'
			if game == 'n' or game == 'N':
				wSize.default()
				clsw.RefreshWindow()
				exit(1)

	def __init__(self):
		print 'Welcome to blister!\n'
		print 'To navigate type what you want to do.'
		print 'Have fun!'
		raw_input('<Enter>')


class Town(object):

    def description(self):
        print 'You are in the town.'
        print 'To your left is the store.'
        print 'To your right is your house.'
        print 'In front of you is the entrance to the dungeon.'

    def enter(self):
        self.description()
        while True:
            x = Choice()
            if x.pChoice in lists.houseList:
                return 'PlayerHouse'
            elif x.pChoice in lists.storeList:
                return 'Store'
            elif x.pChoice in lists.dungeonList:
                return 'Dungeon1'
            else:
				print 'I dont know what that means...'
				windowAction()
				self.description()

class Store(object):

    def description(self):
        print 'The shopkeeper greets you:'
        print '"Hello! have you come to <buy> or <sell>?"'

    def enter(self):
        self.description()

        def buy():

            def goods():
                print 'Here are my goods...'
                for k, v in playerStore.inv.iteritems():
                    print k, '\t', v

            goods()
            while True:
                x = Choice()
                if x.pChoice in lists.buyChoice and x.pChoice in playerStore.inv:
                    if playerCharacter.gold >= playerStore.inv[x.pChoice]:
                        clsw.RefreshWindow()
                        playerCharacter.gold = playerCharacter.gold - playerStore.inv[x.pChoice]
                        playerStore.inv.pop(x.pChoice)
                        playerCharacter.inv.append(x.pChoice)
                        goods()
                    elif playerCharacter.gold < playerStore.inv[x.pChoice]:
                        print '"You don\'t have enough gold for that friend."'
                        windowAction()
                        buy()
                else:
                    if x.pChoice in lists.back:
                        clsw.RefreshWindow()
                        return False
                    print '"I didn\'t quite catch that..."'
                    windowAction()
                    goods()

        def sell():
            playerCharacter.inventoryList()
            while True:
                x = Choice()
                if x.pChoice in playerCharacter.inv:
                    playerCharacter.gold = playerCharacter.gold + gameItems.ItemVal[x.pChoice]
                    playerCharacter.inv.pop(playerCharacter.inv.index(x.pChoice))
                    playerStore.inv[x.pChoice] = gameItems.ItemVal[x.pChoice]
                    print '"You get %d for that."' % gameItems.ItemVal[x.pChoice]
                    windowAction()
                    playerCharacter.inventoryList()
                else:
                    if x.pChoice in lists.back:
                        clsw.RefreshWindow()
                        return False
                    print '"I didn\'t quite catch that..."'
                    windowAction()

        while True:
            x = Choice()
            if x.pChoice in lists.townList:
                return 'Town'
            if x.pChoice == 'buy' or x.pChoice == 'Buy':
                clsw.RefreshWindow()
                buy()
                return 'Store'
            if x.pChoice == 'sell' or x.pChoice == 'Sell':
                clsw.RefreshWindow()
                sell()
                return 'Store'
            print "I don't know what that means..."
            windowAction()
            self.description()

class PlayerHouse(object):

    def description(self):
        print 'You enter the house. There is a chest to your left and a bed to your right.'

    def enter(self):
        self.description()

        def Chest():
            while True:
                playerCharacter.chestList()
                x = Choice()
                if x.pChoice in playerCharacter.inv:
                    del playerCharacter.inv[playerCharacter.inv.index(x.pChoice)]
                    playerCharacter.chest.append(x.pChoice)
                    clsw.RefreshWindow()
                    playerCharacter.chestList
                elif x.pChoice in playerCharacter.chest:
                    del playerCharacter.chest[playerCharacter.chest.index(x.pChoice)]
                    playerCharacter.inv.append(x.pChoice)
                    clsw.RefreshWindow()
                    playerCharacter.chestList
                else:
                    if x.pChoice in lists.back:
                        clsw.RefreshWindow()
                        return False
                    print '...'
                    windowAction()

        def Bed():
            print 'You lay on the bed, thinking about adventures you had and the about the ones awaiting you. You enter dreamland...'
            time.sleep(5)
            print 'You wake up. The sunlight graces your face through a small window as you open your eyes.'
            time.sleep(5)
            clsw.RefreshWindow()

        while True:
            x = Choice()
            if x.pChoice in lists.townList:
                return 'Town'
            if x.pChoice in lists.house[0]:
                clsw.RefreshWindow()
                Chest()
                return 'PlayerHouse'
            if x.pChoice in lists.house[1]:
                clsw.RefreshWindow()
                Bed()
                return 'PlayerHouse'
            print "I don't know what that means..."
            windowAction()
            self.description()

class Dungeon1(object):

	def description(self):
		print 'You descend the staircase to the dungeon.'

	def enter(self):
		self.description()

		def dungeonProgress():
			lists.gnollState[0] = False
			print 'You walk over the gnoll corpse and continue on your way towards a hole in the ground.'
			print 'You look over and see a staircase leading down. Do you turn back or descend once more?'
			x = Choice()
			if x.pChoice in lists.dungeonList:
				return 'Dungeon2'
			elif x.pChoice in lists.back:
				return 'Town'
			else:
				print "I don't know what that means"
				windowAction()
				return dungeonProgress()

		def gnollFight(state):
			print 'What is your next move?'
			y = Choice()
			clsw.RefreshWindow()
			if y.pChoice in lists.battle[1]:
				print 'You swing your sword and slay the gnoll in one motion!'
				return dungeonProgress()
			if y.pChoice in lists.battle[2]:
				print 'You kick the gnoll with yor leg. The gnoll is knocked unconscious. He will be out for awhile...'
				return dungeonProgress()
			if y.pChoice in lists.battle[3]:
				if state == 3:
					print "You punch the gnoll face into a pulp. He's a goner."
					return dungeonProgress()
			else:
				return Dead().Gnoll()

		def firstEnter():
			x = Choice()
			clsw.RefreshWindow()
			if x.pChoice == 'light torch' and playerCharacter.inv.__contains__('Torch'):
				print 'The light illuminates everything around you.'
				print 'You notice a pair of eyes glowing in the shadow, looking at you.'
				print "Its a gnoll! Prepare yourself for battle!"
			else:
				if x.pChoice == 'light torch' and not playerCharacter.inv.__contains__('Torch'):
					print "You don't have a torch!"
					windowAction()
					return 'Dungeon1'
			if x.pChoice == 'forward':
				print 'You carefully walk forward.'
				print 'A gnoll appears out of nowhere!'
				print "It swings at you. It's pickaxe punctures your foot as you try to dash back!"
				footDamaged = True
				lists.damagePC.append(footDamaged)
			else:
				if x.pChoice in lists.back:
					return 'Town'
				print "I don't know what that means"
				windowAction()
				return 'Dungeon1'
			y = Choice()
			clsw.RefreshWindow()
			if y.pChoice in lists.battle[0]:
				print 'How do you attack the gnoll?'
				y = Choice()
				clsw.RefreshWindow()
				if y.pChoice in lists.battle[1]:
					print 'You swing your sword and slay the gnoll in one motion!'
					return dungeonProgress()
				if y.pChoice in lists.battle[2]:
					print 'You kick the gnoll with yor leg. The gnoll is knocked unconscious. He is out for good...'
					return dungeonProgress()
				if y.pChoice in lists.battle[3]:
					gnollState = 0
					for i in range(1, 4):
						gnollState += 1
						print 'You punch the gnoll right into its face. The gnoll is dazzed.'
						if gnollState > 0 and gnollState < 3:
							gnollFight(gnollState)
						elif gnollState == 3:
							return gnollFight(gnollState)

				else:
					Dead().Gnoll()
			else:
				Dead().Gnoll()

		if lists.gnollState[0] == True:
			print 'It is dark in here.'
			return firstEnter()
		else:
			return dungeonProgress()

class Dungeon2(object):

	def description(self):
		print 'You descend a staircase once more.'

	def enter(self):
		
		self.description()

		def dungeonProgress():
			clsw.RefreshWindow()
			while True:
				if 'Troll key' not in playerCharacter.inv: 
					print 'The troll lays dead. There appears to be a key hanging on his belt...'
				else:
					print 'The troll lays dead.'
				print 'A few meters ahead is a pit. It is the only place you can go. There are walls all around.'
				print 'You decide to...'
				x = Choice()
				clsw.RefreshWindow()
				if x.pChoice in lists.dungeon2[2]:
					return 'Dungeon3'
				elif x.pChoice in lists.dungeon2[3]:
					playerCharacter.inv.append('Troll key')
				elif x.pChoice in lists.back:
					return startPosition()
				else:
					print "I don't know what that means..."
					windowAction()			
		
		def goldRoom():
			clsw.RefreshWindow()
			while True:
				print 'The room has a wooden table placed in the middle of the room.'
				if lists.goldRoomState[1] == True:
					print 'On the table lays a brown sack.'
				x = Choice()
				clsw.RefreshWindow()
				if x.pChoice in lists.goldRoom and lists.goldRoomState[1] == True: # 2nd list item is true for unlooted sack
					print 'You decide to take the sack and open it. There are some coins in it. You find 320 gold!'
					time.sleep(4)
					clsw.RefreshWindow()
					playerCharacter.gold = playerCharacter.gold + 320
					lists.goldRoomState[1] = False
				elif x.pChoice in lists.back:
					return leftAlt()
				else:
					print "I don't know what that means..."
					windowAction()
		
		def trollBattle3(var):
			x = Choice()
			clsw.RefreshWindow()
			if var == 1:
				if x.pChoice in lists.battle[1]:
					if 1 in lists.battleLog:
						print 'You swing at the troll in rage. You miss, the troll grabs you by your gullet and snaps your neck!'
						Dead().Troll()
					elif 2 in lists.battleLog:
						print 'You decide to finish the fight and chop him down where he stands!'
						time.sleep(4)
					elif 3 in lists.battleLog:
						print 'You finish him off with a slash. His head comes clean off!'
						time.sleep(4)
				elif x.pChoice in lists.battle[2]:
					if 1 in lists.battleLog:
						print 'While injured you manage to swipe the troll to the ground with your legs and tramp him into the ground!'
						time.sleep(4)
					elif 2 in lists.battleLog:
						print 'You hook the troll with your leg once. As he drops and tries to get up again you hit him with your foot directly to the face. He\'s gone'
						time.sleep(4)
					elif 3 in lists.battleLog:
						print 'You push the troll to the ground. You turn his face into a pulp by beating it with the pommel of your sword!'
						time.sleep(4)
				elif x.pChoice in lists.battle[3]:
					if 1 in lists.battleLog:
						print 'In a rage you drop your sword and jump the troll. You end up on top of him punching him to death!'
						time.sleep(4)
					elif 2 in lists.battleLog:
						print 'In a last ditch effort the troll tries to slash you. You counter him by pummeling him into the ground!'
						time.sleep(4)
					elif 3 in lists.battleLog:
						print 'You dash forward and beat the trolls face into a pulp with your pommel!'
						time.sleep(4)
				else:
					Dead().Troll()
			elif var == 2:
				if x.pChoice in lists.battle[1]:
					if 1 in lists.battleLog:
						print 'The troll dashes forward. You swiftly put the tip of the sword infront. You stab him through the chest!'
						time.sleep(4)
					elif 2 in lists.battleLog:
						print 'Although injured you manage to gain the upper hand and slay the troll with your sword!'
						time.sleep(4)
					elif 3 in lists.battleLog:
						print 'You pull out your sword and finish the troll off!'
						time.sleep(4)
				elif x.pChoice in lists.battle[2]:
					if 1 in lists.battleLog:
						print 'He jumps forward but you best him with a left leg hook!'
						time.sleep(4)
					elif 2 in lists.battleLog:
						print 'You attempt to kick jump yourself back up. As you do that the troll punches a hole in your chest with its sharp claws.'
						Dead().Troll()
					elif 3 in lists.battleLog:
						print 'You finish him off with a leg jab into his face!'
						time.sleep(4)
				elif x.pChoice in lists.battle[3]:
					if 1 in lists.battleLog:
						print 'You dash into him and pummel his face into a pulp!'
						time.sleep(4)
					elif 2 in lists.battleLog:
						print 'The troll jumps on you and you get into a fist fight. You prevail beating him to death!'
						time.sleep(4)
					elif 3 in lists.battleLog:
						print 'You continue to fight barehanded punching him into oblivion!'
						time.sleep(4)
				else:
					Dead().Troll()
			elif var == 3:
				if x.pChoice in lists.battle[1]:
					if 1 in lists.battleLog:
						print 'He turns back around to the sight of your shining blade. You cut him clean in half!'
						time.sleep(4)
					elif 2 in lists.battleLog:
						print 'You finish him off by decapitating him!'
						time.sleep(4)
					elif 3 in lists.battleLog:
						print 'You pull out your sword and in a blind rage chop him into bits!'
				elif x.pChoice in lists.battle[2]:
					if 1 in lists.battleLog:
						print 'He turns around to the sight of your leg flying into his face! He dies instantly!'
						time.sleep(4)
					elif 2 in lists.battleLog:
						print 'You hook him with your leg into his face as he drops down. He is done!'
						time.sleep(4)
					elif 3 in lists.battleLog:
						print 'Although injured you manage to roundhouse kick the troll in the face. The force opens his skull! He is a goner!'
						time.sleep(4)
				elif x.pChoice in lists.battle[3]:
					if 1 in lists.battleLog:
						print 'You continue to use the pommel of the sword to turn his face into a pulp!'
						time.sleep(4)
					elif 2 in lists.battleLog:
						print 'You enter survival mode and release all your anger on his body. He succumbs to the injuries!'
						time.sleep(4)
					elif 3 in lists.battleLog:
						print 'You start swinging mindlessly at him. He dodges all your shots and with a simple straight jab punctures your throat!'
						Dead().Troll()
				else:
					Dead().Troll()
			else:
				Dead().Troll()

		
		def trollBattle2(var):
			if var == 1:
				x = Choice()
				clsw.RefreshWindow()
				if x.pChoice in lists.battle[1]:
					print 'The troll dodges your next attack and pierces a hole in your off hand.'
					handDamaged = True
					lists.damagePC.append(handDamaged)
					trollBattle3(1)
				elif x.pChoice in lists.battle[2]:
					print 'The troll did not anticipate your direct kick!'
					print 'He gets boosted 4 feet backwards by the sheer force of your kick.'
					trollBattle3(2)
				elif x.pChoice in lists.battle[3]:
					print 'The troll grabs your hand mid punch.'
					print 'You use the pommel of your sword on his face.'
					print 'Teeth combined with blood fly out of his mouth.'
					trollBattle3(3)
				else:
					Dead().Troll()
			elif var == 2:
				x = Choice()
				clsw.RefreshWindow()
				if x.pChoice in lists.battle[1]:
					print 'The troll is slowed by the injury.'
					print 'You draw your sword and manage slash open his leg.'
					print "The troll is now heavily damaged but the fight isn't over."
					trollBattle3(1)
				elif x.pChoice in lists.battle[2]:
					print 'The troll dodges your second kick.'
					print 'Using his momentum he swipes his leg on your weight bearing leg.'
					print 'You hit the ground. The troll slashes your leg in the process.'
					legDamaged = True
					lists.damagePC.append(legDamaged)
					trollBattle3(2)
				elif x.pChoice in lists.battle[3]:
					print 'You take on the troll in a fist fight.'
					print 'As he misses you manage to hit him in the same rib area again.'
					print 'The troll can barely breed.'
					trollBattle3(3)
				else:
					Dead().Troll()
			elif var == 3:
				x = Choice()
				clsw.RefreshWindow()
				if x.pChoice in lists.battle[1]:
					print 'You swiftly draw your sword.'
					print 'As he attacks again you puncture his arm and slash his leg.'
					print 'The troll can barely stand.'
					trollBattle3(1)
				elif x.pChoice in lists.battle[2]:
					print 'You hook your leg into his ribcage, breaking his ribs as he attempts to jump on you.'
					trollBattle3(2)
				elif x.pChoice in lists.battle[3]:
					print 'You swing again at him and miss.'
					print 'The troll slashes your body with his sharp claws.'
					bodyDamaged = True
					lists.damagePC.append(bodyDamaged)
					trollBattle3(3)
				else:
					Dead().Troll()
			else:
				Dead().Troll()

		
		def trollBattle():
			clsw.RefreshWindow()
			print "It's a troll! He turns around with his red eyes looking directly at you."
			print 'He starts moving towards you with ill intent!'
			x = Choice()
			clsw.RefreshWindow()
			if x.pChoice in lists.battle[0]:
				print 'How do you attack the troll?'
				y = Choice()
				clsw.RefreshWindow()
				if y.pChoice in lists.battle[1]:
					print 'You swing your sword. The troll dashes back. You slash its arm.'
					print 'The troll is enraged he jumps back at you.'
					lists.battleLog.append(1)
					trollBattle2(1)
				elif y.pChoice in lists.battle[2]:
					print 'You do a roundhouse kick right into the trolls ribs.'
					print 'You can feel rib bone cracking upon hitting him.'
					print 'The troll drops to the ground. It slowly gets back up'
					lists.battleLog.append(2)
					trollBattle2(2)
				elif y.pChoice in lists.battle[3]:
					print 'You skillfully hit the troll with a mighy blow to the abdomen.'
					print "He doesn't go down."
					lists.battleLog.append(3)
					trollBattle2(3)
				else:
					Dead().Troll()
			else:
				Dead().Troll()

		def left():
			while True:
				print 'There appears to be a locked door in front of you.'
				x = Choice()
				clsw.RefreshWindow()
				if (x.pChoice in lists.dungeon2[0]) and ('Troll key' in playerCharacter.inv):
					print 'You place the key into the lock, turn it and hear a clicking sound.'
					time.sleep(2.5)
					print 'You opened the door.'
					lists.goldRoomState[0] = False
					return goldRoom()
				elif (x.pChoice in lists.dungeon2[0]) and ('Troll key' not in playerCharacter.inv):
					print "You don't have the key..."
					windowAction()	
				elif x.pChoice in lists.back:
					return leftAlt()
				else:
					print "I don't know what that means..."
					windowAction()
					return 'Dungeon2'

		def leftAlt():
			while True:
				print 'There is an open door.'
				x = Choice()
				clsw.RefreshWindow()
				if (x.pChoice in lists.enter) and (lists.goldRoomState[1] == True):
					return goldRoom()
				elif x.pChoice in lists.back:
					return 'Dungeon2'
				else:
					print "I don't know what that means..."
					windowAction()

		def right():
			if lists.trollState[0] == True:
				print 'Upon taking a few steps you hear a growling sound.'
				x = Choice()
				clsw.RefreshWindow()
				if x.pChoice in lists.dungeon2[1]:
					print 'You continue onward.'
					print 'You see a hairy, slim creature crouched with its back turned.'
					print 'It appears to be munching on some half bloodied bone.'
					#time.sleep(5)
					trollBattle()
					lists.trollState[0] = False
					while True:
						return dungeonProgress()
				elif x.pChoice in lists.back:
					return 'Dungeon2'
				else:
					print "I don't know what that means..."
					windowAction()
			else:
				while True:
					print 'You walk down a corridor'
					x = Choice()
					clsw.RefreshWindow()
					if x.pChoice in lists.dungeon2[1]:
						return dungeonProgress()
					elif x.pChoice in lists.back:
						return 'Dungeon2'
					else:
						print "I don't know what that means..."
						windowAction()
		
		def startPosition():
			while True:
				print 'There are paths to the left and right. You go...'
				x = Choice()
				clsw.RefreshWindow()
				if x.pChoice == 'left' and lists.goldRoomState[0] == True: # item list is true for locked door
					return left()
				elif x.pChoice == 'left' and lists.goldRoomState[0] == False:
					return leftAlt()
				elif x.pChoice == 'right':
					return right()
				elif x.pChoice in lists.back:
					return 'Dungeon1'
				else:	
					print "I don't know what that means..."
					windowAction()

		if (lists.positionSwitch == True) and (lists.trollState[0] == False):
			lists.positionSwitch = False
			return dungeonProgress()
		elif lists.trollState[0] == False:
			return dungeonProgress()
		else:
			return startPosition()

class Dungeon3(object):

	def description(self):
		if lists.positionSwitch == True:
			print 'You jump down the pit.'
		
		print 'There seems to be 4 corridors leading in every direction. North, south, east and west.'
		print 'You go...'
		
	def enter(self):
	
		self.description()
		
		def orcIsAlive():
			if lists.orcState[0] == True:
				return randint(0, 1)
			else:
				return 1
		
		def dungeonProgress():
			while True:
				if 'Rope' not in playerCharacter.inv:
					print 'The orc corpse lays on the floor. There is a rope hanging around his chest.'
				else:
					print 'The orc corpse lays on the floor.' 
				print 'You look around and see a medieval portal at the end of the corridor.'
				print 'You decide to...'
				x = Choice()
				clsw.RefreshWindow()
				if x.pChoice in lists.enter:
					return 'Dungeon4'
				elif x.pChoice in lists.orcLoot:
					playerCharacter.inv.append('Rope')
				elif x.pChoice in lists.back:
					self.description()
					return corrDecision()
				else:
					print "I don't know what that means..."
					windowAction()
		
		def corrDecision():
			while True:
				lists.positionSwitch = True
				x = Choice()
				clsw.RefreshWindow()
				if x.pChoice in lists.dungeon3path[0]:
					if (lists.orcState[0] == False) and (lists.chosenPath == lists.dungeon3path[0]):
						return dungeonProgress()
					else:
						return corridor1().front()
				elif x.pChoice in lists.dungeon3path[1]:
					if (lists.orcState[0] == False) and (lists.chosenPath == lists.dungeon3path[1]):
						return dungeonProgress()
					else:
						return corridor2().front()
				elif x.pChoice in lists.dungeon3path[2]:
					if (lists.orcState[0] == False) and (lists.chosenPath == lists.dungeon3path[2]):
						return dungeonProgress()
					else:
						return corridor3().front()
				elif x.pChoice in lists.dungeon3path[3]:
					if (lists.orcState[0] == False) and (lists.chosenPath == lists.dungeon3path[3]):
						return dungeonProgress()
					else:
						return corridor4().front()
				elif (x.pChoice in lists.back) and ('Rope' not in playerCharacter.inv):
					print 'You need a rope to climb out of the pit.'
					windowAction()
					self.description()
				elif (x.pChoice in lists.back) and ('Rope' in playerCharacter.inv):
					return 'Dungeon2'
				else:
					print "I don't know what that means..."
					windowAction()
					self.description()
		
		def orcFightLong(weapon):
			playerCharacterHP = 7
			orcHP = 8
			for i in lists.damagePC:
				playerCharacterHP -= 1
			
			if randint(0, 1) == 1:
				print 'You attack the orc with your %s' % weapon
				print 'You deal 1 damage.'
				print 'The orc deals 0 damage.'
				orcHP = orcHP - 1
			else:
				print 'You attack the orc with your %s' % weapon
				print 'You deal 0 damage.'
				print 'The orc deals 1 damage.'
				playerCharacterHP = playerCharacterHP - 1
				
			for turn in range(playerCharacterHP):
				z = randint(0, 2)
				y = randint(0, 3)
				print 'How do you attack the orc?'
				x = Choice()
				clsw.RefreshWindow()
				if ((x.pChoice in lists.battle[1]) or (x.pChoice in lists.battle[2]) or (x.pChoice in lists.battle[3])) and (x.pChoice not in lists.battle[0]):
					print 'You attack the orc with your %s.' % x.pChoice
					print 'You deal %d damage.' % y
					print 'The orc deals %d damage.' % z
					playerCharacterHP = playerCharacterHP - z
					orcHP = orcHP - y
					if (playerCharacterHP == 0) or (playerCharacterHP < 0):
						clsw.RefreshWindow()
						print 'Your HP reached zero.'
						time.sleep(2)
						clsw.RefreshWindow()
						Dead().Orc()
					elif (orcHP == 0) or (orcHP < 0):
						clsw.RefreshWindow()
						print 'You slay the orc!'
						lists.orcState[0] = False
						time.sleep(2)
						clsw.RefreshWindow()
						return dungeonProgress()
				elif x.pChoice not in lists.battle:
					print 'You miss your chance to do something meaningful.'
					print 'You deal 0 damage'
					print 'The orc deals 1 damage.'
					playerCharacterHP = playerCharacterHP - 1
					
					if (playerCharacterHP == 0) or (playerCharacterHP < 0):
						print 'Your HP reached zero.'
						time.sleep(2)
						Dead().Orc()
					
		def orcFight():
			print 'The orc moves towards you with a running start. You decide to...'
			x = Choice()
			clsw.RefreshWindow()
			if x.pChoice in lists.battle[0]:
				print 'How do you attack the orc?'
				x = Choice()
				clsw.RefreshWindow()
				if (x.pChoice in lists.battle[1]) and ('Barbed sword' in playerCharacter.inv):
					print 'You decide to unnseathe your barbed sword knowing that it will do the most damage.'
					print 'You slide in between the legs of the orc and swipe your sword. his leg comes off.'
					print 'You finish him off by slicing him into bits!'
					lists.orcState[0] = False
					time.sleep(3)
					clsw.RefreshWindow()
					return dungeonProgress()
				elif ((x.pChoice in lists.battle[1]) or (x.pChoice in lists.battle[2]) or (x.pChoice in lists.battle[3])) and ('Barbed sword' not in playerCharacter.inv):
					return orcFightLong(x.pChoice)
			else:
				Dead().Orc()
		
		def randomEncounter():			
				print 'You can hear heavy footsteps becoming louder with each step. Something is around the corner.'
				print 'As a shadowy figure emerges at the opposite end of the corridor'
				print 'you become aware of if its huge size.'
				print 'It has dark green skin, teeth sharp as claws, eyes dark as night.'
				print 'It\'s barely dressed, only wearing animal skin to cover its private parts.'
				print 'It\'s an orc! He has a wooden spiked club!'
				return orcFight()
			
		class corridor1(object): # North
			
			def front(self):
				print 'You entered the North corridor.'
				print 'The light barely shines from the cracks above and you can hardly see...'
				#time.sleep(3)
				clsw.RefreshWindow()
				y = orcIsAlive()
				if y == 0:
					lists.chosenPath = lists.dungeon3path[0]
					return randomEncounter()
				elif y == 1:
					while True:
						print 'You arive at the end of the North corridor.'
						print 'There is a junction. Two paths. One to the left and one to the right. You go...'
						x = Choice()
						if x.pChoice in lists.dungeon3[0]: # left - goes west
							return corridor4().end()
						elif x.pChoice in lists.dungeon3[1]: # right - goes east
							return corridor3().end()
						else:
							print "I don't know what that means..."
							windowAction()
						
			def end(self):
				clsw.RefreshWindow()
				print 'You entered the North corridor from the endside.'
				print 'You can see the light from the place where you started.'
				y = orcIsAlive()
				if y == 0:
					lists.chosenPath = lists.dungeon3path[0]
					return randomEncounter()
				elif (y == 1) and (lists.chosenPath == lists.dungeon3path[0]):
					dungeonProgress()
				elif y == 1:
					while True:
						print 'You are at the bottom of the pit.'
						print 'There are 4 corridors leading in every direction. North, south, east and west. You go...'
						return corrDecision()

		class corridor2(object): # South
			
			def front(self):
				print 'You entered the South corridor.'
				print 'The light barely shines from the cracks above and you can hardly see...'
				#time.sleep(3)
				clsw.RefreshWindow()
				y = orcIsAlive()
				if y == 0:
					lists.chosenPath = lists.dungeon3path[1]
					return randomEncounter()
				elif y == 1:
					while True:
						print 'You arive at the end of the South corridor.'
						print 'There is a junction. Two paths. One to the left and one to the right. You go...'
						x = Choice()
						if x.pChoice in lists.dungeon3[0]: # left - goes east
							corridor3().end()
						elif x.pChoice in lists.dungeon3[1]: # right - goes west
							corridor4().end()
						else:
							print "I don't know what that means..."
							windowAction()
						
			def end(self):
				clsw.RefreshWindow()
				print 'You entered the South corridor from the endside.'
				print 'You can see the light from the place where you started.'
				y = orcIsAlive()
				if y == 0:
					lists.chosenPath = lists.dungeon3path[1]
					return randomEncounter()
				elif (y == 1) and (lists.chosenPath == lists.dungeon3path[0]):
					dungeonProgress()
				elif y == 1:
					while True:
						print 'You are at the bottom of the pit.'
						print 'There are 4 corridors leading in every direction. North, south, east and west. You go...'
						return corrDecision()
				
		class corridor3(object): # East
			
			def front(self):
				print 'You entered the East corridor.'
				print 'The light barely shines from the cracks above and you can hardly see...'
				#time.sleep(3)
				clsw.RefreshWindow()
				y = orcIsAlive()
				if y == 0:
					lists.chosenPath = lists.dungeon3path[2]
					return randomEncounter()
				elif y == 1:
					while True:
						print 'You arive at the end of the East corridor.'
						print 'There is a junction. Two paths. One to the left and one to the right. You go...'
						x = Choice()
						if x.pChoice in lists.dungeon3[0]: # left - goes north
							corridor1().end()
						elif x.pChoice in lists.dungeon3[1]: # right - goes south
							corridor2().end()
						else:
							print "I don't know what that means..."
							windowAction()
						
			def end(self):
				clsw.RefreshWindow()
				print 'You entered the East corridor from the endside.'
				print 'You can see the light from the place where you started.'
				y = orcIsAlive()
				if y == 0:
					lists.chosenPath = lists.dungeon3path[2]
					return randomEncounter()
				elif (y == 1) and (lists.chosenPath == lists.dungeon3path[0]):
					dungeonProgress()
				elif y == 1:
					while True:
						print 'You are at the bottom of the pit.'
						print 'There are 4 corridors leading in every direction. North, south, east and west. You go...'
						return corrDecision()
						
		class corridor4(object): # West
		
			def front(self):
				print 'You entered the West corridor.'
				print 'The light barely shines from the cracks above and you can hardly see...'
				#time.sleep(3)
				clsw.RefreshWindow()
				y = orcIsAlive()
				if y == 0:
					lists.chosenPath = lists.dungeon3path[3]
					return randomEncounter()
				elif y == 1:
					while True:
						print 'You arive at the end of the West corridor.'
						print 'There is a junction. Two paths. One to the left and one to the right. You go...'
						x = Choice()
						if x.pChoice in lists.dungeon3[0]: # left - goes south
							corridor2().end()
						elif x.pChoice in lists.dungeon3[1]: # right - goes north
							corridor1().end()
						else:
							print "I don't know what that means..."
							windowAction()
						
			def end(self):
				clsw.RefreshWindow()
				print 'You entered the West corridor from the endside.'
				print 'You can see the light from the place where you started.'
				y = orcIsAlive()
				if y == 0:
					lists.chosenPath = lists.dungeon3path[3]
					return randomEncounter()
				elif (y == 1) and (lists.chosenPath == lists.dungeon3path[0]):
					dungeonProgress()
				elif y == 1:
					while True:
						print 'You are at the bottom of the pit.'
						print 'There are 4 corridors leading in every direction. North, south, east and west. You go...'
						return corrDecision()
					
		return corrDecision()

class Dungeon4(object):

	def description(self):
		print 'You are so deep the air is cold, heavy and stale.'
		
	def enter(self):
		
		def dungeonProgress():
			while True:
				print 'You decide to...'
				x = Choice()
				clsw.RefreshWindow()
				if x.pChoice in lists.enter:
					return 'Dungeon5'
				elif x.pChoice in lists.back:
					return clearedRoom()
				else:
					print 'I don\'t know what that means...'
					windowAction()
			
		def clearedRoom():
			while True:
				print 'You walk over the dead knight corpse.'
				print 'There is an altar at the end of the room.'
				if lists.plate == False:
					print 'You can see a gold chalice on the altar.'
				elif lists.plate == True:
					print 'You can see a staircase descending into darkness.'
				print 'You decide to...'
				x = Choice()
				clsw.RefreshWindow()
				if (lists.plate == False) and (x.pChoice in lists.enter) or (x.pChoice in lists.dungeon4[2]):
					print 'As you move forward you accidentally activate a pressure plate.'
					print 'The chalice slowly dissapears into the altar.'
					print 'This activates a hidden door in the ground in front which reveals a staircase leading down.'
					lists.plate = True
					return dungeonProgress()
				elif (lists.plate == True) and (x.pChoice in lists.enter):
					print 'You stand on the edge of the staircase.'
					print 'Do you go down?'
					y = Choice()
					if (y.pChoice == 'yes') or (y.pChoice == 'Yes'):
						return 'Dungeon5'
					elif y.pChoice in lists.back:
						return 'Dungeon4'
					else:
						print 'I don\'t know what that means...'
						windowAction()
				elif x.pChoice in lists.back:
					return 'Dungeon3'
				else:
					print 'I don\'t know what that means...'
					windowAction()
		
		def knightRoom():
			while True:
				print 'You enter a medieval looking room resembling a small church with a long nave and a transept.'
				print 'Across the room kneels a knight in armor which is covered by black patina.' 
				print 'He has his back turned and holds a long blade in front.'
				print 'He doesn\'t seem to notice you. You decide to...'
				x = Choice()
				if (x.pChoice in lists.dungeon4[1]) or (x.pChoice in lists.battle[0]):
					return fightScene()
				elif x.pChoice in lists.back:
					return 'Dungeon3'
				else:
					print "I don't know what that means"
					windowAction()
		
		def fightScene():
			clsw.RefreshWindow()
			i = None
			for i in range(4):
				print 'You start approaching the knight. He starts talking in a heavy german'
				print 'accent. You don\'t understand him but it sounds intimidating.'
				print '"Spure den zorn Gottes!!"'
				print 'He takes a fighting stance. You prepare for battle...'
				print 'How do you attack the knight?'
				x = Choice()
				if x.pChoice in lists.dungeon4[0]:
					clsw.RefreshWindow()
					print 'You notice the joints are the weakpoints of the armor. You swing your sword and manage to'
					print 'hit them. The knight falls onto his knee and looks upon your face. Without mercy '
					print 'you finish him off with a jab into his throat.'
					lists.knightState[0] = False
					raw_input('>')
					clsw.RefreshWindow()
					return clearedRoom()
				elif (x.pChoice in lists.battle[1]) or (x.pChoice in lists.battle[2]) or (x.pChoice in lists.battle[3]):
					i = i + 1
					if i == 3:
						print 'You get tired from all the failed attempts.'
						Dead().Knight()
					
					print 'Your attack doesnt have any effect!'
					print 'You dodge as the knight swings!'
					time.sleep(3)
					clsw.RefreshWindow()
				else:
					clsw.RefreshWindow()
					Dead().Knight()

		self.description()
		if lists.knightState[0] == True:
			return knightRoom()
		elif lists.knightState[0] == False:
			print 'You enter the medieval looking room.'
			return clearedRoom()

class Dungeon5(object):

	def description(self):
		print 'You go down a cobblestone staircase. There is a mist covering the floor.'
		
	def enter(self):
	
		def dungeonProgress():
			while True:
				if lists.gargStoned == False:
					print 'You manage to light all four torches...'
					print 'As you light the last torch the gargoyle starts slowly turning into stone'
					print 'as he attempts to give one last swing at you.'
					lists.gargStoned = True
			
				print 'There is a stone portal with a heavy wooden door on one'
				print 'end and a cobblestone staircase on the other.'
				print 'You stand in the room and decide to...'
				x = Choice()
				if x.pChoice in lists.enter:
					return 'DungeonFinal'
				elif x.pChoice in lists.back:
					return 'Dungeon4'
				else:
					print 'I don\'t know what that means...'
					windowAction()
	
		def fightScene():
			if not playerCharacter.inv.__contains__('Torch'):
				i = 3
				while True:
					if i <= 0:
						print 'Bring a torch next time!'
						Dead().Gargoyle()
						
					elif i > 0:
						print 'How do you attack the gargoyle?'
						x = Choice()
						if (x.pChoice in lists.battle) or (x.pChoice not in lists.battle[0]):
							print 'You attempt to do damage to the gargoyle but it has no effect...'
							i = i - 1
							time.sleep(2.5)
							windowAction()
						else:
							print 'You fail to do something meaningful...'
							Dead().Gargoyle()
			else:
				print 'You decide to...'
				torchesLitten = 0
				timesStumbled = 0
				while True:
					x = Choice()
					clsw.RefreshWindow()
					
					if torchesLitten == 4:
						lists.gargState[0] = False
						lists.gargStoned = False
						return dungeonProgress()
						
					if timesStumbled == 4:
						Dead().Gargoyle()
					
					if x.pChoice == 'light torch':
						y = randint(0, 1)
						if y == 1:
							print 'You manage to light the torch!'
							torchesLitten = torchesLitten + 1
						elif y == 0:
							print 'The gargoyle manages to slap you with its tail. You stumble and fail to light the torch.'
							timesStumbled = timesStumbled + 1
					elif (x.pChoice in lists.battle) or (x.pChoice not in lists.battle[0]):
						print 'You attempt to do damage to the gargoyle, the gargoyle crouches to recover from the hit.'
						print 'You decide too...'
						x = Choice()
						clsw.RefreshWindow()
						if x.pChoice == 'light torch':
							y = randint(0, 1)
						elif (x.pChoice in lists.battle) or (x.pChoice not in lists.battle[0]):
							print 'You get greedy hoping you can finish him on the spot.'
							print 'He dodges your attack.'
							Dead().Gargoyle()
						if y == 1:
							print 'The gargoyle recovers from being stunned by the previous hit.'
							print 'You manage to light the torch!'
							torchesLitten = torchesLitten + 1
						elif y == 0:
							print 'The gargoyle recovers from being stunned by the previous hit.'
							print 'You manage to light the torch!'
							torchesLitten = torchesLitten + 1
							timesStumbled = timesStumbled - 1
					else:
						print 'You fail to do something meaningful...'
						Dead().Gargoyle()
					
		def gargRoom():
			while True:
				print 'You enter a square room. There are four lit torches, two on each wall placed equally apart.'
				print 'At the end of the room you can see two gargoyle statues. They look intimidating.'
				print 'Between them is a stone portal with a heavy wooden door.'
				print 'You decide to...'
				x = Choice()
				clsw.RefreshWindow()
				if x.pChoice in lists.enter:
					print 'You move towards the door. You can feel a breeze in the room.'
					print 'The breeze turns into a wind extinguishing the torches.'
					print 'The gargoyle starts moving...'
					raw_input('>')
					clsw.RefreshWindow()
					print 'It starts flaping its wings. It looks at you and shrieks in a ear deafening manner.'
					print 'You prepare for a fight...'
					raw_input('>')
					clsw.RefreshWindow()
					return fightScene()
				elif x.pChoice in lists.back:
					return 'Dungeon4'
				else:
					print 'I don\'t know what that means...'
					windowAction()
				
		self.description()
		
		if lists.gargState[0] == True:
			return gargRoom()
		else:
			return dungeonProgress()
		
class DungeonFinal(object):

	def description():
		print 'You crawl through the small opening. The area emits an unpleasant vibe.'
		
	def enter(self):
		
		def dungeonProgress():
			pass
		
		def bossFight():
			print 'You have angered Cthullu. The only way you can defeat him is by cutting off his feelers on his chin (6).'
			print 'He steps from the altar and starts fighting you.'
			
		
		def introFinal():
			print 'As you get your wits you realize you\'ve entered a circular chamber.'
			print 'The chamber has a stone altar in the middle.'
			print 'Upon the altar sits a green-skinned, bald being. It has tentacles instead of a chin.'
			print '"I am Cthullu", he speaks, "one of The Great Old Ones..."'
			print '"Who dares disturb my rumination!!"'
			raw_input('>')
			clsw.RefreshWindow()
			print '"A mere mortal in my chambers! This is outrageous!"'
			print '"I shall smite thee for this insolence!"'
			raw_input('>')
			clsw.RefreshWindow()
			return bossFight()
		
		self.description()
		return introFinal()