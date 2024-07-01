class Pokemon:
    def __init__(self,name,health,element):
        self.name = name
        self.health = health
        self.element = element
    
    def doMove(self): # method all pokemon can do
        print("Pokemon Move")

    def doEat(self): # method all pokemon can eat
        print("Pokemon Eat")
        

class Jigglypuff(Pokemon):
    def __init__(self,name,health,element,lungcapacity):
        super().__init__(name,health, element)
        self.lungcapacity = lungcapacity
    
    def doMove(self): # override the parents(pokemon) method 
        super().doMove()
        print("Jigglypuff can Float")

    def __str__(self):
        return f"Name: {self.name}\nhealth: {self.health}\nElement: {self.element}\nLung capacity : {self.lungcapacity}"
        

class Pikachu(Pokemon):
    def __init__(self,name,health,element,electricity):
        super().__init__(name,health,element)
        self.electricity = electricity
    
    def __str__(self):
        return f"Name: {self.name}\nhealth: {self.health}\nElement: {self.element}\nelectricity : {self.electricity}"

import random

class Game:
    def __init__(self):
        self.elements = ["thunder", "fire", "water", "ghost", "ice"]
        self.pokemons = {
            "jigglypuff": [Jigglypuff(f"J{i}", random.randint(50, 100), self.elements[random.randint(0, len(self.elements)-1)], random.randint(80, 100)) for i in range(1, random.randint(3, 15) + 1)],
            "pikachu": [Pikachu(f"P{i}", random.randint(50, 100), self.elements[random.randint(0, len(self.elements)-1)], random.randint(80, 100)) for i in range(1, random.randint(3, 15) + 1)]
        }
    def __str__(self):
        message = ""
        for pokemonname, pokemonlist in self.pokemons.items():
            for pokemon in pokemonlist:
                message += pokemon.__str__() + "\n" + ("-" * 20) + "\n"
        return message
            

class Weapon:
    def __init__(self):
        pass

class Thunderbolt(Weapon):
    def __init__(self, name):
        super().__init__(name)

class Fireball(Weapon):
    def __init__(self, name):
        super().__init__(name)

'''
#pokemon = Pokemon() # create an object of pokemon
pokemon = Jigglypuff("J1", 75,"fairy",92)  # create an object of pokemon
# in the bracket (name,health, element, lung capacity)
pokemon.doMove()
'''
game = Game()
print(game)




