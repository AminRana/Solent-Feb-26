# Activity 1
"""
fruits=["apple", "banana", "cherry"]
fruits.append("orange")
fruits.append("dragon fruit")
print(fruits)
"""


"""
#Task 1
def directions():
    steps=["Move Forward", "Move Backward", "Turn Left","Turn Right"]
    return steps
def run_task1():
    maze_steps=directions()
    print(maze_steps)
if __name__ == "__main__":
    run_task1()

"""
"""
#Activity 2
fruits = ["apple", 5, "banana", 10, "cherry", 15]
print(fruits[2])
"""

#Task
"""
fruits=["apple", "banana", "cherry"]
fruits.append("orange")
fruits.append("dragon fruit")
print(fruits)
fruits[0:2]=["mango", "grape"]
print(fruits)
fruits.insert(0,"Melon")
print(fruits)
"""

"""
"""
"""

"""
"""


"""

#Task
"""def movements():
    path=["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run_task2():
    print('Moving ...')
    directions_list=movements()
    for i in range (0, len(directions_list), 2):
        direction=directions_list[i]
        steps=directions_list[i+1]
        print(f" {direction} for {steps} steps")
if __name__ == '__main__':
    run_task2()
"""

"""#Activity 3
thislist = ["apple", "banana", "cherry"]
for y in thislist:
  print(y)
"""

"""
#Task
def directions():
    steps=["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps

def menu():
    print("Please enter your direction")
    steps_list=directions()
    for index,direction in enumerate(steps_list):
        print(f"{index}: {direction}")

def run_task3():
    menu()

if __name__ == '__main__':
    run_task3()


"""
#Activity 4
def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps
if __name__ == "__main__":
    my_steps=directions()
    print(my_steps)


#Tuple
