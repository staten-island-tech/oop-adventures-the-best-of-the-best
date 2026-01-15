import random
import app
import villian
import nana

class mc:
    def __init__(self, name, inventory, health, alive):
        self.name = name
        self.inventory = inventory
        inventory = []
        self.health = health
        health = 100
        self.alive = alive
        alive = True

    def heal(self):
        print("Would you like to heal?")
        choose = input("y/n")
        if choose == "y":
            health += 10
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
            print(random.choice)
            app.activity
        if speak == "n":
            app.rejected
        else:
            print("That is not a choice u dum")

    def fight(self):
        print(f"{self.name}, would you like to fight?")
        choose = input("y/n")
        if "y":
            print(f"{self.name}'s health is at {self.health}/100.") 
            self.health -= 5
            print(f"{self.name}'s health are at {self.health}/100.")
            print("Do you wish to heal? y/n")
            if choose == "y":
                self.health += 10
            if choose == "n":
                print("alright.")
                print(f"{self.name}'s health is at {self.health}/100")
            else:
                print("That is not a choice u dum")

    def find(self):
        choose = input("You found something rare! Should you..")
        print("1) Pick it up")
        print("2) Leave it there")
        if choose == "1":
            print("Woahh you got a cool sword")
            self.inventory.append("sword")
        if choose == "2":
         print("Shouldve taken it but ok")
        else:
          print("That is not a choice u dum")

#     def buy(self):
#         nana


    
#     speak = input("The King of Yam is going to take this village prisoner. Help them!")
#     speak = input("Humble Potato wants to talk to you. Do you approach? y/n ")
#     if speak == "y":
# print(self.talk)
        



        
        
        

        
        
       
        