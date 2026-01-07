class villian:
    def __init__(self, name, inventory, stats, dialogue):
        self.name = name
        self.inventory = inventory
        self.stats = stats
        self.dialogue = dialogue
    
    def steal(self,item):
        stealing = input("Do you want to steal from the Humble Potato?(yes/no)")
        if stealing == "yes":
            self.inventory.append(item)
            print(King_of_Yam.__dict__)

King_of_Yam = villian("King of Yam", ["Prisoners of Yam"], ["Hp" == 500, "Hunger" == 100, "Atk" == 500], ["I'm am the all mighty King of Yam"])
print(King_of_Yam.__dict__)


        