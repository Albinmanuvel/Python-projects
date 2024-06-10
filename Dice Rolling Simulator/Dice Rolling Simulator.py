import random

def roll_dice(num_dice, num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls

def play_game():
    num_dice = int(input("Enter the number of dice: "))
    num_sides = int(input("Enter the number of sides per die: "))

    rolls = roll_dice(num_dice, num_sides)
    print(f"You rolled: {', '.join(map(str, rolls))}")
    print(f"Total: {sum(rolls)}")

    play_again = input("Do you want to roll again? (y/n) ").lower()
    if play_again == 'y':
        play_game()

# Start the game
play_game()