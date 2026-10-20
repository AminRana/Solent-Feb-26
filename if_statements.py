book_type = input("What type of book is this?\n")

# Check if the entered book type matches "adventure"
# Using .lower() ensures it works even if the user types "Adventure" or "ADVENTURE"
if book_type.lower() == "adventure":
    print("I like adventure books!")

# This message prints regardless of what type of book was entered
print("Finished reading book.")