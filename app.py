<<<<<<< HEAD
class villian:
    def __init__(self, name, inventory, Hp, dialogue, live):
        self.name = name
        self.inventory = inventory
        self.Hp = Hp
        self.dialogue = dialogue
        self.live = live
    
    def steal(self,item):
        stealing = input("Do you want to steal from the Humble Potato?(yes/no)").lower()
        if stealing.lower() == "yes":
            self.inventory.append(item)
            print(King_of_Yam.__dict__)
        elif stealing.lower() == "no":
            print("Ok whatever")
        else:
            print("Unvalid choice! Please put a yes or no")

    def fight(self):
            fight = input("Do you want to fight the Waverly Potato?(yes/no)").lower()
            while fight.lower() == "yes":
                self.Hp-= 20
                self.fight
                break
            if fight.lower() == "no":
                print(f"This is his Hp:{self.Hp}")
                self.fight
            else:
                print("Unvalid choice! Please put a yes/no")
    
    def talk(self):
        speak = input("Who do you want to interact with?").lower()
        if speak.lower() == "Waverly Potato":
            print("Let's fight! I am so much better than you")
        elif speak.lower() == "Humble Potato":
            print("Give me all your money")
        else: 
            print("Character unfound! Please type an valid name")

    def living(self):
        if 20 <= self.Hp <= 50:
            print(f"He is at low health. This is his stats {self.stats}" )
        elif self.Hp <= 0:
            self.live == False
            print("He is dead")
        else:
            print(f"He is ok. This is his stats{self.stats}")

King_of_Yam = villian("King of Yam", ["Prisoners of Yam"], 500, ["I'm am the all mighty King of Yam"], True)
print(King_of_Yam.__dict__)





         
=======
import random
class npc:
    def _init_(self, name, dialogue, quest, inventory):
        self.name = name
        self.dialogue = dialogue
        dialogue = []
        self.quest = quest
        quest = []
        self.inventory = inventory
        inventory = []

    def activity(self):
        random.choices(self.quest)
        print(random.choice)
        bigchoice = input("what do you want to do?")
        if big

    def robbery(self):
        random.choices(self.inventory)
        if random.choice == "radish":
            print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            self.inventory.pop("radish")
        elif random.choices == "groceries":
            print("THEIRD THEIF")
            self.inventory.pop("groceries")

Humble_Potato = npc("Humble Potato", ["No thank you, its ok, fan.", "nananaan im so humble", "nananaan walking my radish"], ["Hello young lad!"], ["radish", "groceries","money"])        

class anpc:
    def _init_(self):
        self.name = anpc

    def infect(self):
        print("big cough, help me get medicine psl")
        self.talk
        print("thank yoaus kind sire")
        self.stats -= 5
        

sick_potato = npc("sick Potato", ["No thank you, its ok, fan.", "nananaan im so humble", "nananaan walking my radish"], ["i am humble potato. i see to have a request for you young lad! My radish seems to have been gone for some time, can you help me find her?"], ["radish", "groceries","money"])
>>>>>>> 0cdafb8566416aba4653c8ded03a71fbcc236373
