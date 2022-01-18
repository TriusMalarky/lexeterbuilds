
from lib.core import *
from lib.action import *
from lib.core import core
from lib.darkroom import *
import random
from lib.biome import *
from lib.items import *

# subclass responselog for logging player's responses
class responselog(core):
    def __init__(self):
        self.internalID='player-response-log'
    

class player(core):
    def __init__(self,age,them,world,debug):
        self.them=them;self.debug = debug;self.internalID='player-instance';self.rDebug()
        self.hp=50;self.rLog=responselog()
        self.them.act.speak("What is your name?\n")
        self.name=input("")
        self.them.act.speak(self.name+", eh?")
        self.them.act.speak("Well, have a fun adventure.");print("");print("")
        self.instance=age;self.age=age
        self.inventory = []
        self.act=playerAct(self,world)

class wmap(core):
    def __init__(self,world):
        self.debug=world.debug
        self.internalID='world-map'
        self.rDebug()
        
class world(core):
    def __init__(self,age,them,zones,debug,item,lexeter):
        self.debug=debug;self.them=them;self.zones=zones
        self.lexeter = lexeter
        self.internalID = 'reality-instance'
        self.rDebug()
        self.them.act.speak("Hmmmmm . . .")
        self.them.act.speak("There's nothing here.")
        self.them.act.speak("Give me a minute.")
        self.time = 45+(age*5)
        self.instance = age
        self.age = 0
        self.player = player(age,them,self,debug)
        self.characters = characters()
        self.characterlist = []
        self.item = item
        self.map = wmap(self)
        self.map.darkroom = darkroom(self)
        self.map.route = {}
        self.map.route['darkroom']=[]
        self.map.list = ['darkroom']
        for i in range(3):
            zone=random.choice(self.zones)
            room = str(zone+'_'+str(i))
            self.map.route['darkroom'].append(room);self.map.route[room] = ['darkroom']
            self.map.list.append(room)
            exec('self.map.'+room+'='+zone+'(self)')
        self.player.room='darkroom'

# subclass characters for saving each individual character
class characters(core):
    def __init__(self):
        self.internalID='character-list'

class them():
    def __init__(self):
        self.name="#`~<,>_r-kal"
        self.internalID='__ignore__'
        self.act = actGod(self.name)

class lexeter(core):
    def __init__(self):
        self.debug = False
        self.internalID='lexeter'
        self.rDebug()
        self.them = them()
        self.instances=1
        self.zones = ['pond','marble','terracotta','brickfloor','fractured','cave','canopy','cavern','shack']
        self.achievements = []
        self.item = item(self)
        self.world=world(self.instances,self.them,self.zones,self.debug,self.item,self)

