import random
import app
import villian

class mc:
    def __init__(self, name, inventory, health, alive):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.alive = alive

    def heal(self):
        print("Would you like to heal?")
        choose = input("y/n")
        if choose == "y":
            self.health += 10
            if self.health > 100:
                self.health = 100
            elif self.alive == False:
                print("ur dead")       
        elif choose == "n":
            print("u sure...? ok..")
        else:
            print("That is not a choice u dum")

    def talk(self):
        print("Do you want to approach?")
        speak = input("y/n")
        if speak == "y":
            app.activity()
        elif speak == "n":
            app.rejected()
        else:
            print("That is not a choice u dum")

    def fight(self):
        print(f"{self.name}, would you like to fight?")
        choose = input("y/n")
        if choose == "y":
            print(f"{self.name}'s health is at {self.health}/100.") 
            self.health -= 5
            print(f"{self.name}'s health are at {self.health}/100.")
            self.heal()

    def find(self):
        print("1) Pick it up")
        print("2) Leave it there")
        choose = input("You found something rare! Should you..")
        if choose == "1":
            print("Woahh you got a cool sword")
            self.inventory.append("sword")
        elif choose == "2":
            print("Shouldve taken it but ok")
        else:
            print("That is not a choice u dum")

    def steal(self):
        stealing = input("Do you want to steal from Humble Potato?(y/n)").lower()
        if stealing.lower() == "y":
            item = app.robbery()
            self.inventory.append(item)
            print(f"You stole {item}! Current Inventory: {self.inventory}")
        elif stealing == "n":
            print("Better not to")
        else:
            print("Invalid choice! Please type yes or no.")

    def choice(self):
        activity = input("What do you want to do now? (fight/talk/find/steal/quit)").lower()
        if activity == "steal":
            self.steal()
        elif activity == "fight":
            self.fight()
        elif activity == "talk":
            self.talk()
        elif activity == "quit":
            print("brah")
            self.choice()
        else:
            print("Invalid choice. Try again!")


Bravely_Potato = mc("Bravely Potato", ["cool plot armour"], 100, True)
Bravely_Potato.choice()
#     speak = input("The King of Yam is going to take this village prisoner. Help them!")
#     speak = input("Humble Potato wants to talk to you. Do you approach? y/n ")
#     if speak == "y":
# print(self.talk)
        



        
        
        

        
        
       
        