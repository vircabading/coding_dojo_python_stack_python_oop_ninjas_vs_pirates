import random
class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.current_turn = 0
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        print(f"{self.name}'s turn to attack {pirate.name}")
        pirate.health -= random.randint(0, self.strength)
        return self


# 1 customize attack function
# 2 create a battle function
# 3 instance of a battle(thunderdome style)
#bonus is static and class method