import random
import time


def main():   # this def allows a loop without a looping statemeant, see line 35.

    yeslist = ['yes', 'y', 'yeah', 'Y', 'YES']

    answer = random.randrange(1, 10)

    print("Your Range is between 1 and 10!")

    guess = (input("Please enter your guess!:"))
    if not guess.isdigit():
        print("Use a number for this!")
        main()
    else:
        if guess.isdigit():

            if int(guess) == answer:
                print("You got it!")
                restart = input("Try your luck again by typing 'yes'\n ~~>")
                if restart in yeslist:
                    main()
                else:
                    print("Thank you for playing the guessing game!  Closing this app in 10 seconds.")
                    time.sleep(10)
                    exit()

            elif int(guess) < answer:
                restart = input("Your guess is a lil bit too low, try again?\n~~>")
                if restart in yeslist:
                    main()
                else:
                    print("Thank you for playing the guessing game!  Closing this app in 10 seconds.")
                    time.sleep(10)
                    exit()

            elif int(guess) > answer:
                restart = input("Your guess is a lil bit too high, try again?\n~~>")
                if restart in yeslist:
                    main()
                else:
                    print("Thank you for playing the guessing game!  Closing this app in 10 seconds.")
                    time.sleep(10)
                    exit()

main()    # runs the script / toggles inital loop/
