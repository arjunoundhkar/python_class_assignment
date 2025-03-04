import random

def dice_game():
    """Simulates a dice game between player and computer."""
    player_score = 0
    computer_score = 0
    for _ in range(3):  # Play 3 rounds
        player_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)
        print(f"Player rolled: {player_roll}, Computer rolled: {computer_roll}")
        if player_roll > computer_roll:
            player_score += 1
            print("Player wins this round!")
        elif computer_roll > player_roll:
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")
    print(f"Final scores: Player {player_score}, Computer {computer_score}")
    if player_score > computer_score:
        print("Player wins the game!")
    elif computer_score > player_score:
        print("Computer wins the game!")
    else:
        print("It's a tie game!")

dice_game()