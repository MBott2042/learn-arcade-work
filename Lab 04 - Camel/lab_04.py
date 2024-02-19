import random


def menu():
    print("""
    A. Drink from your canteen.
    B. Ahead moderate speed.
    C. Ahead full speed.
    D. Stop for the night.
    E. Status check.
    Q. Quit.
    """)


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    canteen_drinks = 3
    oasis_chance = 0

    done = False
    while not done:
        menu()

        user_choice = input("What is your choice? ").upper()

        if user_choice == 'Q':
            done = True

        elif user_choice == 'A':
            if canteen_drinks > 0:
                thirst = 0
                canteen_drinks = canteen_drinks - 1
                print("\n Oh yeah, nothing like stopping my self from dying of dehydration.\n")
            else:
                print("\nOh no your canteen is empty\n")

        elif user_choice == 'B':
            print(" \nYour camel decides to test out his two leg running style 'p.s it is really slow'.")
            miles_traveled = miles_traveled + random.randrange(5, 12)
            print("you have traveled " + str(miles_traveled) + " miles.")
            camel_tiredness = camel_tiredness + 1
            print("your camel tiredness has gone up by " + str(camel_tiredness))
            oasis_chance = oasis_chance + random.randrange(1, 20)
            thirst = thirst + 1
            print("your thirst has increased to " + str(thirst))
            natives_distance = natives_distance + random.randrange(7, 14)
            print("The natives are " + str(miles_traveled - natives_distance) + " miles behind you.\n")

        elif user_choice == 'C':
            print(" \nYour camel puts his Croc's in sports mode.")
            miles_traveled = miles_traveled + random.randrange(10, 20)
            print("you have traveled " + str(miles_traveled) + " miles.")
            thirst = thirst + 1
            print("your thirst has increased to " + str(thirst))
            camel_tiredness = camel_tiredness + random.randrange(1, 3)
            print("your camel tiredness has gone up by " + str(camel_tiredness))
            oasis_chance = oasis_chance + random.randrange(1, 20)
            natives_distance = natives_distance + random.randrange(7, 14)
            print("The natives are " + str(miles_traveled - natives_distance) + " miles behind you.\n")



        elif user_choice == 'D':
            print(" \nYou have stopped for the night to rest.")
            camel_tiredness = camel_tiredness - camel_tiredness
            print("Your camel is rested and happy.")
            natives_distance = natives_distance + random.randrange(7, 14)
            print("The natives are " + str(miles_traveled - natives_distance) + " miles behind you.\n")

        elif user_choice == 'E':
            print(" \nYou have traveled " + str(miles_traveled) + "miles.")
            print("You have " + str(canteen_drinks) + " drinks left.")
            print("You are at a " + str(thirst) + " on the thirst scale.")
            print("your camel looks to be about a " + str(camel_tiredness) + " on the camel tiredness scale")
            print("The natives are " + str(miles_traveled - natives_distance) + " miles behind you.\n")

        if thirst > 6:
            print("\nYou died of thirst\n")
            done = True
            break

        elif thirst > 4:
            print("\nYou are thirsty!\n")

        elif camel_tiredness > 8:
            print("\n Your camel is talking to hades, and dying!\n")
            done = True
            break

        elif camel_tiredness > 5:
            print("\nYour camel is looking close to death.\n")

        elif natives_distance > miles_traveled:
            print("\nOh no the natives caught up and turned you into a pin cushion!\n")
            done = True
            break
        elif natives_distance > miles_traveled - 15:
            print("That noise in the back ground is your friends the natives I would move it along if i where you!")

        elif miles_traveled > 199:
            print("Congratulations you made it and now you will not be killed for your crimes!")
            done = True
            break

        elif oasis_chance > 20:
            thirst = 0
            canteen_drinks = 3
            oasis_chance = 0
            camel_tiredness = 0
            print(" Wow you found a oasis you can drink from it and refill you canteen.")
        elif oasis_chance < 20:
            oasis_chance = 0

main()
