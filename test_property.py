# isto não é meu
from rich import inspect


class Celsius:

    # Defining init method with its parameter
    def __init__(self, temp=0):
        self._temperature = temp

    # @property decorator
    @property
    # Getter method
    def temp(self):
        # Prints the assigned temperature value
        print("The value of the temperature is: ")
        return self._temperature

    # Setter method
    @temp.setter
    def temp(self, val):
        # If temperature is less than -273 than a value
        # error is thrown
        if val < -273:
            raise ValueError("It is a value error.")

        # Prints this if the value of the temperature is set
        print("The value of the temperature is set.")
        self._temperature = val


# Creating object for the stated class
cel = Celsius(-300)
cel.temp = -300
inspect(cel, private=True, methods=True)
# Setting the temperature value


# Prints the temperature that is set


# Setting the temperature value to -300
# which is not possible so, an error is
# thrown
