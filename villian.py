
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
            print(self.__dict__)
        elif stealing == "no":
            print("Ok, whatever.")
        else:
            print("Invalid choice! Please put yes or no.")

    def fight(self):
        fight = input("Do you want to fight the Waverly Potato? (yes/no) ").lower()
        if fight == "yes":
            self.Hp -= 20
            print(f"You attacked! Hp is now {self.Hp}")
        elif fight == "no":
            print(f"This is his Hp: {self.Hp}")
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
        if 20 <= self.Hp <= 50:
            print(f"He is at low health. Stats: {self.Hp}")
        elif self.Hp <= 0:
            self.live = False
            print("He is dead")
        else:
            print(f"He is ok. Stats: {self.Hp}")


King_of_Yam = Villian("King of Yam", ["Prisoners of Yam"], 500, ["I am the all mighty King of Yam"], True)

activity = input("What do you want to do? (steal/fight/talk/living) ").lower()
if activity == "steal":
    King_of_Yam.steal("Gold Coin")
elif activity == "fight":
    King_of_Yam.fight()
elif activity == "talk":
    King_of_Yam.talk()
elif activity == "living":
    King_of_Yam.living()
else:
    print("Invalid choice")




         
