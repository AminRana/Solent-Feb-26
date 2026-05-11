class Robot:
    # Class attributes
    laws = "Protect, Obey and Survive"
    MAX_ENERGY = 100

    @staticmethod
    def the_laws():
        """
        Static method: Does not access instance (self) or class (cls).
        It simply prints the shared laws.
        """
        print(Robot.laws)

    @classmethod
    def assemble(cls):
        """
        Class method: Receives the class (cls) as a parameter.
        Used to create and return a new instance of Robot.
        """
        return cls("Assembled Robot")

    def __init__(self, name="Robot"):
        """
        Special instance method to initialize instance attributes.
        """
        self.name = name
        self.age = 0
        self.energy = 0  # Starting energy for robots as requested

    def display(self):
        """
        Instance method: Accesses the specific name of this robot.
        """
        print(f"I am {self.name}")


# Testing the class
if __name__ == "__main__":
    robot = Robot()
    robot.display()

    # Testing the static method
    Robot.the_laws()
