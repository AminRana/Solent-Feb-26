"""
#1 Basic if statement
x = 3
y = 10

if x < y:
    print("x is smaller than y.")


#2 A slightly more complex example
# you can also write this in single line x,y,z =3,10,None
x = 3
y = 10
z = None

if x < y:
    z = 13
print(f"Variable z is now {z}.")


#3 What happens here?
x = 3
y = 10

if x > y:
    print("x is greater than y.")

#4 else statement
x = 3
y = 10

if x > y:
    print("x is greater than y.")
else:
    print("x is smaller than y.")


#5 What if the condition is met?
x = 3
y = 10

if x < y:
    print("x is smaller than y.")
else:
    print("x is greater than y.")

#5 x is equal to y
x = 3
y = 3

if x < y:
    print("x is smaller than y.")
else:
    print("x is greater than y.")


#6 x is equal to y with elif statement
x = 3
y = 3

if x < y:
    print("x is smaller than y.")
elif x == y:
    print("x is equal to y.")
else:
    print("x is greater than y.")


#7 elif condition
tomorrow = "warm"

if tomorrow == "warm":
    print("I'll go to the sea.")
elif tomorrow == "very hot":
    print("I'll go to the forest.")
else:
    print("I'll stay home.")


#8 Tomorrow is very hot
tomorrow = "very hot"

if tomorrow == "warm":
    print("I'll go to the sea.")
elif tomorrow == "very hot":
    print("I'll go to the forest.")
else:
    print("I'll stay home.")


#9 Several elif conditions
tomorrow = "snowy"

if tomorrow == "warm":
    print("I'll go to the sea.")
elif tomorrow == "very hot":
    print("I'll go to the forest.")
elif tomorrow == "snowy":
    print("I'll build a snowman.")
elif tomorrow == "rainy":
    print("I'll stay home.")
else:
    print("Weather not recognized.")


#10 Biome prediction with and logical operator
humidity = "low"
temperature = "high"

if humidity == "low" and temperature == "high":
    print("It's a hot desert.")
elif humidity == "low" and temperature == "low":
    print("It's an arctic desert.")
elif humidity == "high" and temperature == "high":
    print("It's a tropical forest.")
else:
    print("I don't know!")

#11 or logical operator
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nums_less_3_greater_equal_10 = []

for num in nums:
    if num < 3 or num >= 10:
        nums_less_3_greater_equal_10.append(num)

print(nums_less_3_greater_equal_10)


#12 Change or to and
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nums_less_3_greater_equal_10 = []

for num in nums:
    if num < 3 and num >= 10:
        nums_less_3_greater_equal_10.append(num)

print(nums_less_3_greater_equal_10)

#13 More complex logical statements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nums_less_3_greater_equal_10_multiple_2 = []

for num in nums:
    if (num < 3 or num >= 10) and num % 2 == 0:
        nums_less_3_greater_equal_10_multiple_2.append(num)

print(nums_less_3_greater_equal_10_multiple_2)

#14 More complex logical statements without parentheses
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nums_less_3_greater_equal_10_multiple_2 = []

for num in nums:
    if num < 3 or num >= 10 and num % 2 == 0:
        nums_less_3_greater_equal_10_multiple_2.append(num)

print(nums_less_3_greater_equal_10_multiple_2)


#15 Nested if statements
mark =  85

if mark >= 60 and mark <= 100:
    if mark >= 90:
        print("You are the best!")
    elif mark >= 80:
        print("Well done!")
    elif mark >= 70:
        print("You can do better.")
    else:
        print("Pass.")
elif mark > 100:
    print("This mark is too high.")
elif mark < 0:
    print("This mark is too low.")
else:
    print("Failed.")


#16 Pattern matching with match..case syntax
tomorrow = "snowy"

match tomorrow:
    case "warm":
        print("I'll go to the sea.")
    case "very hot":
        print("I'll go to the forest.")
    case "snowy":
        print("I'll build a snowman.")
    case "rainy":
         print("I'll stay home.")
    case _:
        print("Weather not recognized.")

#17 Without pass
num = 3
if num == 3:
    print("I'll write this code later.")
"""

#18 With pass
num = 3
if num == 3:
    pass

print("I'll write this code later.")

#19 With pass
num = 4
if num == 3:
    pass
elif num == 4:
    print("The variable num is 4.")
else:
    print("The variable num is neither 3 nor 4.")
    