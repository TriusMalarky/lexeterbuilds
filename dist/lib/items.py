from lib.core import *


class stone(core):
    def __init__(self,debug):
        self.internalID = 'item-stone'
        self.name = 'stone'
        self.quality = 0
        self.debug = debug
        self.rDebug

class branch(core):
    def __init__(self,debug):
        self.internalID = 'item-branch'
        self.name = 'branch'
        self.quality = 0
        self.debug = debug
        self.rDebug

class scrapmetal(core):
    def __init__(self,debug):
        self.internalID = 'item-scrapmetal'
        self.name = 'metal scrap'
        self.quality = 0
        self.debug = debug
        self.rDebug

class egg(core):
    def __init__(self,debug):
        self.internalID = 'item-egg'
        self.name = 'egg'
        self.quality = 2
        self.debug = debug
        self.rDebug

class shinystone(core):
    def __init__(self,debug):
        self.internalID = 'item-shinystone'
        self.name = 'shiny stone'
        self.quality = 1
        self.debug = debug
        self.rDebug()

class diamond(core):
    def __init__(self,debug):
        self.internalID = 'item-diamond'
        self.name = 'diamond'
        self.quality = 3
        self.debug = debug
        self.rDebug()

class excalibur(core):
    def __init__(self,debug):
        self.internalID='item-excalibur'
        self.name = 'Excalibur'
        self.quality = 4
        self.debug = debug
        self.rDebug()

class item(core):
    def __init__(self,world):
        self.debug = world.debug
        self.rDebug()
        self.qualities = {
            0 : "trash",
            1 : "common",
            2 : "useful",
            3 : "treasure",
            4 : "impossible"
        }
        self.trash = [
            'stone',
            'branch',
            'scrapmetal'
        ]
        self.common = [
            'shinystone'
        ]
        self.useful = [
            'egg'
        ]
        self.treasure = [
            'diamond'
        ]
        self.impossible = [
            'excalibur'
        ]
        self.full = self.trash + self.common + self.useful + self.treasure + self.impossible
        self.stone = stone(self.debug)
        self.branch = branch(self.debug)
        self.scrapmetal = scrapmetal(self.debug)
        self.egg = egg(self.debug)
        self.shinystone = shinystone(self.debug)
        self.diamond = diamond(self.debug)
        self.excalibur = excalibur(self.debug)

