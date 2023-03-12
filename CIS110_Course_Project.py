#Introduction
from time import sleep
print(f"Good Morning!")
sleep(1)
print(f"\nIt's 6am and you are a cat waking up in your bed at the top of your cat tree. Tell me a little about yourself.")
sleep(2)
print(f"After typing your answer, be sure to press the enter key.")
input(f"\nPress the enter key to continue...")

startOver = "yes"
while startOver.lower() == "yes":

    #Variables
    fur = input("\nWhat color is your fur?:  ")
    while len(fur) == 0:
        fur = input(f"Please type the color of your fur:  ")
    food = input("\nWhat is your favorite type of food?:  ")
    while len(food) == 0:
        food = input(f"Please type your favorite type of food:  ")
    toy = input("\nWhat is your favorite toy?:  ")
    while len(toy) == 0:
        toy = input(f"Please type your favorite toy:  ")
    fear = input("\nWhat are you most afraid of?:  ")
    while len(fear) == 0:
        fear = input(f"Please type what you are most afraid of:  ")
    while True:
        try:
            sibling = int(input("\nHow many other cats do you live with?:  "))
            break
        except ValueError:
            print("A numerical number of cats please...")
            continue
    if sibling == 1:
        print(f"\nYes you live with one other cat named Taquita.")
    else:
        print(f"\nYou only live with 1 other cat and her name is Taquita.")

    name = input("\nAnd last but definetly not least, what is your name?:  ")
    while len(name) == 0:
        name = input(f"Please type your name:  ")


    #Story Begins
    print(f"\nGood morning {fur} cat named {name}.")
    print(f"\nIt is time to start the day, as long as the day is ready for you.")
    sleep(2)

    #Filler - Written before I understood the assignment. 
    stayAsleep = "dark"
    time = int(6)
    while stayAsleep.lower() == "dark":

        print(f"\nYou open your eyes and it is {time} in the morning.")
        sleep(2)
        stayAsleep = input("\nYou look outside to see if it is light out or dark?:  ")
        while stayAsleep.lower() not in ["dark", "light" ]:
            stayAsleep = input("Is it light outside or dark?:  ")
        if time <= 8:
            time = time+1
        else:
            print(f"\nYou give up on today, maybe tomorrow will be better.")
            time = int(6)

    #Decision 1
    print(f"\nFinally out of bed! Hope you didn't dream about {fear}.")
    print(f"Now {name} you have have to choose if you would like to go downstairs for food or wait for it to come to you.")
    findFood = input(f"Do you go downstairs? Type yes or no:  ")
    while findFood.lower() not in ["yes", "no"]:
        findFood = input("Do you go downstairs? Type yes or no:  ")
    if findFood == "yes":
        print(f"\nYou head downstairs and find your sister Taquita and the humans that feed you.")
        print(f"You meow a few times and are given a bowl filled with {food}.")
        print(f"What a way to start the day!")
    else:
        print(f"\n You decide to wait for food and why not, the world does revolve around you.")
        print(f"After some time you human brings you a bowl of dry kibble.")
        print(f"It isn't your favorite, but it will do.")

    #Decision 2
    print(f"\nNow that you have a full stomach the fun starts!")
    print(f"Do you want to play with {toy} or is it time for you to take a nap?")
    play = input(f"\nDo you play with your {toy}? Type yes or no:  ")
    while play.lower() not in ["yes", "no"]:
        play = input("Do you want to play with {toy} or is it time for you to take a nap? Type yes or no:  ")
    if play == "yes":
        print(f"\nYou find your {toy} and play with it.")
        print(f"Your sister Taquita joins you and you both have a blast.")
    else:
        print(f"\nYou find a secluded place to take a nap")
        print(f"It is dark and hidden away where no one will bother you.")

    print(f"Time flies and the day is almost over!")
    
    #Project Endings
    if findFood == "yes" and play == "yes":
        print(f"\nAfter eating {food} and playing with {toy} it has been a crazy day.")
        print(f"You were social and adventurus.")
        print(f"You curl up to get some sleep on the couch with Taquita and your humans.")
    elif findFood == "no" and play == "no":
        print(f"\nYou spent the day by yourself as the independent {fur} cat that you are.")
        print("You are indepentent and find your spot at the top of your tower to sleep until tomorrow.")
    else:
        print(f"\nAnother normal day and about as average as it can be.")
        print("You find a spot at the foot of the bed to fall asleep.")

    startOver = input(f"\nWould you like to start another day? Type yes or no:  ")
    while startOver.lower() != "yes" and startOver.lower() != "no":
        startOver = input(f"Please type yes or no:  ")
