"""
import os
path=os.getcwd()
print (f"Current Working Directory: {path}")
for file in os.listdir(path):
    print (file)

"""


"""#Activity1, Task
import os
def cwd():
    path=os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following files:")
    files=os.listdir(path)
    for file in files:
        print (file)

def run():
    print("Processing ...")
    cwd()

if __name__ == "__main__":
    run()
"""
"""
#Activity 2, Task
# Function to display a specific number of characters from a file
def display_chars(file_path, num_chars):
    # Open the specified file for reading ('r' mode)
    file = open(file_path, "r")
    # Read and display the specified number of characters
    content = file.read(num_chars)
    print(f"The first {num_chars} characters are:")
    print(content)
    # Close the file to free up system resources
    file.close()


# Function to display only the first line of a file
def display_line(file_path):
    # Open the specified file for reading
    file = open(file_path, "r")
    # Read the first line using readline()
    line = file.readline().strip()
    print("\nThe first line is:")
    print(line)
    # Close the file
    file.close()


# Function to display the entire content of a file
def display_text(file_path):
    # Open the specified file for reading
    file = open(file_path, "r")
    # Read the full text using read()
    full_text = file.read()
    print("\nThe full text is:")
    print(full_text)
    # Close the file
    file.close()


# Main function to coordinate the tasks
def run_task2():
    # Define the path to the library file
    path = "library.txt"

    # Call the earlier functions with required arguments
    display_chars(path, 5)
    display_line(path)
    display_text(path)


# Execute run_task2 if the script is run directly
if __name__ == "__main__":
    run_task2()
"""
"""

"""
"""
#Activity 3, Task
# Function to search through a file and display its contents
def search(file_name):
    # Display the starting message
    print("Searching...")

    # Open the specified file for reading ('r' mode)
    file = open(file_name, "r")

    # Iterate through each line in the file
    for line in file:
        # Use .strip() to remove the newline character (\n) from the end of the line
        location = line.strip()
        print(f"Looked in {location}")

    # Display the completion message
    print("...Done!")

    # Close the file to ensure system resources are released
    file.close()


# Function to execute the search task
def run_task3():
    # Call the search function with the specific file path
    search("library.txt")


# Standard boilerplate to run the program
if __name__ == "__main__":
    run_task3()

"""
#Activity 4, Task
# Function to categorize content into sections and books
def search_books(file_path):
    print("Searching...", end="")

    sections = ""
    books = "Books:\n"

    # Open the specified file for reading
    file = open(file_path, "r")

    # Iterate through each line in the file
    for line in file:
        # Check if the line starts with the word "Section"
        if line.startswith("Section"):
            # Add line and a newline character to the sections string
            sections += line.strip() + "\n"
        else:
            # Add line and a newline character to the books string
            books += line.strip() + "\n"

    # Close the file
    file.close()
    print("Done!")

    # Return the formatted string with two new lines in between
    return f"{sections}\n\n{books}"


# Function to save data to a specified file path
def save(file_path, data):
    print("Saving...", end="")

    # Open the file for writing ('w' mode will create/overwrite the file)
    file = open(file_path, "w")

    # Write the data string to the file
    file.write(data)

    # Close the file
    file.close()
    print("Done!")


# Main function to coordinate the reading and saving tasks
def run_task4():
    # Call the search function and store the returned string
    data = search_books("books.txt")

    # Pass the processed data to the save function with the new filename
    save("section-books.txt", data)


# Execute the program
if __name__ == "__main__":
    run_task4()