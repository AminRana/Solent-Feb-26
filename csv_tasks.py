
# activity 1, task 2
"""
import csv


# The first function named read_csv
def read_csv(file_path):
    # Open the specified file for reading
    # Using 'with' ensures the file is closed automatically
    with open(file_path, mode="r", encoding="utf-8") as file:
        # Create a csv reader object
        csv_reader = csv.reader(file)

        # Read the first line as headings using next()
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")

        print("Values:")

        # For each line remaining in the file, display the values
        for row in csv_reader:
            print(row)


# The second function named run_task1
def run_task1():
    # Call the read_csv function (mapped to 'read' in the logic)
    # and pass the filename as the argument
    read_csv("clothing.csv")


# Execute run_task1 when the file is run directly
if __name__ == "__main__":
    run_task1()
"""

#activity 2, task 1
"""
import csv


# Function to extract only the 'name' column from the CSV
def extract(file_path):
    print("Extracting...", end="")

    # Open the specified file for reading
    with open(file_path, mode="r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)

        # Read in and ignore the headings
        next(csv_reader)

        # Create a variable named names set to an empty string
        names = ""

        # Process each remaining line in the file
        for row in csv_reader:
            # The 'name' is the second item in the list (index 1)
            item_name = row[1]
            # Add the extracted name with a new line character
            names += item_name + "\n"

    print("Done!")
    print("The extracted items are as follows:")
    # Display the final accumulated string
    print(names)


# Function to run the extraction task
def run_task2():
    # Call the extract function with the specific file path
    extract("clothing.csv")


# Execute the program
if __name__ == "__main__":
    run_task2()
"""

#Activity 3, task 1

# Function to export (append) a specific number of items to a CSV file
def export(file_path, num_items):
    print("Exporting...")

    # Open the specified file for appending ('a' mode)
    # This adds to the end of the file without overwriting existing data
    file = open(file_path, "a")

    # Loop for the number of items to be exported
    for i in range(num_items):
        # Gather user input for each field
        item_id = input("Please enter the item id:\n")
        item_name = input("Please enter the item name:\n")
        item_colour = input("Please enter the item colour:\n")

        # Write the values to the CSV file in comma-separated format
        # We add \n at the end to ensure the next entry starts on a new line
        file.write(f"{item_id},{item_name},{item_colour}\n")

    # Close the file to save changes
    file.close()
    print("Done!")


# Function to run the program with suitable values
def run():
    # Calling export with the filename and 2 items as shown in the example
    export("exported_items.csv", 2)


# Standard entry point to execute the run function
if __name__ == "__main__":
    run()