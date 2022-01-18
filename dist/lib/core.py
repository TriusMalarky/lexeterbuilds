import pickle
import os
import inspect

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

class core(): # <-- core class, all other classes should inherit this
    def __init__(self):
        self.internalID='core-parent'
    def __str__(self): # <-- core function for displaying all relevant members of a given class instance
        attr = inspect.getmembers(self, lambda a:not(inspect.isroutine(a)))
        ar=[]
        for _ in [a for a in attr if not(a[0].startswith('__')) and not(a[0].startswith('internal'))]:
            ar.append(_)
        return str(ar)
    def rDebug(self):
        if self.debug:
            print("Debug: " + self.internalID)
            print(" ++ "+ str(self))

class prefer(core): # <-- dummy class
    def __init(self):
        self.internalID='character-preference'


def save(lexeter):
    lexMem=inspect.getmembers(lexeter,lambda a:not(inspect.isroutine(a))) # <-- Not sure if this is necessary, the save function only worked right after I added this though . . .
    loc=open('save\\lexeter.txt','wb')
    pickle.dump(lexeter,loc)
    # Unused function for saving each individual class instance. Ignore.
    #for lexMemEntry in [a for a in lexMem if not(a[0].startswith('__') and not (a[0].startswith('internal'))]:
        #loc=open('save\\'++'.txt','wb')
        #pickle.dump(lexMemEntry,loc)

    
def load():
    savefile=open('save\\lexeter.txt','rb') # <-- open save file in readable binary for pickle
    return pickle.load(savefile) # <-- returning loaded save state class instance

def lex_init():
    if os.path.exists('save\\lexeter.txt'):
        return load() # <-- returning the loaded save state class instance
    else:
        open('save\\lexeter.txt','w')
        from lib.player import lexeter
        lexet = lexeter()
        save(lexet) # <-- saving the save state instance
        return lexet # <-- returning the newly created save state






def tick(lexeter,world):
    for _ in world.characterlist:
        exec('world.characters.'+_.lower()+'.tick(world)')
    world.player.act.playeraction()
    save(lexeter) # save on every tick
    tick(lexeter,world)
