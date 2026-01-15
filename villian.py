import mc
import app

class Villian:
    def __init__(self, name, inventory, Hp, dialogue, live):
        self.name = name
        self.inventory = inventory
        self.Hp = Hp
        self.dialogue = dialogue
        self.live = live
        live = True
    
    def steal(self,item):
        print("Let's steal")
        stealing = input("Do you want to steal from the Humble Potato?(yes/no)").lower()
        if stealing.lower() == "yes":
            app.robbery()
            self.inventory.append(item)
            print(f"You stole {item}! Current Inventory: {self.inventory}")
        elif stealing == "no":
            print("Ok, whatever.")
        else:
            print("Invalid choice! Please type yes or no.")

    def fight(self):
            print("You see that guy over there?")
            fight = input("Do you want to fight the Bravely Potato?(yes/no)").lower()
            while fight.lower() == "yes":
                if self.live == True:
                    self.Hp -= 20
                    self.living()
                    self.fight()
                    break
                if self.live == False:
                    self.living()
                break
            if fight.lower() == "no":
                print(f"This is his Hp:{self.Hp}/100")
                self.fight()
            else:
                print("Unvalid choice! Please put a yes/no")
    
    def talk(self):
        print("1) Bravely Potato")
        print("2) Humble Potato")
        speak = input("Who do you want to interact with?").lower()
        if speak == "1":
            print("hmm")
            self.fight()
        elif speak == "2":
            print("Give me all your money")
            self.steal()
        else: 
            print("Character not found! Please type a valid number.")

    def living(self):
        if self.Hp <= 0:
            self.live = False
            print("He is dead")
        elif self.Hp <= 100:
            print(f"Hp: {self.Hp}/100")
        else:
            self.Hp = 100
            print(f"Hp: {self.Hp}/100")
    
    def choice(self):
        activity = input("What do you want to do now? (steal/fight/talk/quit) ").lower()
        if activity == "steal":
            self.steal()
        elif activity == "fight":
            self.fight()
        elif activity == "talk":
            self.talk()
        elif activity == "quit":
            print("OK bro")
            self.choice()
        else:
            print("Invalid choice. Try again!")

King_of_Yam = Villian("King of Yam", ["Prisoners of Yam"], 500, ["I am the all mighty King of Yam"], True)
King_of_Yam.choice()


         
