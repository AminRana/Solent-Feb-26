#1 Basic if statement
x = 3
y = 10

if x < y:
    print("x is smaller than y.")

#2 Slightly more complex example
#You can also write this in a single line x,y,z =3,10,none
x= 3
x= 10
z= None

z= 13
print(f"variable z is now {z}")

#3 what happens here?
x = 3
y =10

if x > y:
         print ("x is greater than y.")

#4 else statement
x = 3
y =-10

if x >y:
    print ("x is greater than y>")
else:
    print ("x is smaller than y.")


#5 What if the condition is met?
    x = 3
    y =10

    if x < y:
        print ("xi is smaller than y.")
    else:
        print ("x is greater than y.")

# x is equal to y
x = 3
y = 3

if x < y:
    print ("x is smaller than y.")
else:
    print ("x is greater than y.")


#6 x is equal to y with elif statement
x = 3
y = 3

if x < y:
        print ("x is smaller to y.")
elif x == y:
        print ("x is equal to y.")
else:
    print("x is greater than y.")

    # 7 elif condition
    tomorrow = "warm"

    if tomorrow == "worm":
        print("I'll go to the forest")
    elif tomorrow == "very hot":
        print("I'll go the the porest")
    else:
        print("I'll stay at home")

        # 8 tomorrow is very hot
        tomorrow = "very hot"

        if tomorrow == "warm":
            print("I'll go to the sea.")
        elif tomorrow == "very hot":
            print("I'll go to the forest.")
        else:
            print("I'll stay at home")

            # 9 Several elif conditions
            tomorrow = "snowy"

        if tomorrow == "warm":
            print("I'll go to the sea.")
        elif tomorrow == "very hot":
            print("I'll go to the forest.")
        elif tomorrow == "snowy":
            print("I'll build a snowman.")
        elif tomorrow == "rainy":
            print("I'll stay at home.")
        else:
            print("Weather not recognized.")

            





























