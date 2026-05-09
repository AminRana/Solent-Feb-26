class Human:
    # Class attribute (Constant for all humans)
    MAX_ENERGY = 100

    def __init__(self, name="Human"):
        """
        Initializer to set up a new Human instance.
        """
        # Instance attributes
        self.name = name
        self.age = 0
        # Accessing class attribute using the class name
        self.energy = Human.MAX_ENERGY

    def display(self):
        """
        Instance method to display the human's name.
        """
        print(f"I am {self.name}")

# Testing the class
if __name__ == "__main__":
    human = Human()
    human.display()
