# Nested loops

# Ask the user for the number of rows
rows = int(input("How many rows should I have?\n"))

# Ask the user for the number of columns
columns = int(input("\nHow many columns should I have?\n"))

print("\nHere I go:\n")

# Outer loop controls the rows
for row in range(rows):
    # Inner loop controls the columns
    for column in range(columns):
        print(":-)", end=" ")
    # Move to the next line after each row is complete
    print()

print("\nDone!")