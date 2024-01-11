
import random

class Item:
    def __init__(self, weight, worth):
        self.weight = weight
        self.worth = worth

class Potion(Item):
    def __init__(self,weight,worth):
        Item.__init__(weight, worth)

class HealthPotion(Potion):
    def __init__(self, weight, worth, regenerated_health):
        Potion.__init__(self, weight, worth)
        self.regenerated_health = regenerated_health

class Character:
    def __init__(self, hp, ad, name):
        self.hp = hp
        self.ad = ad
        self.name = name
    
    def get_hit(self, ad):
        self.hp = self.hp - ad
        if self.hp <= 0:
            self.die()
    
    def is_dead(self):
        return self.hp <= 0
    
    def die(self):
        print(self.name + "died")

class Goblin(Character):
    def __init__(self):
        Character.__init__(self, 100, 10, "Goblin")

class Ork(Character):
    def __init__(self):
        Character.__init__(self,100,10, "Ork")

class Player(Character):
    def __init__(self, name, hp, ad):
       Character.__init__(self, hp, ad, name)
       self.max_hp = hp
    
    def die(self):
        exit("You died. Try again")
    
    def rest(self):
        self.hp = self.max_hp

class Field:
    def __init__(self, enemies):
        self.enemies = enemies
        self.loot = []

    def print_state(self):
        print("You look around and see")
        for i in self.enemies:
            print(i.name) 

    @staticmethod
    def gen_random():
        rand = random.randint(0,2)
        if rand == 0:
            return Field([]) #keine Gegner drauf
        if rand == 1:
            return Field([Ork()]) #keine Gegner drauf
        if rand == 2:
            return Field([Goblin()]) #keine Gegner drauf
        
        

class Map:
    def __init__(self, width, height):
        self.state = [] #two dimensional map
        self.x = 0
        self.y = 0
        for i in range(width):
            fields = []
            for j in range(height):
                fields.append(Field.gen_random())
            self.state.append(fields)

    def print_state(self):
        self.state[self.x][self.y].print_state()

    def get_enemies(self):
        return self.state[self.x][self.y].enemies
    
    def forward(self):
        if self.x == len (self.state) -1 :
            print("You see huge mountains that you cant pass")
        else:
             self.x = self.x + 1

    def backwards(self):
        if self.x == 0:
             print("You see cliffs, but you can t jump safely")
        else: 
            self.y = self.y -1
    def right(self):
        if self.y == len(self.state[self.x]) - 1:
            print("You see huge mountains which you cant pass")
        else:
            self.y = self.y +1

    def left(self):
        if self.y == 0:
            print("you see Cliffs, but you cant jump safely")
        else:
            self.y = self.y -1 


def forward(p,m):
     m.forward()

def right(p,m):
     m.right()

def left(p,m):
     m.left()

def backwards(p,m):
     m.backwards()

def save():
     pass

def load():
     pass

def quit_game(p,m):
     print("You commit suicide and leave this world")
     exit(0)

def print_help(p,m):
    print(Commands.keys())

def pickup(p,m):
    pass

def fight(p,m):
    enemies = m.get_enemies()
    while len(enemies) > 0:
        enemies[0].get_hit(p.ad)
        if enemies[0].is_dead():
            enemies.remove(enemies[0])
        for i in enemies:
            p.get_hit(i.ad)
        print("You are wounded and have " + str(p.hp) + " hp left")

def rest(p,m):
    p.rest()


Commands = {
    'help': print_help,
    'quit': quit_game,
    'pickup': pickup,
    'forward': forward,
    'right': right,
    'left': left,
    'backwards': backwards,
    'fight': fight,
    'save': save,
    'load': load,
    'rest': rest,

}



if __name__ == '__main__':
    name = input("enter your name")             #name requested and put in
    p = Player(name, 200, 100)                 #player initialized with 1000 hp and 100 ad
    map = Map(5,5)                              # Map initialized with size 5 times 5
    print("(Type help to list the commands available)\n") 

    while True: #GameLoop
        command = input(">").lower().split(" ") #Asks for the command, f.e. forward
        if command[0] in Commands:              # Checks if the command is in the List of Commands
                Commands[command[0]](p, map)    # if it is run function Command
        else:
            print("You run around in circles and don't know what to do")
        map.print_state()


