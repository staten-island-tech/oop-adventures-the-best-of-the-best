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
        talk = random.choices(self.dialogue)
        print(talk)
        alert = random.choices(self.quest)
        print(alert)
    
    def talkself(self):
        talk = random.choices(self.dialogue)
        print(talk)

    def rejected(self):
        print("Goodbye! Thank you young lad!")
            
    def robbery(self):
        item = random.choices(self.inventory)
        if item == "radish":
            print("NOOOOOOOOOOOOOOOOO!!!! WE CANNOT BOTH SHARE HIM")
        elif item == "groceries":
            print("KIDNAPPER!!!111! IM BABYSITTING THEM 11!!!")
        elif item == "money":
            print("I thought radish hood stole from the rich to give to the poor!! IM NOT RICH!111!!!!!!!!!!")
        else:
            print("oh sad! despair! but i am humble")
        self.inventory.remove(item)

Humble_Potato = npc("Humble Potato", ["No thank you, its ok, fan.", "nananaan im so humble", "nananaan walking my radish"], ["Hello young lad!"], ["radish", "groceries","money"])        