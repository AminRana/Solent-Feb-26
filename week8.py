
"""
import matplotlib.pyplot as plt

labels = ('A', 'B', 'C', 'D')
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels)
plt.show()


import matplotlib.pyplot as plt
x = [0,2,4,6,8,10]
y = [10,20,40,60,80,100]
plt.xlabel("No of Years in Job Exp")
plt.ylabel("Salary in £K")
plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt
x = [0,2,4,6,8,10]
y = [10,20,40,60,80,100]
plt.xlabel("No of Years in Job Exp")
plt.ylabel("Salary in £K")
plt.plot(x, y, "o")
plt.show()


import matplotlib.pyplot as plt
x = [0, 5, 10]
y = [0, 50, 100]
plt.plot(x, y)
plt.show()


import matplotlib.pyplot as plt


# Function to display a line plot using provided X and Y coordinates
def display_line(x_values, y_values):
    # Create the line plot
    plt.plot(x_values, y_values)

    # Add optional labels to make the graph readable
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('Basic Line Graph')

    # Display the plot window
    plt.show()


# Function to initialize data and call the plotting function
def run_task1():
    # Create the list of x values (independent variable)
    x_values = [1, 2, 3, 4, 5]

    # Create the list of y values (dependent variable - these are x squared)
    y_values = [1, 4, 9, 16, 25]

    # Call the display function with the data
    display_line(x_values, y_values)


# Standard entry point
if __name__ == "__main__":
    run_task1()

"""
import matplotlib.pyplot as plt


# Function to display a small square
def small():
    # Defining coordinates for a 1x1 square
    x = [0, 1, 1, 0, 0]
    y = [0, 0, 1, 1, 0]

    # Customization:
    # color='red', linestyle='dotted', marker='o' (circle)
    plt.plot(x, y, color='red', linestyle='dotted', marker='o', label='Small')


# Function to display a medium square
def medium():
    # Defining coordinates for a 3x3 square (centered around the small one)
    x = [-1, 2, 2, -1, -1]
    y = [-1, -1, 2, 2, -1]

    # Customization:
    # color='green', linestyle='dashed', marker='s' (square)
    plt.plot(x, y, color='green', linestyle='dashed', marker='s', label='Medium')


# Function to display a large square
def large():
    # Defining coordinates for a 5x5 square (centered around the other two)
    x = [-2, 3, 3, -2, -2]
    y = [-2, -2, 3, 3, -2]

    # Customization:
    # color='blue', linestyle='solid', marker='p' (pentagon)
    plt.plot(x, y, color='blue', linestyle='solid', marker='p', label='Large')


# Main function to coordinate the tasks
def run_task2():
    # Call each function; they will all add to the same plot
    small()
    medium()
    large()

    # Ensuring the x and y axes have the same scale so squares look like squares
    plt.axis('equal')

    # Optional: adds labels and a title for clarity
    plt.title('Customized Nested Squares')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    # Optional: displays a legend based on labels defined in plot commands
    plt.legend()

    # Display the final combined plot
    plt.show()


# Standard entry point to execute the script
if __name__ == "__main__":
    run_task2()

