import random

def roll_dice():
    roll = input("Roll Dice? (Yes/No)")

    while roll.lower() == 'yes':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print(f"Dice rolled: {dice1} and {dice2}")

        roll = input("Roll again? (Yes/No): ")

roll_dice()