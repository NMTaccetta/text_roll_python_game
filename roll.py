import random

class Player: 

    def __init__(self):
        self.name = input("> Nombre del personaje: \n")
        self.strengh = 10
        self.agility = 10
        self.constitution = 10
        self.healt = self.constitution * 10
        self.intelligence = 10
        self.mana = self.intelligence * 10

    def choose_class(self):
        chosen = input("Select class: \n> 1- Warrior\n> 2- Mage\n> 3- Rogue\n> 4- Acolyte\n > Number: ")
        if chosen == 1:
            self.strengh = 12
            self.agility = 10
            self.constitution = 12
            self.healt = self.constitution * 10
            self.intelligence = 6
            self.mana = self.intelligence * 10
        if chosen == 2:
            self.strengh = 8
            self.agility = 8
            self.constitution = 8
            self.healt = self.constitution * 10
            self.intelligence = 16
            self.mana = self.intelligence * 10
        if chosen == 3:
            self.strengh = 12
            self.agility = 14
            self.constitution = 8
            self.healt = self.constitution * 10
            self.intelligence = 6
            self.mana = self.intelligence * 10
        if chosen == 4:
            self.strengh = 8
            self.agility = 8
            self.constitution = 12
            self.healt = self.constitution * 10
            self.intelligence = 12
            self.mana = self.intelligence * 10