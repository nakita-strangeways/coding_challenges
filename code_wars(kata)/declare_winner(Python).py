
############
# PLEASE NOTE: Answers are below! Do not look here if you're just trying to find a hint!
############

# Create a function that returns the name of the winner in a fight between two fighters.

# Each fighter takes turns attacking the other and whoever kills the other first is victorious. 
# Death is defined as having health <= 0.

# Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

# Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You 
# can mutate the Fighter objects.

# Example:
# class Fighter(object):
#     def __init__(self, name, health, damage_per_attack):
#         self.name = name
#         self.health = health
#         self.damage_per_attack = damage_per_attack

#     def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
#     __repr__=__str__


############
#  My Code #
############

def declare_winner(fighter1, fighter2, first_attacker):
    
    while True:
        if fighter1.name == first_attacker:
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
        else:
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name


#################
#  Basic Tests  #
#################

Example test cases

test.describe("Example test cases")

test.assert_equals(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"), "Lew")

test.assert_equals(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry"),"Harry")

test.assert_equals(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"),"Harald")

test.assert_equals(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"),"Harald")

test.assert_equals(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"), "Harald")
    
test.assert_equals(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"),"Harald")


###########################################
#  CodeWars Test Results from above code  #
###########################################

# Time: 663ms Passed: 206 Failed: 0
# Test Results:
#  Example test cases
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
#  200 Random test cases
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# Test Passed
# You have passed all of the tests! :)

########################
#  Alternate Solutions #
########################

def declare_winner(fighter1, fighter2, first_attacker):
    current, opponent = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while current.health > 0:        
        opponent.health -= current.damage_per_attack
        current, opponent = opponent, current
    return opponent.name

# 
def declare_winner(fighter1, fighter2, first_attacker):
    # Code your solution here
    if(fighter1.name == first_attacker):
        winner = fight(fighter1,fighter2)
    elif(fighter2.name == first_attacker):
        winner = fight(fighter2,fighter1)
    return winner.name
    
def fight(attacker,defender):
    print('defender: ' + defender.name + ' current health: ' + str(defender.health))
    print('attacker: ' + attacker.name + ' attacks for: ' + str(attacker.damage_per_attack))

    defender.health = defender.health - attacker.damage_per_attack
    print(defender.name + ' health after being attacked is: ' + str(defender.health))
    
    if(defender.health <= 0):
        print('\r\n')
        print(defender.name + ' has been defeated')
        print(attacker.name + ' is the winner!')
        return attacker
    else:
        print('\r\n')
        return fight(defender,attacker)

# 
from math import ceil
def declare_winner(fighter1, fighter2, first_attacker):
    rounds1 = ceil(float(fighter1.health)/fighter2.damage_per_attack)
    rounds2 = ceil(float(fighter2.health)/fighter1.damage_per_attack)
    if rounds1 == rounds2:
        return first_attacker
    else:
        return fighter1.name if (rounds1 > rounds2) else fighter2.name

# 
def declare_winner(fighter1, fighter2, first_attacker):
    if fighter1.name == first_attacker:
        attacker, defender = fighter1, fighter2
    else:
        attacker, defender = fighter2, fighter1
    while True:
        defender.health -= attacker.damage_per_attack
        if defender.health <= 0:
            return attacker.name
        else:
            attacker, defender = defender, attacker