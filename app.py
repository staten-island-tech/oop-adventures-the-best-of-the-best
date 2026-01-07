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

    def fight():
        fight = input("Do you want to fight the Waverly Potato?(yes/no)").lower()
        for "Hp" in {self.stats}:
            if fight.lower() == "yes":
                "Hp"-= 5
            elif fight.lower() == "no":
                print(f"Hp" in {self.stats})
            else:
                print("Unvalid choice! Please put a yes/no")

King_of_Yam = villian("King of Yam", ["Prisoners of Yam"], ["Hp" == 500, "Hunger" == 100, "Atk" == 500], ["I'm am the all mighty King of Yam"])
print(King_of_Yam.__dict__)



        