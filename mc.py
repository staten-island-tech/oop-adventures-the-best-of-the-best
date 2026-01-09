class mc:
    def __init__(self, name, inventory, stats, dialogue, quest, live):
        self.name = name
        self.inventory = inventory
        self.stats = stats
        self.dialogue = dialogue
        self.quest = quest
        self.live = True

    def fight(self):
        while self.live == True:
            print(f"{self.name}, would you like to fight? y/n")
        if "y":
            print(f"{self.name}'s  stats are at {self.stats}.") 
            Hp -= 5
            print(f"{self.name}'s stats are at {self.stats}.")
        else:
            print(f"Get stronger, {self.name}. Maybe another day.")

    
Wavely_Potato = mc("Wavely Potato", ["Sword, healing orb, radishes"], ["Hp = 100, Atk = 20"], ["I come here to kill the King of Yam."], ["Main quest: Go to the village."], ["Live = True"])
        

def talk(self):
        while self.live == True:
            speak = input("Do you want to approach? y/n").lower()
        if speak == "y":
            print("I am humble potato. I seem to have a request for you young lad! My radish seems to have been gone for some time, can you help me find her? Press_Enter to find radish.")
            print(f"Thank you {self.name}! Here is 10 carrot coins")
    
        else:
            print(f"Goodbye {self.name}! Hope to see you again!")
    