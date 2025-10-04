import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

number_of_picks = input("How many quick picks? ")
number_of_picks = int(number_of_picks)
print("How many quick picks?", number_of_picks)
if number_of_picks < 0:
    print("Sorry, but you don't have enough numbers to pick")
    number_of_picks = input("How many quick do you picks? ")

for i in range(number_of_picks):
    quick_number = []
    for j in range(NUMBERS_PER_LINE):
       quick_number_of_picks = random.randint(MINIMUM, MAXIMUM)
       quick_number.append(quick_number_of_picks)
       quick_number.sort()
    print(" ".join(f"{number:2}" for number in quick_number))