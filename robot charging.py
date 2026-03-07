battery = int(input("How many bars should be charged\n"))

bars = 0

while battery > bars:

    bars = bars + 1

    print("Charging:" + "\u2588" * bars)

print ("\nThe battery is fully charged!")