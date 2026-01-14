class mc:
    def __init__(self, name, inventory, health):
        self.name = name
        self.inventory = inventory
        self.health = health
       
    def heal(self):
        print("Would you like to heal?")
        choose = input("y/n")
        if choose == "y":
            Hp += 10
        if choose == "n":
            print("u sure...? ok..")
        else:
            print("That is not a choice u dum")

    def talk(self):
        print("Do you want to approach?")
        speak = input("y/n")
        if speak == "y":
            print("I am humble potato. I seem to have a request for you young lad! My radish seems to have been gone for some time, can you help me find her? Press_Enter to find radish.")
        if speak == "n":
            print("Goodbye! Come back soon, young lad!")
        else:
            print("That is not a choice u dum")

    def fight(self):
        print(f"{self.name}, would you like to fight?")
        choose = input("y/n")
        if "y":
            print(f"{self.name}'s health is at {self.health}.") 
            Hp -= 5
            print(f"{self.name}'s health are at {self.health}.")
            print("Do you wish to heal? y/n")
            if choose == "y":
                Hp += 10
            if choose == "n":
                print("alright.")
                print(f"{self.name}'s health is at {self.health}")
            else:
                print("That is not a choice u dum")

    def find(self):
        print("You found something rare! Should you..")
        print("1) Pick it up")
        print("2) Leave it there")
    choose = input
    if choose == "1":
        print("Woahh you got a cool sword")
    if choose == "2":
        print("Shouldve taken it but ok")
    else:
        print("That is not a choice u dum")

    
    
        



        
        
        

        
        
       
        