# while_loops.py
# This program simulates a robot removing apples from a box
# Ask the user how many apples should be removed
apples_to_remove = int(input("How many apples should I remove?\n"))
# Create a variable to track the number of removed apples
removed_apples = 0
# Use a while loop to remove apples until the target is reached
while removed_apples < apples_to_remove:
    # Display message showing an apple has been removed
    print("Removed apple.")
    removed_apples += 1