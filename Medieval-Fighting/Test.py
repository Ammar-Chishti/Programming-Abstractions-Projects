from CSE216.Homework2.Person import *
from CSE216.Homework2.Fighter import *
from CSE216.Homework2.Fight import *
from CSE216.Homework2.KnightErrant import *
import random


print("Ammar Chishti CSE 216 Homework #2")
print()

#Testing out Person
next = input("Press any key to test out Person: ")
print()

a = Person()
print("Creating default person a -> " + str(a))
if a.adult == True:
    print(str(a.name) + " is an adult. He has " + str(a.wealth) + " wealth.")
else:
    print(str(a.name) + " is not an adult. He has " + str(a.wealth) + " wealth.")
print("")

b = Person("name", 10, 10)
c = Person("name", 10, 20)
d = Person("nickname", 10, 10)
e = Person("name", 20, 10)

print("Equality checking:")
if (b == c):
    print("Since person b and c have the same name and age. They can be considered equal despite having different wealth amounts.")
if (b != d):
    print("Since person b and d do not have the same name despite having the same age, they are not equal.")
if (b != e):
    print("Since person b and e do not have the same age despite having the same name, they are not equal.")
if (b != a):
    print("Since person b and a have nothing in common, they are not equal.")
print()

print("Creating a person with invalid type parameters: ")
try:
    a = Person(8, "hi", "hello")
except:
    print("Name must be a String. Age must be a number. Wealth must be a number.")
print()

print("Creating a person with negative age: ")
try:
    a = Person("name", -5)
except:
    print("Cannot create a person with negative age!")
print()

print("Creating a person with negative wealth: ")
try:
    a = Person("name", 5, -5)
except:
    print("Cannot create a person with negative wealth!")
print()

a = Person("Ammar", 20, 120)
print("Creating a unique person -> " + str(a))
print("End testing of Person.")
print()

#Testing out Fighter
next = input("Press any key to test out Fighter: ")
print()


print("Creating a Fighter with invalid skill values: ")
try:
    a = Fighter("Ammar", 20, 120, -5, 20, -2, 25)
except:
    print("Skill values must be between 0 and 10.")
print()

print("Creating a Fighter that is less than 18 years old: ")
try:
    a = Fighter("Ammar", 17)
except:
    print("Fighter must be an adult!")
print()

print("Creating a Fighter that has 0 wealth: ")
try:
    a = Fighter("Ammar", 17, 0)
except:
    print("Fighter must have positive wealth!")
print()

print("Fighter attempts to challenge themself. ")
try:
    a = Fighter("Ammar", 20, 120, 5, 5, 5, 5)
    a.challenge(a, "spear")
except:
    print("Fighter cannot challenge themself!")
print()

print("Fighter attempts to challenge a person. ")
try:
    a = Fighter("Ammar", 20, 120, 5, 5, 5, 5)
    b = Person()
    a.challenge(b, "spear")
except:
    print("Fighter must challenge a Fighter!")
print()

print("Fighter challenges a fighter with an invalid skill. ")
try:
    a = Fighter("Ammar", 20, 120, 5, 5, 5, 5)
    b = Fighter()
    a.challenge(b, "Scimitar")
except:
    print("That is not a valid skill!")
print()

print("Fighter challenges a Fighter with skill spear and wins.")
a = Fighter("Ammar", 20, 120, 5, 5, 5, 5)
b = Fighter("Mark", 22, 103, 3, 3, 3, 3)
a.challenge(b, "spear")
print()

print("Fighter challenges a Fighter with skill spear and loses.")
a = Fighter("Ammar", 20, 8, 5, 5, 5, 5)
b = Fighter("Marcus", 22, 103, 8, 8, 8, 8)
a.challenge(b, "spear")
print()

print("Fighter attempts to fight again despite losing all of his wealth.")
try:
    a.challenge(b, "spear")
except:
    print("Cannot engage in a fight if a fighter has 0 wealth!")
print()

print("Fighter wins a fight but has maximum skill level, (keep running until you see)")
a = Fighter("Ammar", 20, 8, 10, 10, 10, 10)
b = Fighter("Marcus", 22, 103, 5, 5, 5, 5)
a.challenge(b, "spear")
print()

print("Two Fighters with equal skill values fight,")
a = Fighter("Ammar", 20, 120, 5, 5, 5, 5)
b = Fighter("Marcus", 22, 103, 5, 5, 5, 5)
a.challenge(b, "spear")
print()

print("End testing of Fighter")
print()

#Testing out Warrior (Values have intentionally been set to 100 for easier debugging)
next = input("Press any key to test out Warrior: ")
print()


#Fighter challenging warrior and warrior accepts first, they fight
#Multiple fighters challenging warrior and warrior accepts random, they fight

print("Fighter challenges a Warrior multiple times with different skills. Warrior accepts first challenge, and fighter wins. Fighter cannot increase his skill level because it is already level 10.")
a = Fighter("Ammar", 100, 100, 10)
b = Warrior("Jason", 100, 100)
a.challenge(b, "spear")
a.challenge(b, "mace")
b.accept_first()
b.printChallenges()
print()

print("Fighter challenges a Warrior. Warrior accepts and fighter loses.")
a = Fighter("Ammar", 100, 100, 2)
b = Warrior("Jason", 100, 100, 5)
a.challenge(b, "spear")
b.accept_first()
print()

print("Warrior challenges a Fighter. Fight happens immediately and Warrior Wins")
a = Warrior("Ammar", 100, 100, 6)
b = Fighter("Harry", 100, 100, 5)
a.challenge(b, "spear")
print()

print("Warrior challenges a Fighter. Fight happens immediately and Warrior loses")
a = Warrior("Ammar", 100, 100, 4)
b = Fighter("Harry", 100, 100, 5)
a.challenge(b, "spear")
print()

print("Warrior a challenges Warrior b, Warrior a wins")
a = Warrior("Ammar", 100, 100, 10)
b = Warrior("Jack", 100, 100, 5)
a.challenge(b, "spear")
b.accept_first()
print()

print("Warrior a challenges Warrior b, Warrior a loses")
a = Warrior("Ammar", 100, 100, 1)
b = Warrior("Jack", 100, 100, 5)
a.challenge(b, "spear")
b.accept_first()
print()


print("Fighter challenges multiple warriors, fights another fighter and loses, and withdraws")
a = Fighter()
b = Warrior("Nick", 100, 100)
c = Warrior("John", 100, 100)
d = Fighter("Mark", 100, 100, 5)
a.challenge(b, "spear")
a.challenge(c, "spear")
a.challenge(d, "spear")
a.withdraw(b, "spear")
print()


print("Multiple fighters challenge Warrior and Warrior accepts random and wins.")
a = Fighter()
b = Fighter("Nick", 100, 100)
c = Fighter("John", 100, 100)
d = Fighter("Thomas", 100, 100)
e = Fighter("Joe", 100, 100)
f = Warrior("Ammar", 100, 100, 5)

a.challenge(f, "spear")
b.challenge(f, "spear")
c.challenge(f, "spear")
d.challenge(f, "spear")
e.challenge(f, "spear")
f.accept_random()
f.printChallenges()
print()


print("Warrior declines the first request from his inbox.")
a = Fighter()
b = Fighter("Nick", 100, 100)
c = Fighter("John", 100, 100)
d = Fighter("Thomas", 100, 100)
e = Fighter("Joe", 100, 100)
f = Warrior("Ammar", 100, 100, 5)

a.challenge(f, "spear")
b.challenge(f, "spear")
c.challenge(f, "spear")
d.challenge(f, "spear")
e.challenge(f, "spear")
f.decline_first()
f.printChallenges()
print()

print("Warrior declines request from his inbox at random.")
a = Fighter()
b = Fighter("Nick", 100, 100)
c = Fighter("John", 100, 100)
d = Fighter("Thomas", 100, 100)
e = Fighter("Joe", 100, 100)
f = Warrior("Ammar", 100, 100, 5)

a.challenge(f, "spear")
b.challenge(f, "spear")
c.challenge(f, "spear")
d.challenge(f, "spear")
e.challenge(f, "spear")
f.decline_random()
f.printChallenges()
print()

print("Fighter successfully withdraws their request to a Warrior.")
a = Fighter()
b = Warrior("Ammar", 100, 100)
a.challenge(b, "spear")
a.withdraw(b, "spear")
print()

print("Warrior tries to withdraw from a Person.")
try:
    a = Warrior()
    b = Person()
    a.withdraw(b, "spear")
except:
    print("Can only withdraw from Warriors!")
print()

print("Warrior tries to withdraw from themself.")
try:
    a = Warrior()
    a.withdraw(a, "spear")
except:
    print("A Fighter cannot withdraw from themself!")
print()

print("Warrior tries to withdraw from someone they never issued a request to.")
try:
    a = Warrior()
    b = Warrior("Ammar", 100, 100)
    a.withdraw(b, "spear")
except:
    print(str(a.name) + " has not issued a request to " + str(b.name) + " with the skill spear")
print()

print("Warrior accepts a request when he has no requests.")
try:
    a = Warrior()
    a.accept_first()
except:
    print("Cannot accept if there are no challenges to accept")
print()

print("Warrior declines a request when there is nothing to decline.")
try:
    a = Warrior()
    a.decline_first()
except:
    print("Cannot decline if there are no challenges to decline.")
print()

print("Warrior A challenges warrior B when B already has a pending challenge towards A with the same skill.")
try:
    a = Warrior()
    b = Warrior("Ammar", 100, 100)
    a.challenge(b, "spear")
    b.challenge(a, "spear")
except:
    print("Cannot challenge someone who has a challenge pending towards you with the same skill!")

print("End testing of Warrior")
print()

#Testing out KnightErrant (Values have intentionally been set to 100 for easier debugging)
next = input("Press any key to test out KnightErrant: ")
print()



print("Creating a default KnightErrant")
a = KnightErrant()
print(a)
print()

print("KnightErrant going on a travel, returning back, and finding treasure (Keep running until you find treasure.")
a = KnightErrant("Ammar", 100, 100)
a.travel()
a.returnFromTravel()
print()

print("KnightErrant returning from travel when he was never travelling at all.")
a = KnightErrant("Ammar", 100, 100)
a.returnFromTravel()
print()

print("KnightErrant travelling again while travelling.")
a = KnightErrant()
a.travel()
a.travel()
print()

print("KnightErrant can store challenges while travelling but cannot accept.")
a = KnightErrant("Ammar", 100, 100)
a.travel()
b = Warrior()
c = Fighter("Jason", 100, 100)
b.challenge(a, "spear")
c.challenge(a, "spear")
try:
    a.accept_first()
except:
    print("A travelling KnightErrant cannot engage in a Fight!")
print()

print("Fighter wins against KnightErrant")
a = Fighter("Ammar", 100, 100, 7)
b = KnightErrant("John", 100, 100, 5)
a.challenge(b, "spear")
b.accept_first()
print()

print("Fighter wins against KnightErrant (with edge cases such as Fighter has skill level 9 and KnightErrant has less than 40 wealth.")
a = Fighter("Ammar", 100, 100, 9)
b = KnightErrant("John", 100, 30, 5)
a.challenge(b, "spear")
b.accept_first()
print()

print("Warrior wins against KnightErrant.")
a = Warrior("Ammar", 100, 100, 5)
b = KnightErrant("John", 100, 100, 4)
b.challenge(a, "spear")
a.accept_first()
print()

print("KnightErrant wins against KnightErrant (at random).")
a = KnightErrant("Ammar", 100, 100, 5)
b = KnightErrant("Jake", 100, 100, 5)
a.challenge(b, "spear")
b.accept_first()
print()

print("KnightErrant wins against Warrior")
a = KnightErrant("Ammar", 100, 100, 6)
b = Warrior("Jake", 100, 100, 5)
a.challenge(b, "spear")
b.accept_first()
print()

print("KnightErrant wins against Fighter")
a = KnightErrant("Ammar", 100, 100, 6)
b = Fighter("Jake", 100, 100, 5)
b.challenge(a, "spear")
a.accept_first()
print()

print("End testing of KnightErrant")
print("End testing of Homework 2")




















