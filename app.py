import random
import
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
        print("nahaha")

    def robbery(self):
        random.choices(self.inventory)
        if random.choice == "radish":
            print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            self.inventory.pop("radish")
        elif random.choices == "groceries":
            print("THEIRD THEIF")
            self.inventory.pop("groceries")

Humble_Potato = npc("Humble Potato", ["No thank you, its ok, fan.", "nananaan im so humble", "nananaan walking my radish"], ["Hello young lad!"], ["radish", "groceries","money"])        

# "Thank you, with such gratitude and grace, for accepting request young, kind lad."
class anpc:
    def _init_(self):
        self.name = anpc

    def infect(self):
        print("big cough, help me get medicine psl")
        self.talk
        print("thank yoaus kind sire")
        self.stats -= 5
        

sick_potato = npc("sick Potato", ["No thank you, its ok, fan.", "nananaan im so humble", "nananaan walking my radish"], ["Hello young lad!"], ["radish", "groceries","money"])