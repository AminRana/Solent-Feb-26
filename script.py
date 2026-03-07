"""
# Basic if statement
x = 3
y = 10
if x<y:
    print("x is smaller than y.")
    # A slightly more complex example
    x=3
    y=10
    z=0
    if x<y:
        z=13
        print(f"variable z is now {z}.")
        # what happens here ?
        x=3
        y=10
        if x>y:
            print("x is greater than y.")
            # else statement
            x=3
            y=10
            if x>y:
                print("x is greater than y.")
            else:
                print("x is smaller than y.")
                #what if the condition is met ?
                x=3
                y=10
                if x<y:
                    print("x is smaller than y.")
                else:
                    print("x is greater than y.")
                    # x is = y
                    x=3
                    y=3
                    if x<y:
                        print("x is smaller than y.")
                    else:
                        print("x is greater than y.")
                    # x is = y
                    x=3
                    y=3
                    if x<y:
                        print("x is smaller than y.")
                    else:
                        print("x is greater than y.")"""

# x is equal to y with elif statement
x = 3
y = 3

if x < y:
    print("x is smaller than y.")
elif x == y:
    print("x is equal to y.")
else:
    print("x is greater than y.")
# elif condition
tomorrow = "warm"
if tomorrow == "warm"
    print("I will go to the sea")