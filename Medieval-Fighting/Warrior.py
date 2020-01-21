from CSE216.Homework2.Fighter import *

class Warrior(Fighter):

    # New variables includes lists to hold challenges with respective skills
    def __init__(self, name = None, age = 18, wealth = 1, spear = 0, unarmed_combat = 0, mace = 0, broadsword = 0):

        Fighter.__init__(self, name, age, wealth, spear, unarmed_combat, mace, broadsword)

        if self.wealth < 1:
            raise Exception("Warriors must be created with positive wealth!")

        self._challenges = []
        self._challengesSkills = []

    @property
    def challenges(self) -> list:
        return self._challenges

    @property
    def challengesSkills(self) -> list:
        return self._challengesSkills

    """
    Parameters:
        enemy: The enemy you are challenging
        skill: The skill you are challenging the enemy with
    Preconditons:
        -The enemy you are challenging has been instantiated
        -The enemy you are challenging is a Fighter or a subtype
        -You are challenging an enemy with a valid skill
    Postconditions
        -If you are challenging a Fighter, the winner gains 10 wealth and the chance to increase their skill by 1, the loser loses 10 wealth and the chance to increase their skill by 1
        -If you are challenging a KnightErrant or Warrior, leave the request in their inbox
    Returns:
        None
    Throws:
        Exception: If you do not challenge a Fighter or subclass
        Exception: If the skill you specify in your challenge is invalid
        Exception: If you challenge yourself
        Exception: If you try to issue a challenge with 0 wealth
        Exception: If the enemy you are challenging has a pending request towards you
    """
    def challenge(self, enemy: "Fighter", skill: str):

        #Imports
        from CSE216.Homework2.Warrior import Warrior
        from CSE216.Homework2.KnightErrant import KnightErrant
        from CSE216.Homework2.Fight import Fight

        ##
        # This section is for ensuring all conditions of a challenge are peroperly met
        ##
        skill = skill.lower()  # For checking if skill is a valid String

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

        # If a Warrior fights a Fighter
        elif (isinstance(enemy, Fighter)):

            print(self.__class__.__name__ + " " + str(
                self.name) + " has engaged in a fight with " + self.__class__.__name__ + " " + str(
                enemy.name) + " with skill " + skill + ".")

            result = Fight(self, enemy, skill)
            winner = result.winner
            loser = result.loser

            if (isinstance(winner, Warrior)):

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
                        print("Despite being lucky, " + str(winner.name) + " cannot increase his " + str(
                            skill) + " skill past 10.")
                    else:
                        winner.skillIncrementValue(skill)
                        print("Through random chance, " + str(winner.name) + " was able to increase his " + str(
                            skill) + " skill by 1 to " + str(winner.getSkill(skill)) + ".")

                if (random.random() < 0.5):
                    if (loser.getSkill(skill)) == 10:
                        print("Despite being lucky, " + str(loser.name) + " cannot increase his " + str(
                            skill) + " skill past 10.")
                    else:
                        loser.skillIncrementValue(skill)
                        print("Through random chance, " + str(loser.name) + " was able to increase his " + str(
                            skill) + " skill by 1 to " + str(loser.getSkill(skill)) + ".")

            elif (isinstance(winner, Fighter)):

                winner.wealth += 25
                print(str(winner.name) + " has won the fight and increased his wealth by 25 to " + str(
                    winner.wealth) + ".")

                if (loser.wealth < 25):
                    loser.wealth = 0
                    print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= -25
                    print(
                        str(loser.name) + " has lost the fight and decreased his wealth by 25 to " + str(loser.wealth))

                if (random.random() < 0.5):
                    if (winner.getSkill(skill)) == 10:
                        print("Despite being lucky, " + str(winner.name) + " cannot increase his " + str(
                            skill) + " skill past 10.")
                    else:
                        winner.skillIncrementValue(skill)
                        print("Through random chance, " + str(winner.name) + " was able to increase his " + str(
                            skill) + " skill by 1 to " + str(winner.getSkill(skill)) + ".")

                if (random.random() < 0.5):
                    if (loser.getSkill(skill)) == 10:
                        print("Despite being lucky, " + str(loser.name) + " cannot increase his " + str(
                            skill) + " skill past 10.")
                    else:
                        loser.skillIncrementValue(skill)
                        print("Through random chance, " + str(loser.name) + " was able to increase his " + str(
                            skill) + " skill by 1 to " + str(loser.getSkill(skill)) + ".")



        else:
            raise Exception("Fight can only occur between two Fighters!")

        #super().challenge(enemy, skill)

    """
    Parameters:
        challengerFrom: Fighter that is challenging you
        skill: The skill that the Fighter is challenging you with
    Preconditons:
        -Skill is a valid input
        -The fighter that is challenging you is valid
    Postconditions
        -Your challenges and challengesSkills list (or your inbox) is updated to store the challenger's request.
    Returns:
        None
    Throws:
        Exception: If skill is not valid
        Exception: If the person challenging you is not a Fighter
    """
    def update(self, challengerFrom: "Fighter", skill: str):

        #Imports
        from CSE216.Homework2.Fight import Fight

        skill = skill.lower()  # For checking if skill is a valid String
        if (not (skill == "spear")) and (not (skill == "unarmed_combat")) and (not (skill == "mace")) and (not (skill == "broadsword")):
            raise Exception("That is not a valid skill!")

        if (not isinstance(challengerFrom, Fighter)):
            raise Exception("Cannot accept a challenge from a person that is not a Fighter!")

        if isinstance(challengerFrom, Fighter):
            self._challenges.append(challengerFrom)
            self._challengesSkills.append(skill)

            print(str(self.name) + " has received a challenge from " + str(challengerFrom.name) + ".") #What does " + str(self.name) + " want to do?")
            print(str(self.name) + "'s inbox of challenges ordered by precedence (fifo):")

            #Printing all challenges in inbox
            i = 1
            for x in range(len(self._challenges)):
                print("Challenge #" + str(i) + ":  Name: " + str(self._challenges[x].name) + ", skill: " + self._challengesSkills[x])
                i += 1
            print()
    """
            decision = input("Does " + str(self.name) + " want to accept, decline or ignore a message?: ")

            #Decision error checking
            decision = decision.lower()
            if (not (decision == "accept")) and (not (decision == "decline")) and (not (decision == "ignore")):
                raise Exception("That is not a valid decision! Valid decisions are accept, ignore, or decline.")

            if (decision == "accept"):
                order = input("Does " + str(self.name) + " want to accept the first challenge in his inbox or a random one? (first) (random): ")
                print("")
                order = order.lower()

                if (order == "first"):
                    self.accept_first()

                elif (order == "random"):
                    self.accept_random()

                else:
                    raise Exception("That is not a valid decision! Valid decisions are first or random.")

            elif (decision == "decline"):
                order = input("Does " + str(self.name) + " want to decline the first challenge in his inbox or a random one? (first) (random): ")
                order = order.lower()

                if (order == "first"):
                    self.decline_first()

                elif (order == "random"):
                    self.decline_random()

                else:
                    raise Exception("That is not a valid decision! Valid decisions are first or random.")

            elif (decision == "ignore"):
                print("Ignoring challenge request.\n")
                return
    """

    # This is a helper function used to help update a winner and loser's skill level based on chance. It is used in the accept_first() function
    def luckUpdateFirst(self, me: "Fighter", other: "Fighter"):

        # Determining who gets to increase their skills due to luck
        if (random.random() < 0.5):
            if me.getSkill(self._challengesSkills[0]) == 10:
                print("Despite being lucky, " + str(me.name) + " cannot increase his " + str(self.challengesSkills[0]) + " skill past 10.")
            else:
                me.skillIncrementValue(self._challengesSkills[0])
                print("Through random chance, " + str(me.name) + " was able to increase his " + self._challengesSkills[0] + " skill by 1 to " + str(me.getSkill(self._challengesSkills[0])) + ".")

        if (random.random() < 0.5):
            if other.getSkill(self._challengesSkills[0]) == 10:
                print("Despite being lucky, " + str(other.name) + " cannot increase his " + str(self.challengesSkills[0]) + " skill past 10.")
            else:
                other.skillIncrementValue(self._challengesSkills[0])
                print("Through random chance, " + str(other.name) + " was able to increase his " + self._challengesSkills[0] + " skill by 1 to " + str(other.getSkill(self._challengesSkills[0])) + ".")

    # This is a helper function used to help update a winner and loser's skill level based on chance. It is used in the accept_random() function
    def luckUpdateRandom(self, me: "Fighter", other: "Fighter", index: int):

        # Determining who gets to increase their skills due to luck
        if (random.random() < 0.5):
            if me.getSkill(self._challengesSkills[index]) == 10:
                print("Despite being lucky, " + str(me.name) + " cannot increase his " + str(self.challengesSkills[index]) + " skill past 10.")
            else:
                me.skillIncrementValue(self._challengesSkills[index])
                print("Through random chance, " + str(me.name) + " was able to increase his " + self._challengesSkills[index] + " skill by 1 to " + str(me.getSkill(self._challengesSkills[index])) + ".")

        if (random.random() < 0.5):
            if other.getSkill(self._challengesSkills[index]) == 10:
                print("Despite being lucky, " + str(other.name) + " cannot increase his " + str(self.challengesSkills[index]) + " skill past 10.")
            else:
                other.skillIncrementValue(self._challengesSkills[index])
                print("Through random chance, " + str(other.name) + " was able to increase his " + self._challengesSkills[index] + " skill by 1 to " + str(other.getSkill(self._challengesSkills[index])) + ".")

    """
    Parameters:
        None
    Preconditons:
        -You have been issued a challenge
    Postconditions
        -You accept the first challenge request in your inbox and you two fight
        -If the winner wins against someone that is of the same combatant status or lower, 
        the winner gains 10 wealth, the loser loses 10 wealth, and both participants have the chaince to increase their skill level by 1
        -If the winner wins against someone that is of a status higher, the winner gains 20 wealth, increases their skill by 1, and the loser loses 20 wealth (at a minimum of 0)
    Returns:
        None
    Throws:
        Exception: If you have no requests to accept
    """
    def accept_first(self):
        from CSE216.Homework2.Fight import Fight
        from CSE216.Homework2.KnightErrant import KnightErrant

        if not (self._challenges):
            raise Exception("Cannot accept if there are no challenges to accept.\n")

        result = Fight(self, self._challenges[0], self._challengesSkills[0])
        winner = result.winner
        loser = result.loser

        if (winner is self):

            # If a Warrior wins against a KnightErrant
            if isinstance(loser, KnightErrant):

                print(winner.__class__.__name__ + " " + str(winner.name) + " has accepted his first challenge with " + loser.__class__.__name__ + " " + str(loser.name) + " with skill " + self._challengesSkills[0] + ".")

                winner.wealth += 20
                print(str(winner.name) + " has won the fight and increased his wealth by 20 to " + str(winner.wealth) + ".")

                if (loser.wealth < 20):
                    loser.wealth = 0
                    print(loser.name + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 20
                    print(str(loser.name) + " has lost the fight and decreased his wealth by 20 to " + str(loser.wealth))

                if (winner.getSkill(self._challengesSkills[0]) == 10):
                    print("Despite winning, " + str(winner.name) + " cannot increase his " + str(self.challengesSkills[0]) + " skill past 10.")
                else:
                    winner.skillIncrementValue(self._challengesSkills[0])
                    print(str(winner.name) + " was able to increase his " + self._challengesSkills[0] + " skill by 1 to " + str(winner.getSkill(self._challengesSkills[0])) + ".")


            # If a Warrior wins against a Warrior
            elif (isinstance(loser, Warrior)):
                print(winner.__class__.__name__ + " " + str(winner.name) + " has accepted his first challenge with " + loser.__class__.__name__ + " " + str(loser.name) + " with skill " +self._challengesSkills[0] + ".")

                winner.wealth += 10
                print(str(winner.name) + " Has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " Has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " Has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                self.luckUpdateFirst(winner, loser)


            # If a Warrior wins against a Fighter
            elif (isinstance(loser, Fighter)):

                print(winner.__class__.__name__ + " " + str(winner.name) + " has accepted his first challenge with " + loser.__class__.__name__ + " " + str(loser.name) + " with skill " + self._challengesSkills[0] + ".")

                winner.wealth += 10
                print(str(winner.name) + " Has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " Has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " Has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                self.luckUpdateFirst(winner, loser)



        elif (loser is self):

            # If a KnightErrant Wins against a Warrior
            if isinstance(winner, KnightErrant):

                print(loser.__class__.__name__ + " " + str(loser.name) + " has accepted his first challenge with " + winner.__class__.__name__ + " " + winner.name + " with skill " + self._challengesSkills[0] + ".")

                winner.wealth += 10
                print(str(winner.name) + " Has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " Has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " Has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                self.luckUpdateFirst(loser, winner)

            # If a Warrior wins against a Warrior
            elif (isinstance(winner, Warrior)):

                print(loser.__class__.__name__ + " " + str(loser.name) + " has accepted his first challenge with " + winner.__class__.__name__ + " " + winner.name + " with skill " + self._challengesSkills[0] + ".")

                winner.wealth += 10
                print(str(winner.name) + " has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                self.luckUpdateFirst(loser, winner)

            # If a Fighter wins against a Warrior
            elif (isinstance(winner, Fighter)):

                print(loser.__class__.__name__ + " " + str(loser.name) + " has accepted his first challenge with " + winner.__class__.__name__ + " " + winner.name + " with skill " + self._challengesSkills[0] + ".")

                winner.wealth += 25
                print(str(winner.name) + " has won the fight and increased his wealth by 25 to " + str(winner.wealth) + ".")

                if (loser.wealth < 25):
                    loser.wealth = 0
                    print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 25
                    print(str(loser.name) + " has lost the fight and decreased his wealth by 25 to " + str(loser.wealth))

                if (winner.getSkill(self._challengesSkills[0]) == 10):
                    print("Despite winning " + str(winner.name) + " cannot increase his " + str(self.challengesSkills[0]) + " skill past 10.")
                else:
                    winner.skillIncrementValue(self._challengesSkills[0])
                    print(str(winner.name) + " was able to increase his " + self._challengesSkills[0] + " skill by 1 to " + str(winner.getSkill(self._challengesSkills[0])) + ".")

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
    Returns:
        None
    Throws:
        Exception: If you have no requests to accept
    """
    def accept_random(self):
        from CSE216.Homework2.Fight import Fight
        from CSE216.Homework2.KnightErrant import KnightErrant

        if not (self._challenges):
            raise Exception("Cannot accept if there are no challenges to accept.\n")

        randIndex = random.randint(0, len(self._challenges) - 1)

        result = Fight(self, self._challenges[randIndex], self._challengesSkills[randIndex])
        winner = result.winner
        loser = result.loser

        if (winner is self):

            # If a Warrior wins against a KnightErrant
            if isinstance(loser, KnightErrant):

                if (winner.isTravelling == True):
                    raise Exception("A travelling KnightErrant cannot engage in a Fight!")

                print(winner.__class__.__name__ + " " + str(winner.name) + " has decided to randomly accept challenge #" + str(randIndex + 1) + " in his inbox and fight: " + loser.__class__.__name__ + " " + loser.name + ". ")

                winner.wealth += 20
                print(str(winner.name) + " has won the fight and increased his wealth by 20 to " + str(winner.wealth) + ".")

                if (loser.wealth < 20):
                    loser.wealth = 0
                    print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 20
                    print(str(loser.name) + " has lost the fight and decreased his wealth by 20 to " + str(loser.wealth))

                if (winner.getSkill(self._challengesSkills[randIndex]) == 10):
                    print("Despite winning " + str(winner.name) + " cannot increase his " + str(self.challengesSkills[randIndex]) + " skill past 10.")
                else:
                    winner.skillIncrementValue(self._challengesSkills[randIndex])
                    print(str(winner.name) + " was able to increase his " + self._challengesSkills[randIndex] + " skill by 1 to " + str(winner.getSkill(self._challengesSkills[randIndex])) + ".")


            # If a Warrior wins against a Warrior
            elif (isinstance(loser, Warrior)):

                print(winner.__class__.__name__ + " " + str(winner.name) + " has decided to randomly accept challenge #" + str(randIndex + 1) + " in his inbox and fight: " + loser.__class__.__name__ + " " + str(loser.name) + ". ")

                winner.wealth += 10
                print(str(winner.name) + " Has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " Has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " Has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                self.luckUpdateRandom(winner, loser, randIndex)


            # If a Warrior wins against a Fighter
            elif (isinstance(loser, Fighter)):

                print(winner.__class__.__name__ + " " + str(winner.name) + " has decided to randomly accept challenge #" + str(randIndex + 1) + " in his inbox and fight: " + loser.__class__.__name__ + " " + str(loser.name) + ". ")

                winner.wealth += 10
                print(str(winner.name) + " Has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " Has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " Has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                self.luckUpdateRandom(winner, loser, randIndex)



        elif (loser is self):

            # If a KnightErrant Wins against a Warrior
            if isinstance(winner, KnightErrant):

                if (winner.isTravelling == True):
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

                self.luckUpdateRandom(loser, winner, randIndex)

            # If a Warrior wins against a Warrior
            elif (isinstance(winner, Warrior)):

                print(loser.__class__.__name__ + " " + str(loser.name) + " has decided to randomly accept challenge #" + str(randIndex + 1) + " in his inbox and fight: " + winner.__class__.__name__ + " " + str(winner.name) + ". ")

                winner.wealth += 10
                print(str(winner.name) + " has won the fight and increased his wealth by 10 to " + str(winner.wealth) + ".")

                if (loser.wealth < 10):
                    loser.wealth = 0
                    print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 10
                    print(str(loser.name) + " has lost the fight and decreased his wealth by 10 to " + str(loser.wealth))

                self.luckUpdateRandom(loser, winner, randIndex)

            # If a Fighter wins against a Warrior
            elif (isinstance(winner, Fighter)):

                print(loser.__class__.__name__ + " " + str(loser.name) + " has decided to randomly accept challenge #" + str(randIndex + 1) + " in his inbox and fight: " + winner.__class__.__name__ + " " + str(winner.name) + ". ")

                winner.wealth += 25
                print(str(winner.name) + " has won the fight and increased his wealth by 25 to " + str(winner.wealth) + ".")

                if (loser.wealth < 25):
                    loser.wealth = 0
                    print(str(loser.name) + " has lost the fight. His wealth is now " + str(loser.wealth) + ".")
                else:
                    loser.wealth -= 25
                    print(str(loser.name) + " has lost the fight and decreased his wealth by 25 to " + str(loser.wealth))

                if (winner.getSkill(self._challengesSkills[randIndex]) == 10):
                    print("Despite winning, " + str(winner.name) + " cannot increase his " + str(self.challengesSkills[randIndex]) + " skill past 10.")
                else:
                    winner.skillIncrementValue(self._challengesSkills[randIndex])
                    print(str(winner.name) + " was able to increase his " + self._challengesSkills[randIndex] + " skill by 1 to " + str(winner.getSkill(self._challengesSkills[randIndex])) + ".")

        # Removing the request from the inbox
        self._challenges.pop(randIndex)
        self._challengesSkills.pop(randIndex)

    """
    Parameters:
        None
    Preconditons:
        -You have been issued a challenge
    Postconditions
        -You decline the first challenge request in your inbox and pop that request from the lists
    Returns:
        None
    Throws:
        Exception: If you have no requests to decline
    """
    def decline_first(self):

        if not (self._challenges):
            raise Exception("Cannot decline if there are no challenges to decline.\n")

        print("Declining first challenge in " + str(self.name) + "'s inbox.")
        self._challenges.pop(0)
        self._challengesSkills.pop(0)
        return

    """
    Parameters:
        None
    Preconditons:
        -You have been issued a challenge
    Postconditions
        -You decline a random challenge request in your inbox and pop that request from the lists
    Returns:
        None
    Throws:
        Exception: If you have no requests to decline
    """
    def decline_random(self):

        if not self._challenges:
            raise Exception("Cannot decline if there are no challenges to decline.")

        indexToDelete = random.randint(0, len(self._challenges) - 1)

        print("Declining Challenge #" + str(indexToDelete + 1) + " in " + str(self.name) + "'s inbox.\n")
        self._challenges.pop(indexToDelete)
        self._challengesSkills.pop(indexToDelete)

    # This is a helper function used to print all of the challenges in a person's inbox
    def printChallenges(self):

        print(str(self.name) + "'s inbox: ")
        # Printing all challenges in inbox
        i = 1
        for x in range(len(self._challenges)):
            print("Challenge #" + str(i) + ":  Name: " + str(self._challenges[x].name) + ", skill: " + self._challengesSkills[x])
            i += 1