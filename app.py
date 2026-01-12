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