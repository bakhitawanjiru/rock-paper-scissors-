import random
computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
print (f"Computer chose: {computer_choice}")
user_score = 0
computer_score = 0

if user_choice == computer_choice:
        print("Tied!")

elif user_choice == 'rock' and computer_choice == 'scissors':
        print(f"You get a point! {user_score}" )
        user_score+=1
elif user_choice == 'paper' and computer_choice == 'rock':
        print(f"You get a point! {user_score}")
        user_score+=1
   
elif user_choice == 'scissors' and computer_choice =='paper':
        print(f"You get a point! user {user_score}" )
        user_score+=1
else:
    print(f"Computer wins!{computer_score}")
    computer_score+=1
print(f"Score - You: {user_score}, Computer: {computer_score}")
print("\n=== Game Over ===")
if user_score > computer_score:
        print("Congratulations! You win!")
elif computer_score > user_score:
        print("Computer wins!")
else:
        print("It's a tie!")
while True:
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
    

    
