import random

class merchant:
    def __init__(self, name, stock, dialogue, money):
        self.name = name
        self.stock = stock
        stock = []
        self.dialogue = dialogue
        dialogue = []
        self.money = money
        money = 12000

    def welcome(self):
        random.choice(self.dialogue)
        mc.enter
        print("Go ahead! take your time chap!")
        mc.buy