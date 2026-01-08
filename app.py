class villian:
    def __init__(self, name, inventory, stats, dialogue):
        self.name = name
        self.inventory = inventory
        self.stats = stats
        self.dialogue = dialogue
    
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
                Hp -= 20
                self.fight
                break
            if fight.lower() == "no":
                print(f"Hp" in {self.stats})
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

King_of_Yam = villian("King of Yam", ["Prisoners of Yam"], ["Hp" == 500, "Atk" == 250], ["I'm am the all mighty King of Yam"])
print(King_of_Yam.__dict__)



         