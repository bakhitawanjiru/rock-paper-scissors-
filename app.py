import random

def play_game(rounds):
    user_score = 0
    computer_score = 0
    majority = (rounds // 2) + 1 

    for round in range(1, rounds + 1):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        user_choice = input(f"\nRound {round} - Enter your choice (rock, paper, scissors): ").lower()
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("Round tied!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Current Score - You: {user_score}, Computer: {computer_score}")

        
        if user_score == majority:
            print("\n=== Game Over ===")
            print("Congratulations! You win the game!")
            return
        elif computer_score == majority:
            print("\n=== Game Over ===")
            print("Computer wins the game!")
            return

   
    print("\n=== Game Over ===")
    if user_score > computer_score:
        print("Congratulations! You win the game!")
    elif computer_score > user_score:
        print("Computer wins the game!")
    else:
        print("It's a tie!")

def main():
    while True:
        rounds = int(input("Enter the number of rounds (3 or 5): "))
        if rounds not in [3, 5]:
            print("Invalid input. Please choose 3 or 5 rounds.")
            continue

        play_game(rounds)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()