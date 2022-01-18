from lib.core import *


class stone(core):
    def __init__(self,debug):
        self.internalID = 'item-stone'
        self.name = 'stone'
        self.quality = 0
        self.descriptions = [
            "Well, it's a rock. What did you expect?",
            "It's a grey stone.",
            "Looks like it might be a chunk of granite.",
            "It might not be granite after all."
        ]
        self.debug = debug
        self.rDebug

class branch(core):
    def __init__(self,debug):
        self.internalID = 'item-branch'
        self.name = 'branch'
        self.quality = 0
        self.descriptions = [
            "It's just a stick, but it's cool nonetheless.",
            "Why have a sword when you can have this stick?",
            "En garde!",
            "You can face any danger with this, as long as that danger is largely imaginary.",
            "You don't have a dog, unfortunately.",
            "Where's a dog when you need one?",
            "It's a muddy twig."
        ]
        self.debug = debug
        self.rDebug

class scrapmetal(core):
    def __init__(self,debug):
        self.internalID = 'item-scrapmetal'
        self.name = 'metal scrap'
        self.quality = 0
        self.descriptions = [
            "Several pieces of metal. A hallmark of many survival games.",
            "You're pretty sure none of this is actually useable without the correct tools and training, but somehow things will work out. They always do.",
            "How do you use this?",
            "Don't cut yourself, it's sharp.",
            "Maybe if you found a way to melt it, you could . . . never mind, you're not a blacksmith.",
            "A bunch of junk from various metal things.",
            "Bottlecaps, wires, a doorknob and a steel plate glove that is conveniently dented in a way that you can't wear it.",
            "Why in the world is this here?"
        ]
        self.debug = debug
        self.rDebug

class egg(core):
    def __init__(self,debug):
        self.internalID = 'item-egg'
        self.name = 'egg'
        self.quality = 2
        self.descriptions = [
            "It's an egg.",
            "Scrambled, overeasy, sunny side up, hardboiled . . .",
            "It probably won't hatch into anything, it looks just like an average chicken egg from the supermarket.",
            "Breakfast is served! Well, once you find a frying pan.",
            "Tasty."
        ]
        self.debug = debug
        self.rDebug

class potato(core):
    def __init__(self,debug):
        self.internalID = 'item-potato'
        self.name = 'potato'
        self.quality = 2
        self.descriptions = [
            "Boil it, mash it, stick it in a stew.",
            "The Irish lived on these for a while.",
            "A Russian's favorite beverage. Well, almost.",
            "All the nutrients in one spud.",
            "Idaho grown, of course.",
            "So many possibilities in one small package."
        ]
        self.debug = debug
        self.rDebug

class shinystone(core):
    def __init__(self,debug):
        self.internalID = 'item-shinystone'
        self.name = 'shiny stone'
        self.quality = 1
        self.descriptions = [
            "It's an oddly shiny stone. Interesting, but not worth much.",
            "Sparkly.",
            "It's so close to mundane, and yet so far."
        ]
        self.debug = debug
        self.rDebug()

class diamond(core):
    def __init__(self,debug):
        self.internalID = 'item-diamond'
        self.name = 'diamond'
        self.quality = 3
        self.descriptions = [
            "You cannot afford ford . . . this overpriced rock.",
            "There's no way you can make tools out of this.",
            "Hilariously valuable, for almost no reason.",
            "It's not rare, really.",
            "Or is it cubic zirconia?",
            "Just a thumb-sized chunk of diamond.",
            "It's a lot larger than most you've seen."
        ]
        self.debug = debug
        self.rDebug()

class ruby(core):
    def __init__(self,debug):
        self.internalID = 'item-ruby'
        self.name = 'ruby'
        self.quality = 3
        self.descriptions = [
            "A blood red jewel. ",
            "This would go really good with gold on like, a necklace or something.",
            "Evil magic scepter material.",
            "It's the color of, well, rubies."
        ]
        self.debug = debug
        self.rDebug()

class sapphire(core):
    def __init__(self,debug):
        self.internalID = 'item-sapphire'
        self.name = 'sapphire'
        self.quality = 3
        self.descriptions = [
            "A deep, deep blue stone.",
            "A refreshingly blue color.",
            "Ice magic, baby!"
        ]
        self.debug = debug
        self.rDebug()

class emerald(core):
    def __init__(self,debug):
        self.internalID = 'item-emerald'
        self.name = 'emerald'
        self.quality = 3
        self.descriptions = [
            "Hmmmmmmm . . .",
            "If it were cut, it'd likely be a square.",
            "A beautiful shade of green.",
            "It's a big one.",
            "You wonder what this'd go for."
        ]
        self.debug = debug
        self.rDebug()

class opal(core):
    def __init__(self,debug):
        self.internalID = 'item-opal'
        self.name = 'opal'
        self.quality = 3
        self.descriptions = [
            "Shiny!",
            "It's a kaleidoscope, but a rock!",
            "All the colors in one stone."
        ]
        self.debug = debug
        self.rDebug()

class twine(core):
    def __init__(self,debug):
        self.internalID = 'item-twine'
        self.name = 'twine'
        self.quality = 1
        self.descriptions = [
            "A simple length of string."
        ]
        self.debug = debug
        self.rDebug()

class excalibur(core):
    def __init__(self,debug):
        self.internalID='item-excalibur'
        self.name = 'Excalibur'
        self.quality = 4
        self.descriptions = [
            "An arbitrarily powerful sword.",
            "Did this come from the stone, or the lake?",
            "It feels like you don't deserve to hold it."
        ]
        self.debug = debug
        self.rDebug()

class crudespear(core):
    def __init__(self,debug):
        self.internalID='item-crudespear'
        self.name = 'crude spear'
        self.quality = 4
        self.descriptions = [
            "An incredibly simple weapon.",
            "It's like a sharpened stick, but sharper."
        ]
        self.debug = debug
        self.rDebug()

class item(core):
    def __init__(self,world):
        self.debug = world.debug
        self.internalID = 'library-items'
        self.rDebug()
        self.qualities = {
            0 : "trash",
            1 : "common",
            2 : "useful",
            3 : "treasure",
            4 : "impossible",
            5 : "crafted"
        }
        self.trash = [
            'stone',
            'branch',
            'scrapmetal',
            'twine'
        ]
        self.common = [
            'shinystone'
        ]
        self.useful = [
            'egg',
            'potato'
        ]
        self.treasure = [
            'diamond',
            'ruby',
            'sapphire',
            'emerald',
            'opal'
        ]
        self.impossible = [
            'excalibur'
        ]
        self.crafted = [
            'crudespear'
        ]
        self.full = self.trash + self.common + self.useful + self.treasure + self.impossible
        self.stone = stone(self.debug)
        self.branch = branch(self.debug)
        self.scrapmetal = scrapmetal(self.debug)
        self.egg = egg(self.debug)
        self.shinystone = shinystone(self.debug)
        self.diamond = diamond(self.debug)
        self.excalibur = excalibur(self.debug)
        self.ruby = ruby(self.debug)
        self.sapphire = sapphire(self.debug)
        self.emerald = emerald(self.debug)
        self.opal = opal(self.debug)
        self.potato = potato(self.debug)
        self.twine = twine(self.debug)
        self.crudespear = crudespear(self.debug)

class crudespearRecipe(core):
    def __init__(self,debug):
        self.internalID = 'recipe-crudespear'
        self.debug = debug
        self.rDebug()
        self.ingredients = [
            'metalscrap',
            'branch',
            'twine'
        ]

class recipes(core):
    def __init__(self,world):
        self.world = world
        self.debug = self.world.debug
        self.internalID = 'library-crafting'
        self.rDebug()
        self.crudespearRecipe = crudespearRecipe(self.debug)

class constructs(core):
    def __init__(self,world):
        self.world = world
        self.debug = self.world.debug
        self.internalID = 'library-construction'
        self.rDebug()