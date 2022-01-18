from lib.core import *
import random

class corebiome(core):
    def __init__(self):
        self.internalID = 'biome-core'
    def genList(self,trash,common,useful,treasure,impossible):
        list = []
        for i in range(trash):
            list.append(random.choice(self.world.item.trash))
        for i in range(common):
            list.append(random.choice(self.world.item.common))
        for i in range(useful):
            list.append(random.choice(self.world.item.useful))
        for i in range(treasure):
            list.append(random.choice(self.world.item.treasure))
        for i in range(impossible):
            list.append(random.choice(self.world.item.impossible))
        return list
    def loottable(self, quality):
        if quality == 0:
            list = self.genList(99,15,7,3,1)
        elif quality == 1:
            list = self.genList(20,70,10,3,1)
        elif quality == 2:
            list = self.genList(5,10,30,3,1)
        elif quality == 3:
            list = self.genList(15,10,5,20,1)
        elif quality == 4:
            list = self.genList(1,2,3,4,5)
        loot = []
        for i in range(1,random.randint(1,5)):
            loot.append(random.choice(list))
        return loot



class pond(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-pond'
        self.descriptions=[
            'A sapphire blue pool sits in the center of the room, surrounded and filled by small flora. The air is refreshing.',
            'White cobblestones surround a deep blue pond. The room feels slightly mystical.'
        ]
        self.loot = self.loottable(2)
        self.debug = world.debug
        self.rDebug()

class marble(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-marble'
        self.descriptions = [
            'Your footsteps clack on the marbled flooring. The gold engravings on the pillars surrounding you make the room feel regal.'
        ]
        self.loot = self.loottable(2)
        self.debug = world.debug
        self.rDebug()

class terracotta(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-terracotta'
        self.descriptions = [
            'The floors and wall appear to be made of smashed, repurposed planter pots.'
        ]
        self.loot = self.loottable(2)
        self.debug = world.debug
        self.rDebug()

class brickfloor(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-brickfloor'
        self.descriptions = [
            'For some reason, whoever built this room thought red bricks for a floor and paisley wallpaper would look cool.'
        ]
        self.loot = self.loottable(0)
        self.debug = world.debug
        self.rDebug()

class fractured(corebiome):
    def __init__(self, world):
        self.world = world
        self.internalID = 'biome-fractured'
        self.descriptions = [
            'You have no idea what this room actually looks like.',
            "It appears you're inside of a kaleidoscope."
        ]
        self.loot = self.loottable(3)
        self.debug = world.debug
        self.rDebug()

class cave(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-cave'
        self.descriptions = [
            "Drip. Drip. Drip. It's a cave, all right."
        ]
        self.loot = self.loottable(1)
        self.debug = world.debug
        self.rDebug()

class canopy(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-canopy'
        self.descriptions = [
            "It's not exactly obvious how a subsection of a rainforest ended up here, but it's best not to question it."
        ]
        self.loot = self.loottable(1)
        self.debug = world.debug
        self.rDebug()

class cavern(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-cavern'
        self.descriptions = [
            "You look up and wonder where the top is. Then you look into a hole and wonder where the bottom is."
        ]
        self.loot = self.loottable(1)
        self.debug = world.debug
        self.rDebug()

class shack(corebiome):
    def __init__(self,world):
        self.world = world
        self.internalID = 'biome-shack'
        self.descriptions = [
            "There is a clearing inside a forest . . . with an old cabin in the middle."
        ]
        self.loot = self.loottable(1)
        self.debug = world.debug
        self.rDebug()