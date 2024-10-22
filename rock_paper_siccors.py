from random import choice

# Rock Paper Scissors
# Ruthlessness Max Only one winner
def number():
    x = input("enter odd numeric value for game point: ")
    while x.isnumeric() == False:
        x = input("the entered value is not correct, please enter again: ")
    return x

def check():
    x = int(number())
    while x%2 == 0:
        x = int(number())
    return x

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
        elif winner(users_choice, computers_choice):
            computers_score += 1
            print(f"Computer has chosen {computers_choice}. Computer wins \n Computers score: {computers_score} \n Users score: {users_score}")
        else:
            users_score += 1
            print(f"Computer has chosen {computers_choice}. You win! \n Computers score: {computers_score} \n Users score: {users_score}")

    if users_score > computers_score:
        print("You have won the game!")
    else:
        print("Computer has won the game!")

def winner(user, computer):
    if (user == 's' and computer == 'r') or (user == 'r' and computer == 'p') or (user == 'p' and computer == 's'):
        return True

game(check())
