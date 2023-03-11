#Introduction
from time import sleep
print(f"Good Morning!")
sleep(1)
print(f"\nIt's 6am and you are a cat waking up in your bed at the top of your cat tree. Tell me a little about yourself.")
sleep(2)


#Variables
fur = input("\nWhat color is your fur?:  ")
food = input("\nWhat is your favorite type of food?:  ")
toy = input("\nWhat is your favorite toy?:  ")
fear = input("\nWhat are you most afraid of?:  ")
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


print(f"\nGood morning {fur} cat named {name}.")
print(f"\nIt is time to start the day, as long as the day is ready for you.")
sleep(2)

#Decision 1
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

#
