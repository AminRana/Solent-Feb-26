"""#Activity 1
fruits = []
fruits = ["apple", "banana", "cherry"]
fruits.append("dragon fruit")
fruits.remove("dragon fruit")

# list_tasks.py
def directions():

    This function creates a list of movement
    and returns the list.
    steps = []
    steps.append("Move Forward")
    steps.append("Move Backward")
    steps.append("Turn Left")
    steps.append("Turn Right")
    # Return the completed list
    return steps
def run_task1():

    This function calls the directions function
    and displays the list of steps.
    maze_steps = directions()
    print(maze_steps)
if __name__ == "__main__":
    run_task1()
#Activity 2

#Display the firs item i.e. apple
print(fruits[0])
#update the second item i.e. replace banana with berry
fruits[1] = "berry"
#remove the third item i.e removes cherry
del fuits[2]
fruits =["apple",5, "banana",10, "cherry",15]

def movements():
    path=["move forward",10,"Move backword",5,"move left",3,"Move right",1]
    return path
def run_task2():
    print("moving...")
    path_list = movements()

    for i in range(0,len(path_list),2):
        diretion = path_list[i]
        steps = path_list[i+1]
        print(f"{direction}for{steps} steps")
        if__name__=="__main__"
        run_task2()
#Activity 3
def direction():
    steps = ["Move forward", "move backward", "Turn Left", "Turn Right"]
    return steps
def menu():
    print("please enter a direction:")
    steps = direction()
    for index in range(0,len(steps)):
        direction = steps[index]
        print(f"{index}. {direction}")
        def run_task3():
            if__name__=="__main__"


#Activity 4
def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps
def menu_and_input():
    print("\nPlease select a direction:")
    steps = directions()
    for index in range(len(steps)):
        print(f"{index}: {steps[index]}")
    choice = int(input())
    return steps[choice]
def run_task4():
    route = []
    print("Working out escape route...")
    for i in range(5):
        valid = False
        while not valid:
            try:
                direction = menu_and_input()
                route.append(direction)
                valid = True
            except ValueError:
                print("Please enter a number from 0 to 3.")
            except IndexError:
                print("Please select a valid number from 0 to 3.")

    print(f"\nEscape route: {route}")
if __name__ == "__main__":
    run_task4()


# Tuple
temperature = (19, 23, 21, 21, 20, 18, 22)
all_temperatures = temperature + (20,21)
print(all_temperatures)
print(temperature * 2)
print(20 in temperature)
print(f"The lowest temperature is:{min(temperature)}")
print(f"The highest temperature is:{max(temperature)}")

# Function to calculate the minimum likelihood of falling
def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)
def run_task1():
    min_value = likelihood()
    print(f"Minimum likelihood of falling: {min_value}%")
if __name__ == "__main__":
    run_task1()

#Tuple return type

def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    minimum=min(likelihoods)
    maximum=max(likelihoods)
    return minimum,maximum
def run_task2():
    min_val, max_val = likelihood_min_max()

#Nested Tuples

# Function to reate and retur a list of steps likelihood
def steps():
    likelihoods = []
    ("step1",50)
    ("step2",38)
    ("step3",27)
    ("step4",99)
    ("step5",4)
    return likelihoods
def runtask3():
    step_list = steps()
    good_steps = []
    bad_steps = []
    for step in step_list:
        if step[1]>=50:
            good_steps.append(step)
        else:
            bad_steps.append(step)
            print(f"Good step: {step}:{len(good_steps)}")
            print(f"Bad step: {step}:{len(bad_steps)}")
            runtask3()

            """




