from classes.ninja import Ninja
from classes.pirate import Pirate

# isrunning = True

def battle(fighter1, fighter2):
    isrunning = True
    turn_counter = 1
    while(isrunning):
        if(fighter1.health > 0 and fighter2.health > 0):
            fighter1.current_turn += fighter1.speed
            fighter2.current_turn += fighter2.speed
            
            if(fighter1.current_turn >= 100): 
                fighter1.attack(fighter2)
                fighter1.current_turn = 0
                # fighter1.show_stats()
                fighter2.show_stats()
            if(fighter2.current_turn >= 100):
                fighter2.attack(fighter1)
                fighter2.current_turn = 0
                fighter1.show_stats()
                # fighter2.show_stats()
        else:
            isrunning=False
        
michelangelo = Ninja("Michelanglo")

donatelo = Ninja("Donatelo")

jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()
# print("hi")

battle(michelangelo,jack_sparrow)
# battle(donatelo, jack_sparrow)
# battle(michelangelo,donatelo)