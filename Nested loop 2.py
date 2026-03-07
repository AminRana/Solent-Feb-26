# nesting.py
# Ask the user to enter a sequence
sequence = input("Please enter a sequence\n")
# Ask the user to enter the marker character
marker = input("\nPlease enter the character for the marker\n")
# Variable to count the dashes between markers
distance = 0
# Variable to count how many markers have been found
marker_count = 0
# Go through each character in the sequence
for character in sequence:
    if character == marker:
        marker_count += 1
        # Stop checking once the second marker is found
        if marker_count == 2:
            break
    elif character == "-" and marker_count == 1:
        # Only count dashes after the first marker
        # and before the second marker
        distance += 1
# Display the result
print(f"\nThe distance between the markers is {distance}.")