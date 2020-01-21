from CSE216.Homework2.Person import *
import random

class Fighter(Person):

    # Constructor
    # Checks to see if skills are in valid range. If not throw exception
    # Checks to see if fighters are created with postive wealth. If not throw exception
    def __init__(self, name = None, age = 18, wealth = 1, spear = 0, unarmed_combat = 0, mace = 0, broadsword = 0):

        self.__skills = {"spear": 0, "unarmed_combat": 0, "mace": 0, "broadsword": 0}

        Person.__init__(self, name, age, wealth)
        self.__skills["spear"] = spear
        self.__skills["unarmed_combat"] = unarmed_combat
        self.__skills["mace"] = mace
        self.__skills["broadsword"] = broadsword

        for key in self.__skills:
            if (self.__skills[key] > 10) or (self.__skills[key] < 0):
                raise Exception("Skills must be between 0 and 10.")

        if self.wealth < 1:
            raise Exception("Fighters must be created with positive wealth!")


    @Person.age.setter
    def age(self, value: int):

        if not (isinstance(value, (int, float, complex))):
            raise Exception("Age must be a positive number.")

        elif (value < 18):
            raise Exception("Fighter must be an adult.")

        self._adult = True
        self._age = value

    @Person.wealth.setter
    def wealth(self, value: int):

        if not (isinstance(value, (int, float, complex))):
            raise Exception("Wealth must be a positive number.")

        elif (value < 0):
            raise Exception("Wealth cannot be negative.")

        #elif (value < 1):
            #raise Exception("Wealth must be positive.")

        self._wealth = value

    #Skill getter
    def getSkill(self, skill: str) -> int:

        skill = skill.lower()
        if (not (skill == "spear")) and (not (skill == "unarmed_combat")) and (not (skill == "mace")) and (not (skill == "broadsword")):
            raise Exception("That is not a valid skill!")

        return self.__skills[skill]

    # For when a Fighter wins against someone that is a level above their class. Increment their skill value by 1
    def skillIncrementValue(self, skill: str):

        skill = skill.lower()
        if (not (skill == "spear") and (not (skill == "unarmed_combat")) and (not ("mace")) and (not skill == "spear")):
            raise Exception("That is not a valid skill!")

        if (self.__skills[skill] == 10):
            return

        self.__skills[skill] += 1

    # For when an actual type Fighter wins against a KnightErrant. Increment their skill value by 2
    def skillIncrementValueTwo(self, skill: str):

        skill = skill.lower()
        if (not (skill == "spear") and (not (skill == "unarmed_combat")) and (not ("mace")) and (not skill == "spear")):
            raise Exception("That is not a valid skill!")

        if (self.__skills[skill] == 10):
            return

        self.__skills[skill] += 2


    """
    Parameters:
        enemy: The enemy you are challenging
        skill: The skill you are challenging the enemy with
    Preconditons:
        -The enemy you are challenging has been instantiated
        -The enemy you are challenging is a Fighter or a subtype
        -You are challenging an enemy with a valid skill
    Postconditions
        -If you are challenging a Fighter, the winner gains 10 wealth and the chance to increase their skill by 1, 
        the loser loses 10 wealth (at a minimum of 0) and has the chance to increase their skill by 1
        -If you are challenging a KnightErrant or Warrior, leave the request in their inbox
    Returns:
        None
    Throws:
        Exception: If you do not challenge a Fighter or subclass
        Exception: If the skill you specify in your challenge is invalid
        Exception: If you challenge yourself
        Exception: If you try to issue a challenge with 0 wealth
    """
    def challenge(self, enemy: "Fighter", skill: str):

        #Imports
        from CSE216.Homework2.Warrior import Warrior
        from CSE216.Homework2.KnightErrant import KnightErrant
        from CSE216.Homework2.Fight import Fight

        ##
        # This section is for ensuring all conditions of a challenge are peroperly met
        ##
        skill = skill.lower()   #For checking if skill is a valid String

        # You cannot challenge somebody again with the same skill
        if (isinstance(enemy, Warrior)):
            for c in range(len(enemy.challenges)):
                if self == enemy.challenges[c]:
                    if skill == enemy.challengesSkills[c]:
                        raise Exception("Cannot challenge someone with the same skill!")

        if (not (isinstance(enemy, Fighter))):
            raise Exception("Must challenge a Fighter!")

        elif (self == enemy):
            raise Exception("A fighter cannot fight themselves!")

        elif (self.wealth == 0) or (enemy.wealth == 0):
            raise Exception("Cannot engage in a fight if a fighter has 0 wealth!")

        elif (not (skill == "spear")) and (not (skill == "unarmed_combat")) and (not (skill == "mace")) and (not (skill == "broadsword")):
            raise Exception("That is not a valid skill!")


        if (isinstance(enemy, KnightErrant)):

            # Update your enemy's challenges list with corresponding skill
            enemy.update(self, skill)

        elif (isinstance(enemy, Warrior)):

            # Update your enemy's challenges list with corresponding skill
            enemy.update(self, skill)

        #If a Fighter fights a Fighter
        elif (isinstance(enemy, Fighter)):

            print(self.__class__.__name__ + " " + str(self.name) + " has engaged in a fight with " + self.__class__.__name__ + " " + str(enemy.name) + " with skill " + skill + ".")

            result = Fight(self, enemy, skill)
            winner = result.winner
            loser = result.loser

            winner.wealth += 10
            print(str(winner.name) + " has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

            if (loser.wealth < 10):
                loser.wealth = 0
                print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
            else:
                loser.wealth -= 10
                print(str(loser.name) + " has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

            if (random.random() < 0.5):
                if (winner.getSkill(skill)) == 10:
                    print("Despite being lucky, " + str(winner.name) + " cannot increase his " + str(skill) + " skill past 10.")
                else:
                    winner.skillIncrementValue(skill)
                    print("Through random chance, " + str(winner.name) + " was able to increase his " + str(skill) + " skill by 1 to " + str(winner.getSkill(skill)) + ".")

            if (random.random() < 0.5):
                if (loser.getSkill(skill)) == 10:
                    print("Despite being lucky, " + str(loser.name) + " cannot increase his " + str(skill) + " skill past 10.")
                else:
                    loser.skillIncrementValue(skill)
                    print("Through random chance, " + str(loser.name) + " was able to increase his " + str(skill) + " skill by 1 to " + str(loser.getSkill(skill)) + ".")

        else:
            raise Exception("Fight can only occur between two Fighters!")

    """
    Parameters:
        enemy: The enemy you are withdrawing from
        skill: The skill you previously requested a challenge with
    Preconditons:
        -You previously challenged an enemy with a skill and they ignored it
    Postconditions
        -The request in the enemey's inbox has been removed
    Returns:
        None
    Throws:
        Exception: If you specify an invalid skill
        Exception: If you try to withdraw from yourself
        Exception: If you try to withdraw from a Warrior that you never issued a challenge to
    """
    def withdraw(self, enemy: "Fighter", skill: str):

        #Imports
        from CSE216.Homework2.Warrior import Warrior
        from CSE216.Homework2.KnightErrant import KnightErrant

        if (isinstance(enemy, Warrior)):

            if (self == enemy):
                raise Exception("A Fighter cannot withdraw from themself!")

            elif (not (skill == "spear")) and (not (skill == "unarmed_combat")) and (not (skill == "mace")) and (not (skill == "broadsword")):
                raise Exception("That is not a valid skill!")

            if (self in enemy.challenges):
                removeIndex = enemy.challenges.index(self)

                enemy.challenges.pop(removeIndex)
                enemy.challengesSkills.pop(removeIndex)
                print("Removed " + str(self.name) + "'s request from " + str(enemy.name) + "'s inbox of challenges.")
            else:
                raise Exception(str(self.name) + " has not issued a request to " + str(enemy.name) + " with the skill " + skill + ".")

        else:
            raise Exception("Can only withdraw requests from Warriors!")

    def __str__(self):
        return "Name: " + str(self.name) + ", Age: " + str(self.age) + ", Wealth: " + str(self.wealth) + ", Spear: " + str(self.getSkill("spear")) + ", Unarmed_Combat: " + str(self.getSkill("unarmed_combat")) + ", Mace: " + str(self.getSkill("mace")) + ", Broadsword: " + str(self.getSkill("broadsword"))










