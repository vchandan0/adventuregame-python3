import time
import turtle
import random


def print_sleep(x):
    print(x)
    time.sleep(2)


def print_sleep5(x):
    print(x)
    time.sleep(5)


def intro():
    print_sleep("Hello Hello!\n\n")
    print_sleep("You and your family are on a family vacation"
                " for 14 days to The United Kingdom.\n\n")
    print_sleep("You have reached the airport for departures.\n\n")
    print_sleep("You have got 6 and a half hours"
                " in-hand to make it through customs,"
                " security, check-in and bag drop."
                "\n\nReaching 6 and half hours prior to"
                " the flight definitely says something about your"
                " personality :P\n\n"
                "That is a lot of time to kill now before"
                " you onboard your flight.")

    print("----------------------------------------------------")


def option_1():
    print("For the four of you, the entry price to the lounge is $450.")
    price_confirm = input(
        "Please press 1 to continue and 2 to choose another option.")
    if price_confirm == "1":
        credit_card_number = input(
            "Please enter your 16 digits credit card number.")
    elif price_confirm == "2":
        print("Hey, no worries! Select something else")
        all_options_together()
    else:
        print("It was either 1 or 2. Please try again.")


def option_2():
    shop_confirm = input("Which shop would you like to go to?\n"
                         "1. Zara\n"
                         "2. H&M\n"
                         "3. Mango\n"
                         "4. Forever 21\n")

    print("Great Choice, Use coupon code:ZSERGTYH"
          " to avail flat 50% off")


def option_3():
    print_sleep("Great")
    print_sleep(
        "Head to floor 3 and drop your children"
        " first as things can get pretty hot")
    print_sleep("Now head to floor 7 and enter the spa named as Sukha Thai")
    print_sleep("Welcome to Sukha Thai, you are"
                " about to experience one of the finest"
                " couple Spa sessions ever.")
    print("Before we begin the session, you"
          " and your partner need to undress and"
          " wear the given bathrobe please.")
    spa_choice = input("After the spa session,"
                       " would you like to spend some intimate"
                       " time with your partner?"
                       "(As the massuesses will be instructed accordingly)"
                       "\nYes or No\n")
    if spa_choice == "yes":
        massuesses_choice = input("Would you like the massuesses"
                                  " to join you and your partner"
                                  " with your intimate session?\n")
        if "yes" == massuesses_choice:
            print("All set! Things are about to get wild."
                  "Get in your bathrobe and"
                  " wait until called please")
        else:
            print("No worries! You can enjoy your intimate"
                  " session just the two of you"
                  "... Happy Spa!")
    else:
        print("We understand and respect your decision!"
              " Please get in your bathrobe and wait"
              " until called for your Couple Spa Session.")


def option_4():
    print_sleep("Ounce of prevention is worth a pound of cure\n\n")
    print("Great Choice\n\n")
    print("To keep you entertained, we have a game"
          "for you and your family:\n\n")
    x = random.randint(1, 20)
    while True:
        num = input(
            "Pick a number between 1 to 20"
            " and see if you guessed it right.")
        if x == int(num):
            print("Wohooo! You won.")
            break
        elif x > int(num):
            print("Your guess is too small. Please try again.")
        elif x < int(num):
            print("Your guess is too big. Please try again.")


def all_options_together():
    kt_choice = input("So what would you like to do"
                      " from the following:\n\n"
                      "1. Vist the signature lounge and chill.\n\n"
                      "2. Go shopping.\n\n"
                      "3. Drop your kids in the playzone"
                      " while you along with your partner go for"
                      " a sizzling couple spa session.\n\n"
                      "4. Do nothing. Simply finish the security,"
                      "customs, check-in, and"
                      " go sit next to the boarding gate.\n\n")
    if kt_choice == "1":
        option_1()

    elif kt_choice == "2":
        option_2()

    elif kt_choice == "3":
        option_3()

    elif kt_choice == "4":
        option_4()

    else:
        print_sleep("Please select from the options below only.")
        all_options_together()


def win_loose():
    if kt_choice == "3" or "4":
        time.sleep(6)
        print_sleep5("Btw don't get too excited, this whole game"
                     " was just a facade.")
        print_sleep5("This game was actually testing your personality traits"
                     " to see whether if you are going"
                     " to be a succesfull"
                     " person or not.")
        print_sleep5("You have won! Congratulations. Your"
                     " decisons clearly depecit your life choices."
                     " You are definitely"
                     " going to be a succesfull one.")
    elif kt_choice == "1" or "2":
        print_sleep5("Btw don't get too excited, this whole game"
                     " was just a facade.")
        print_sleep5("This game was actually testing your personality traits"
                     " to see whether if you are going to be a succesfull"
                     " person or not.")
        print_sleep5("You have depicted decisions that resemble your traits"
                     " and some of which need to be improved!"
                     " However, based on your traits it is clear"
                     " that you are definitely going to be succesfull in life"
                     " but just that you will need to do some real hard work"
                     " before you shine.")


def game_again():
    ga = input("Woulld you like to play the game again? Y/N\n")
    if ga == "Y".lower():
        intro()
        all_options_together()
    elif ga == "N".lower():
        exit()


def trait_tester():
    intro()
    while True:
        time.sleep(5)

        all_options_together()
        win_loose()
        game_again()
# Start
# Start


trait_tester()
