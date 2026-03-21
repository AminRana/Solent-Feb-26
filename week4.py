"""# Program to determine the ASCII code of a character
print("Program Started!")

# Ask the user to enter a character
letter = input("Please enter a letter: ")

# Check the length of the input using len()
if len(letter) == 1:
    # Get ASCII code using ord()
    ascii_value = ord(letter)
    print("The ASCII code for", letter, "is:", ascii_value)

else:
    print("Error: Please enter only a single character.")

print("Program Ended!")
# Program to determine the ASCII character represented by an ASCII code
print("Program Started!")
code = input("Please enter an ASCII code: ")
code = abs(int(code))
if code in range(32, 127):
    character = chr(code)
    print("The character represented by the ASCII code", code, "is", character)
else:
    print("Error: ASCII code must be between 32 and 126.")
print("Program Ended!")

def greet_user():
 print("Please enter your name")
name = input()
print("Hello", name)
greet_user()

# This program demonstrates the use of a user-defined function.
def listen():
    sound = input("What sound did you hear?\n")
    print("\nThat was a loud " + sound + "!")
listen()
listen()
listen()

# Function: escape_by
def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")

# Function that simulates crossing a bridge
def cross_bridge(distance):
    for step in range(distance):
        print("Crossed step.")
    if distance > 5:
        print("The bridge is collapsing!")
    else:#
        print("We must keep going!")
cross_bridge(3)
cross_bridge(6)

#Funcion to simulate climbing a ladder
def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        print("still some way to go")
    else:
        print(" we are almost there")
        climb_ladder(5,2)
        climb_ladder(2,5)
        climb_ladder(10,7)


def display_box(name):
    message = f"* Hello {name} *"
    print("*" * len(message))
    print(message)
    print("*" * len(message))


def greet_user():
    print("Please enter your name")
    name = input()
    display_box(name)
greet_user()

def display_ladder(steps):
    for i in range(steps):
        print("| |")
        print("***")
    print("| |")
def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)
create_ladder()


# Function to calculate the total weight
def sum_weights(person_weight, inventory_weight):
    total = person_weight + inventory_weight
    return total
def calc_avg_weight(person_weight, inventory_weight):
    total = sum_weights(person_weight, inventory_weight)
    average = total / 2
    return average
person_weight = 70
inventory_weight = 15
total = sum_weights(person_weight, inventory_weight)
print("The sum of weights is:", total)
average = calc_avg_weight(person_weight, inventory_weight)
print("The average weight is:", average)


# Function 1: Display word in a box
def display_box(word):
    print("*" * (len(word) + 4))
    print("* " + word + " *")
    print("*" * (len(word) + 4))
def display_lower(word):
    print(word.lower())
def display_upper(word):
    print(word.upper())
def display_mirror(word):
    print(word + " | " + word[::-1])
def repeat_word(word):
    times = int(input("How many times do you want to repeat the word? "))
    for i in range(times):
        if i % 2 == 0:
            print(word.lower())
        else:
            print(word.upper())
def run():
    word = input("Enter a word: ")
    print("\nChoose an option:")
    print("1) Display in a Box")
    print("2) Display Lower-case")
    print("3) Display Upper-case")
    print("4) Display Mirrored")
    print("5) Repeat")
    choice = input("Enter option number: ")
    if choice == "1":
        display_box(word)
    elif choice == "2":
        display_lower(word)
    elif choice == "3":
        display_upper(word)
    elif choice == "4":
        display_mirror(word)
    elif choice == "5":
        repeat_word(word)
    else:
        print("Invalid option.")
run()"""










