"""import os
path=os.getcwd()
print(f"The path of the file is {path}")
for file in os.listdir(path):
    print(file)

import os
def cwd():
    path = os.getcwd()
    print(f" the current working directory is {path}")
    print("The directory contains the following files:")
    files = os.listdir(path)
    for file in files:
        print(file)
        def run():
            print("Processing...")
            cwd()
            if __name__ == "__main__":
                run()

                def display_chars(file_path, num_chars):
    with open(file_path) as file:
        print(f"The first {num_chars} characters are:")
        print(file.read(num_chars))
        print()


def display_line(file_path):
    with open(file_path) as file:
        print("The first line is:")
        print(file.readline().strip())
        print()


def display_text(file_path):
    with open(file_path) as file:
        print("The full text is:")
        print(file.read())


def run_task2():
    file_path = "library.txt"  # works because file is in same folder
    display_chars(file_path, 5)
    display_line(file_path)
    display_text(file_path)


if __name__ == "__main__":
    run_task2()

# Function to search through the file line by line
def search(file_name):
    print("Searching...")
    with open(file_name) as file:
        for line in file:
            location = line.strip()
            print(f"Looked in {location}.")
    print("...Done!")
    file.close()# Function to search through the file line by line
def search(file_name):
    print("Searching...")
    with open(file_name) as file:
        for line in file:
            location = line.strip()
            print(f"Looked in {location}.")
    print("...Done!")# Function to search through the file line by line
"""

# Function to search through the books file
def search_books(file_path):
    # Display searching message
    print("Searching...", end="")
    sections = ""
    books = "Books:\n"
    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line.startswith("Section"):
                sections += line + "\n"
            else:
                books += line + "\n"
    print("Done!")
    return sections + "\n\n" + books
def save(file_path, data):
    print("Saving...", end="")
    with open(file_path, "w") as file:
        file.write(data)
    print("Done!")
def run_task4():
    data = search_books("books.txt")
    save("section-books.txt", data)
if __name__ == "__main__":
    run_task4()
    

