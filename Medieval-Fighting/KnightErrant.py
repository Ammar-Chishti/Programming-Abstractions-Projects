from CSE216.Homework2.Warrior import *
from CSE216.Homework2.Fight import *


class KnightErrant(Warrior):

    # Add instance variable isTravelling
    def __init__(self, name = None, age = 18, wealth = 1, spear = 0, unarmed_combat = 0, mace = 0, broadsword = 0, isTravelling = False):
        Warrior.__init__(self, name, age, wealth, spear, unarmed_combat, mace, broadsword)

        self._isTravelling = isTravelling

    @property
    def isTravelling(self) -> bool:
        return self._isTravelling

    @isTravelling.setter
    def isTravelling(self, value: bool):
        if not (isinstance(value, bool)):
            raise Exception("Value must be a boolean")

        self._isTravelling = value

    # Added one exception, cannot challenge someone if self is travelling
    def challenge(self, enemy: "Fighter", skill: str):

        # Imports
        from CSE216.Homework2.Warrior import Warrior
        from CSE216.Homework2.KnightErrant import KnightErrant
        from CSE216.Homework2.Fight import Fight

        if (self.isTravelling == True):
            raise Exception("Cannot fight while travelling!")

        super().challenge(enemy, skill)

    """
    Parameters:
        None
    Preconditons:
        -You have been issued a challenge
    Postconditions
        -You accept the first request in your inbox and you two fight
        -If the winner wins against someone that is of the same combatant status or lower, 
        the winner gains 10 wealth, the loser loses 10 wealth, and both participants have the chaince to increase their skill level by 1
        -If the winner wins against someone that is of a status higher, the winner gains 20 wealth, increases their skill by 1, and the loser loses 20 wealth (at a minimum of 0)
        -If the winner wins against someone that is of two status higher, the winner gains 40 wealth, increases their skill by 2, and the loser loses 40 wealth (at a minimum of 0)
    Returns:
        None
    Throws:
        Exception: If you have no requests to accept
    """
    def accept_first(self):
        from CSE216.Homework2.Fight import Fight
        from CSE216.Homework2.KnightErrant import KnightErrant

        result = Fight(self, self._challenges[0], self._challengesSkills[0])
        winner = result.winner
        loser = result.loser

        if (winner is self):

            # If a KnightErrant wins against a KnightErrant
            if isinstance(loser, KnightErrant):

                if (winner.isTravelling == True) or (loser.isTravelling == True):
                    raise Exception("A travelling KnightErrant cannot engage in a Fight!")

                print(winner.__class__.__name__ + " " + str(winner.name) + " has accepted his first challenge with " + loser.__class__.__name__ + " " + str(loser.name) + " with skill " + self._challengesSkills[0] + ".")

                winner.wealth += 10
                print(str(winner.name) + " has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                super().luckUpdateFirst(winner, loser)



            # If a KnightErrant wins against a Warrior
            elif (isinstance(loser, Warrior)):

                if (winner.isTravelling == True):
                    raise Exception("A travelling KnightErrant cannot engage in a Fight!")

                print(winner.__class__.__name__ + " " + str(winner.name) + " has accepted his first challenge with " + loser.__class__.__name__ + " " + str(loser.name) + " with skill " + self._challengesSkills[0] + ".")

                winner.wealth += 10
                print(str(winner.name) + " has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                super().luckUpdateFirst(winner, loser)


            # If a KnightErrant wins against a Fighter
            elif (isinstance(loser, Fighter)):

                if (winner.isTravelling == True):
                    raise Exception("A travelling KnightErrant cannot engage in a Fight!")

                print(winner.__class__.__name__ + " " + str(winner.name) + " has accepted his first challenge with " + loser.__class__.__name__ + " " + str(loser.name) + " with skill " + self._challengesSkills[0] + ".")

                winner.wealth += 10
                print(str(winner.name) + " Has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " Has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " Has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                super().luckUpdateFirst(winner, loser)



        elif (loser is self):

            # If a KnightErrant Wins against a KnightErrant
            if isinstance(winner, KnightErrant):

                if (loser.isTravelling == True):
                    raise Exception("A travelling KnightErrant cannot engage in a fight")

                print(loser.__class__.__name__ + " " + str(loser.name) + " has accepted his first challenge with " + winner.__class__.__name__ + " " + str(winner.name) + " with skill " + self._challengesSkills[0] + ".")

                winner.wealth += 10
                print(str(winner.name) + " Has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " Has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " Has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                super().luckUpdateFirst(loser, winner)

            # If a Warrior wins against a KnightErrant
            elif (isinstance(winner, Warrior)):

                if (loser.isTravelling == True):
                    raise Exception("A travelling KnightErrant cannot engage in a Fight!")

                print(loser.__class__.__name__ + " " + str(loser.name) + " has accepted his first challenge with " + winner.__class__.__name__ + " " + str(winner.name) + " with skill " + self._challengesSkills[0] + ".")

                winner.wealth += 20
                print(str(winner.name) + " has won the fight and increased his wealth by 20 to " + str(winner.wealth) + ".")

                if (loser.wealth < 20):
                    loser.wealth = 0
                    print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 20
                    print(str(loser.name) + " has lost the fight and decreased his wealth by 20 to " + str(loser.wealth))

                if (winner.getSkill(self._challengesSkills[0]) == 10):
                    print("Despite winning, " + str(winner.name) + " cannot increase his " + str(self.challengesSkills[0]) + " skill past 10.")
                else:
                    winner.skillIncrementValue(self._challengesSkills[0])
                    print(str(winner.name) + " was able to increase his " + self._challengesSkills[0] + " skill by 1 to " + str(winner.getSkill(self._challengesSkills[0])) + ".")

            # If a Fighter wins against a KnightErrant
            elif (isinstance(winner, Fighter)):

                if (loser.isTravelling == True):
                    raise Exception("A travelling KnightErrant cannot engage in a Fight!")

                print(winner.__class__.__name__ + " " + str(winner.name) + " has accepted his first challenge with " + loser.__class__.__name__ + " " + str(loser.name) + " with skill " + self._challengesSkills[0] + ".")

                winner.wealth += 40
                print(str(winner.name) + " has won the fight and increased his wealth by 40 to " + str(winner.wealth) + ".")

                if (loser.wealth < 40):
                    loser.wealth = 0
                    print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 40
                    print(str(loser.name) + " has lost the fight and decreased his wealth by 40 to " + str(loser.wealth))

                if (winner.getSkill(self._challengesSkills[0]) == 10):
                    print("Despite winning, " + str(winner.name) + " cannot increase his " + str(self.challengesSkills[0]) + " skill past 10.")
                elif (winner.getSkill(self._challengesSkills[0]) == 9):
                    winner.skillIncrementValue(self._challengesSkills[0])
                    print(str(winner.name) + " was able to increase his " + self._challengesSkills[0] + " skill by 1 to " + str(winner.getSkill(self._challengesSkills[0])) + ".")
                else:
                    winner.skillIncrementValueTwo(self._challengesSkills[0])
                    print(str(winner.name) + " was able to increase his " + self._challengesSkills[0] + " skill by 2 to " + str(winner.getSkill(self._challengesSkills[0])) + ".")


        # Removing the request from the inbox
        self._challenges.pop(0)
        self._challengesSkills.pop(0)

    """
    Parameters:
        None
    Preconditons:
        -You have been issued a challenge
    Postconditions
        -You accept a random challenge request in your inbox and you two fight
        -If the winner wins against someone that is of the same combatant status or lower, 
        the winner gains 10 wealth, the loser loses 10 wealth, and both participants have the chaince to increase their skill level by 1
        -If the winner wins against someone that is of a status higher, the winner gains 20 wealth, increases their skill by 1, and the loser loses 20 wealth (at a minimum of 0)
        -If the winner wins against someone that is of two status higher, the winner gains 40 wealth, increases their skill by 2, and the loser loses 40 wealth (at a minimum of 0)
    Returns:
        None
    Throws:
        Exception: If you have no requests to accept
    """
    def accept_random(self):
        from CSE216.Homework2.Fight import Fight
        from CSE216.Homework2.KnightErrant import KnightErrant

        randIndex = random.randint(0, len(self._challenges) - 1)

        result = Fight(self, self._challenges[randIndex], self._challengesSkills[randIndex])
        winner = result.winner
        loser = result.loser

        if (winner is self):

            # If a KnightErrant wins against a KnightErrant
            if isinstance(loser, KnightErrant):

                if (winner.isTravelling == True) or (loser.isTravelling == True):
                    raise Exception("A travelling KnightErrant cannot engage in a Fight!")

                print(winner.__class__.__name__ + " " + str(winner.name) + " has decided to randomly accept challenge #" + str(randIndex + 1) + " in his inbox and fight: " + loser.__class__.__name__ + " " + str(loser.name) + ". ")

                winner.wealth += 10
                print(str(winner.name) + " has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                super().luckUpdateRandom(winner, loser, randIndex)


            # If a KnightErrant wins against a Warrior
            elif (isinstance(loser, Warrior)):

                if (winner.isTravelling == True):
                    raise Exception("A travelling KnightErrant cannot engage in a Fight!")

                print(winner.__class__.__name__ + " " + str(winner.name) + " has decided to randomly accept challenge #" + str(randIndex + 1) + " in his inbox and fight: " + loser.__class__.__name__ + " " + str(loser.name) + ". ")

                winner.wealth += 10
                print(str(winner.name) + " Has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " Has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " Has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                super().luckUpdateRandom(winner, loser, randIndex)


            # If a KnightErrant wins against a Fighter
            elif (isinstance(loser, Fighter)):

                if (winner.isTravelling == True):
                    raise Exception("A travelling KnightErrant cannot engage in a Fight!")

                print(winner.__class__.__name__ + " " + str(winner.name) + " has decided to randomly accept challenge #" + str(randIndex + 1) + " in his inbox and fight: " + loser.__class__.__name__ + " " + str(loser.name) + ". ")

                winner.wealth += 10
                print(str(winner.name) + " Has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " Has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " Has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                super().luckUpdateRandom(winner, loser, randIndex)



        elif (loser is self):

            # If a KnightErrant wins against a KnightErrant
            if isinstance(winner, KnightErrant):

                if (loser.isTravelling == True) or (winner.isTravelling == True):
                    raise Exception("A travelling KnightErrant cannot engage in a fight")

                print(loser.__class__.__name__ + " " + str(loser.name) + " has decided to randomly accept challenge #" + str(randIndex + 1) + " in his inbox and fight: " + winner.__class__.__name__ + " " + str(winner.name) + ". ")

                winner.wealth += 10
                print(str(winner.name) + " Has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " Has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " Has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                super().luckUpdateRandom(loser, winner, randIndex)

            # If a Warrior wins against a KnightErrant
            elif (isinstance(winner, Warrior)):

                print(loser.__class__.__name__ + " " + str(loser.name) + " has decided to randomly accept challenge #" + str(randIndex + 1) + " in his inbox and fight: " + winner.__class__.__name__ + " " + str(winner.name) + ". ")

                winner.wealth += 20
                print(str(winner.name) + " has won the fight and increased his wealth by 20 to " + str(winner.wealth) + ".")

                if (loser.wealth < 20):
                    loser.wealth = 0
                    print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 20
                    print(str(loser.name) + " has lost the fight and decreased his wealth by 20 to " + str(loser.wealth))

                if (winner.getSkill(self._challengesSkills[0]) == 10):
                    print("Despite winning, " + str(winner.name) + " cannot increase his " + str(self.challengesSkills[randIndex]) + " skill past 10.")
                else:
                    winner.skillIncrementValue(self._challengesSkills[randIndex])
                    print(str(winner.name) + " was able to increase his " + self._challengesSkills[randIndex] + " skill by 1 to " + str(winner.getSkill(self._challengesSkills[randIndex])) + ".")


            # If a Fighter wins against a KnightErrant
            elif (isinstance(winner, Fighter)):

                print(loser.__class__.__name__ + " " + str(loser.name) + " has decided to randomly accept challenge #" + str(randIndex + 1) + " in his inbox and fight: " + winner.__class__.__name__ + " " + str(winner.name) + ". ")

                winner.wealth += 40
                print(str(winner.name) + " has won the fight and increased his wealth by 40 to " + str(winner.wealth) + ".")

                if (loser.wealth < 40):
                    loser.wealth = 0
                    print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 40
                    print(str(loser.name) + " has lost the fight and decreased his wealth by 40 to " + str(loser.wealth))

                if (winner.getSkill(self._challengesSkills[randIndex]) == 10):
                    print("Despite winning, " + str(winner.name) + " cannot increase his " + str(self.challengesSkills[randIndex]) + " skill past 10.")
                elif (winner.getSkill(self._challengesSkills[randIndex]) == 9):
                    winner.skillIncrementValue(self._challengesSkills[randIndex])
                    print(str(winner.name) + " was able to increase his " + self._challengesSkills[0] + " skill by 1 to " + str(winner.getSkill(self._challengesSkills[randIndex])) + ".")
                else:
                    winner.skillIncrementValueTwo(self._challengesSkills[randIndex])
                    print(str(winner.name) + " was able to increase his " + self._challengesSkills[0] + " skill by 2 to " + str(winner.getSkill(self._challengesSkills[randIndex])) + ".")

        # Removing the request from the inbox
        self._challenges.pop(randIndex)
        self._challengesSkills.pop(randIndex)

    # Sets the isTravelling value of self to true
    # If self is already travelling, prints a message and does nothing
    def travel(self):

        if self.isTravelling == True:
            print(str(self.name) + " is already travelling!")
            return

        else:
            print(str(self.name) + " went to go travel.")
            self.isTravelling = True

    # Sets the isTravelling value of self to False
    # If self is not currently travelling, prints a message and does nothing
    def returnFromTravel(self):

        if self.isTravelling == False:
            print(str(self.name) + " is not currently travelling!")
            return
        else:
            if random.random() < 0.2:
                print(str(self.name) + " has returned from travel.")
                print("By rare chance, " + str(self.name) + " has found tresure worth 30 wealth while travelling. Congratulations!")
                self.wealth += 30
                print(str(self.name) + "'s wealth is now " + str(self.wealth) + ".")
                self.isTravelling = False
            else:
                print(str(self.name) + " has returned from travel.")
                print("Unfortunately, " + str(self.name) + " did not find any treasure during his travel.")
                self.isTravelling = False

    def __str__(self):
        return "Name: " + str(self.name) + ", Age: " + str(self.age) + ", Wealth: " + str(self.wealth) + ", Spear: " + str(self.getSkill("spear")) + ", Unarmed_Combat: " + str(self.getSkill("unarmed_combat")) + ", Mace: " + str(self.getSkill("mace")) + ", Broadsword: " + str(self.getSkill("broadsword")) + ", isTravelling: " + str(self._isTravelling)










