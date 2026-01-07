class mc:
    def __init__(self, name, inventory, stats, dialogue, quest):
        self.name = name
        self.inventory = inventory
        self.stats = stats
        self.dialogue = dialogue
        self.quest = quest

    


Wavely_Potato = mc("Wavely_Potato", ["sword, chips, health orb"], "Health = 100, Hunger = 100, Atk = 15", ["I am Wavely Potato. i embark on a quest to kill the King of Yam."], ["Main Questline: Prisoners of Yam."])


speak = input("Do you want to approach? y/n")
if "y":
    print("I am humble potato. I seem to have a request for you young lad! My radish seems to have been gone for some time, can you help me find her?")
else:
    print("Goodbye kind lad! Hope to see you again!")
