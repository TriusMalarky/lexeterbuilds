from lib.core import *
import random
from lib.biome import *

class act(core):
    def __init__(self, name, world):
        self.name=name
        self.world=world
        self.internalID=self.name+'-action-library'
        self.debug=self.world.debug;self.rDebug()
    def speak(self,text,room):
        if room == self.world.player.room:
            print("["+self.name+"] says: "+text)
    def ask(self,text,qID,room):
        if room == self.world.player.room:
            response=input("["+self.name+"] asks: "+text+'\n')
            exec("self.world.player.rLog."+qID+"=response")

class actGod(core):
    def __init__(self,name):
        self.name=name
        self.internalID='__ignore__'
    def speak(self,text):
        print("["+self.name+"] : "+text)

class playerAct(core):
    def __init__(self,player,world):
        self.internalID = 'player-action-library'
        self.player=player;self.world=world
        self.array = {
            'moveTo': '.m',
            'moveAlias':'move',
            'help':'.h',
            'helpAlias': 'help',
            'inspect':'.i',
            'inspectAlias':'inspect',
            'wait':'.w',
            'waitAlias':'wait',
            'scream':'scream',
            'pickup':'.p',
            'pickupAlias':'pickup',
            'pickAlias':'pick',
            'interact':'.in',
            'interactAlias':'interact'
                    }
        self.helparray = [
            'Help: Shows help screen. | .h, help',
            'Move: Move to another room. | .m, move',
            "Pickup: Pick an item up. | .p, pick, pickup",
            "Interact: Interact with an object. | .in, interact",
            'Inspect: Look at the current room and its contents. | .i, inspect',
            'Wait: Waste a moment. | .w, wait'
        ]
        self.debug=self.world.debug;self.rDebug()
    def playeraction(self):
        resp = input(": ")
        found = False
        for item in self.array:
            if resp == self.array[item]:
                found=True
                exec("self." + item + "()")
        if found == False:
            print("That's not a possible action. Try again, or use '.h' or 'help' to see the help screen.")
            self.playeraction()
    def help(self):
        clearConsole()
        for i in self.helparray:
            print(' - '+i)

    def helpAlias(self):
        self.help()
    def moveTo(self):
        clearConsole()
        self.rDebug()
        self.player.rDebug()
        self.world.rDebug()
        self.world.map.rDebug()
        print('Where would you like to go?')
        room=self.player.room
        print(room)
        if int(len(self.world.map.route[room])) < 3: # if there are less than 3 zones
            ind = len(self.world.map.route) # gets length of map
            zone = str(random.choice(self.world.zones))
            newzone = str(zone+"_"+str(ind))
            self.world.map.route[newzone]=[]
            self.world.map.route[self.player.room].append(newzone)
            self.world.map.route[newzone].append(self.player.room)
            exec("self.world.map."+newzone+"="+zone+"(self.world)")
        for i in self.world.map.route[self.player.room]:
            print(" - " + i)
        def moveToLoop(self):
            newloc = input(": ")
            if newloc in self.world.map.route[self.player.room]:
                self.player.room = newloc
                print("Moving to " + newloc)
            else:
                print("That's not an option, try again.")
                moveToLoop(self)
        moveToLoop(self)
        self.inspect()
    def inspect(self):
        clearConsole()
        roomtitle = self.world.player.room
        room = getattr(self.world.map,roomtitle)
        print(random.choice(room.descriptions))
    def moveAlias(self):
        self.moveTo()
    def inspectAlias(self):
        self.inspect()
    def wait(self):
        clearConsole()
        array = [
            'You stand about aimlessly.',
            'You wait as if you have all the time in the world.',
            'You waste a few minutes.'
        ]
        print(random.choice(array))
    def waitAlias(self):
        self.wait()
    def scream(self):
        clearConsole()
        print("Something screams with you.")
        self.world.lexeter.achievements.append('scream')
    def pickup(self):
        clearConsole()
        roomtitle = self.world.player.room
        room = getattr(self.world.map,roomtitle)
        if hasattr(room,'loot'):
            if len(room.loot) > 0:
                print("What do you want to pick up?")
                for i in room.loot:
                    print(" - "+i)
                choice = input(": ")
                def loop(choice,room):
                    if choice in room.loot:
                        room.loot.remove(choice)
                        print("You picked up "+choice)
                    else:
                        print("That's not an option, try again.")
                        loop(input(": "),room)
                loop(choice,room)
            else:
                print("There's nothing here.")
        else:
            print("There's nothing here.")
    def pickupAlias(self):
        self.pickup()
    def pickAlias(self):
        self.pickup()
    def interact(self):
        pass
    def interactAlias(self):
        self.interact()