from random import choice

# Rock Paper Scissors

def game(game_point):
    users_score = 0
    computers_score = 0
    
    while users_score < game_point and computers_score < game_point:
        users_choice = input("Enter rock(r), paper(p), or scissors(s): ").lower()
        if users_choice not in ['r', 'p', 's']:
            print("Invalid choice, please try again.")
            continue
        
        computers_choice = choice(['r', 'p', 's'])
        if users_choice == computers_choice:
            print(f"Computer has chosen {computers_choice}. It's a draw!")
        elif winner(users_choice, computers_choice) == "computer":
            print(f"Computer has chosen {computers_choice}. Computer wins!")
            computers_score += 1
        else:
            print(f"Computer has chosen {computers_choice}. You win!")
            users_score += 1

    if users_score > computers_score:
        print("You have won the game!")
    else:
        print("Computer has won the game!")

def winner(user, computer):
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        return "user"
    elif (user == 's' and computer == 'r') or (user == 'r' and computer == 'p') or (user == 'p' and computer == 's'):
        return "computer"
    else:
        return "draw"

game(1)
