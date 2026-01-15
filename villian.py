class Villian:
    def __init__(self, name, inventory, Hp, dialogue, live):
        self.name = name
        self.inventory = inventory
        self.Hp = Hp
        self.dialogue = dialogue
        self.live = live

    def steal(self, item):
        stealing = input("Do you want to steal from the Humble Potato? (yes/no) ").lower()
        if stealing == "yes":
            self.inventory.append(item)
            print(f"You stole {item}! Current Inventory: {self.inventory}")
        elif stealing == "no":
            print("Ok, whatever.")
        else:
            print("Invalid choice! Please type yes or no.")

    def fight(self):
        fight = input("Do you want to attack the Waverly Potato? (yes/no) ").lower()
        if fight == "yes":
            self.Hp -= 20
            print(f"You attacked! Hp is now {self.Hp}")
            if self.Hp <= 0:
                self.live = False
                print("The villain is dead!")
        elif fight == "no":
            print(f"The villain's Hp is {self.Hp}")
        else:
            print("Invalid choice! Please type yes or no.")

    def talk(self):
        speak = input("Who do you want to interact with? ").lower()
        if speak == "waverly potato":
            print("Let's fight! I am so much better than you")
        elif speak == "humble potato":
            print("Give me all your money")
        else: 
            print("Character not found! Please type a valid name.")

    def living(self):
        if self.Hp <= 0:
            self.live = False
            print("He is dead")
        elif 20 <= self.Hp <= 50:
            print(f"He is at low health. Hp: {self.Hp}")
        else:
            print(f"He is ok. Hp: {self.Hp}")


King_of_Yam = Villian("King of Yam", ["Prisoners of Yam"], 500, ["I am the all mighty King of Yam"], True)

while King_of_Yam.live:
    activity = input("What do you want to do? (steal/fight/talk/quit) ").lower()
    
    if activity == "steal":
        King_of_Yam.steal("radish")
    elif activity == "fight":
        King_of_Yam.fight()
    elif activity == "talk":
        King_of_Yam.talk()
    elif activity == "quit":
        print("OK bro")
        break
    else:
        print("Invalid choice. Try again!")

print("Bye!")



         
