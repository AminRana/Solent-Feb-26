# Ask the user how many bars should be charged
total_bars = int(input("How many bars should be charged? "))

# Create a variable to track charged bars
charged = 0

# Use a while loop
while charged < total_bars:
    print("Charging:")

    # Increment the number of charged bars
    charged += 1

    # Display the current number of charged bars
    print(charged)

# Final message
print("The battery is fully charged.")