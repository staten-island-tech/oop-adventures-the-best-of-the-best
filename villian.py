class villian:
    def __init__(self, name, inventory, Hp, dialogue, live):
        self.name = name
        self.inventory = inventory
        self.Hp = Hp
        self.dialogue = dialogue
        self.live = live
    
    def steal(self,item):
        print("Let's steal")
        stealing = input("Do you want to steal from the Humble Potato?(yes/no)").lower()
        if stealing.lower() == "yes":
            self.inventory.append(item)
            print(King_of_Yam.__dict__)
        elif stealing.lower() == "no":
            print("Ok whatever")
        else:
            print("Unvalid choice! Please put a yes or no")

    def fight(self):
            print("You see that guy over there?")
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
        print("Hey you see that potato. Let's go up to them")
        speak = input("Who do you want to interact with?").lower()
        if speak.lower() == "Waverly Potato":
            print("Let's fight! I am so much better than you")
        elif speak.lower() == "Humble Potato":
            print("Give me all your money")
        else: 
            print("Character unfound! Please type an valid name")

    def living(self):
        if 20 <= self.Hp <= 50:
            print(f"He is at low health. This is his stats {self.Hp}" )
        elif self.Hp <= 0:
            self.live == False
            print("He is dead")
        else:
            print(f"He is ok. This is his stats{self.Hp}")
        
King_of_Yam = villian("King of Yam", ["Prisoners of Yam"], 500, ["I'm am the all mighty King of Yam"], True)
activites = input("What do you want to do?")
print(King_of_Yam.__dict__)





         
