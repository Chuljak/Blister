import clsw
import maps
import wSize

wSize.size()

class Engine(object):
	
	def __init__(self, map):
		self.map = map
		
	def play(self):
		
		currentScene = self.map.opening()
		
		while True:
			clsw.RefreshWindow()
			
			nextMap = currentScene.enter()
			currentScene = self.map.next(nextMap)
		
class Map(object):

	mapName = {
		'Intro': maps.Intro(),
		'Town': maps.Town(),
		'Store': maps.Store(),
		'PlayerHouse': maps.PlayerHouse(),
		'Dungeon1': maps.Dungeon1(),
		'Dungeon2': maps.Dungeon2(),
		'Dungeon3': maps.Dungeon3(),
		'Dungeon4': maps.Dungeon4(),
		'Dungeon5': maps.Dungeon5(),
		'DungeonFinal': maps.DungeonFinal()
		}
	
	def __init__(self, start):
		self.start = start
		
	def next(self, name):
		return Map.mapName.get(name)
		
	def opening(self):
		return self.next(self.start)
		
		
startGame = Map('Intro')
fireEngine = Engine(startGame)
fireEngine.play()
