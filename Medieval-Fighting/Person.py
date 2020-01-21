
class Person:

    def __init__(self, name = None, age = 0, wealth = 0):
        self.name = name
        self.age = age
        self.wealth = wealth

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):

        if (value == None):
            pass

        elif not (isinstance(value, str)):
            raise Exception("Name must be a String.")

        self._name = value


    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):

        if not (isinstance(value, (int, float, complex))):
            raise Exception("Age must be a number.")

        elif (value < 0):
            raise Exception("Age cannot be a negative number.")

        elif (value > 0) and (value < 18):
            self._age = value
            self._adult = False
            return

        self._adult = False
        self._age = value


    @property
    def wealth(self) -> int:
        return self._wealth

    @wealth.setter
    def wealth(self, value: int):

        if not (isinstance(value, (int, float, complex))):
            raise Exception("Wealth must be a positive number.")

        elif (value < 0):
            raise Exception("Wealth cannot be negative.")

        self._wealth = value

    @property
    def adult(self) -> bool:
        return self._adult

    # Compares name and age between two people, and if they are the same then they are equal
    def __eq__(self, other: "Person"):
        if (self.name is other.name) and (self.age is other.age): #and (self.wealth is other.wealth):
            return True

    def __str__(self):
        return "Name: " + str(self.name) + ", Age: " + str(self.age) + ", Wealth: " + str(self.wealth)











