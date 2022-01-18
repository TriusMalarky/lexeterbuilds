from lib.action import act
from lib.core import *
import random

from lib.core import core


class shade(core):
    def __init__(self,name,world):
        self.name=name
        world.characterlist.append(self.name)
        self.internalID='character-shade-'+self.name
        self.world=world
        self.debug=self.world.debug
        self.rDebug()
        self.room='darkroom'
        self.hp=15
        self.act = act(self.name,self.world)
        self.age=0
        self.tickCount=random.randrange(1,5)
        self.prefer=prefer()

        if self.name=='mek':
            self.prefer.fruit='orange'
            self.week = 5
        elif self.name=='geoflib':
            self.prefer.fruit='pineapple'
            self.week = 4
    def tick(self,world):
        self.age+=1;self.tickCount+=1
        if self.tickCount==self.week: self.tickCount=1
        if self.tickCount==1:
            lines=[
                'heya, stranger!','im a shade, not a ghost. theres a difference.',
                'waddup, '+world.player.name+'?','evening!',
                'i cannae find ma lunch!', 'i like '+self.prefer.fruit+'s. my brother doesnt.',
                'ah, the darkness. so refreshing.','blegh! just got a bug in my mouth!',
                'have ya talked to my twin?','tha rats here, they make quite the racket!',
                'not a big fan of moths. how bout you?','ever been to paris?']
            self.act.speak(random.choice(lines),self.room)
        elif self.tickCount==2:
            pass # ask
        elif self.tickCount==3:
            pass #nothing/atk
        elif self.tickCount==4:
            pass #possiblemove
        
        
class darkroom(core):
    def __init__(self,world):
        self.world=world
        self.internalID='room-darkroom'
        self.debug=self.world.debug
        self.rDebug()
        world.characters.geoflib=shade('geoflib',world)
        world.characters.mek=shade('mek',world)
        self.descriptions = [
            "It's incredibly dark.",
            "There's not much here.",
            "Where'd everything go?"
        ]
