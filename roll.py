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