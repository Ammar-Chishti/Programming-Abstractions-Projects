from CSE216.Homework2.Fighter import *
from CSE216.Homework2.Warrior import *
from CSE216.Homework2.KnightErrant import *
import random

class Fight:

    # Checks to see if participants are fighters and if they are, let's them fight
    def __init__(self, a, b, skill):

        skill = skill.lower()

        if isinstance(a, Fighter):
            if isinstance(b, Fighter):
                self.winner = Fight.winner(a, b, a.getSkill(skill), b.getSkill(skill))
        else:
            raise Exception("Fight can only occur between two Fighters!")

        if (self.winner is a):     #To find out who the loser is
            self.loser = b
        elif (self.winner is b):
            self.loser = a

    # Calculates the winner between two Fighters based on their respective skill values
    @staticmethod
    def winner(a: "Fighter", b: "Fighter", a_skill_level: int, b_skill_level: int) -> "Fighter":

        if (a_skill_level > b_skill_level):
            return a

        elif (a_skill_level < b_skill_level):
            return b

        elif (a_skill_level == b_skill_level):
            choices = [a, b]
            return random.choice(choices)







