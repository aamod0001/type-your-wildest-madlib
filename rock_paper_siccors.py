from random import choice
# rock paper siccors

def game(game_point):
    users_score = 0
    computers_score = 0
    while game_point != users_score or computers_score:
        users_choice = input("enter rock(r) papers(p) or siccors(s): ")
        computers_choice = choice(['r', 'p', 's'])
        if users_choice == computers_choice:
            print(f"computer has chosen {computers_choice} its a draw")
        elif winner(users_choice, computers_choice) == "computer":
            print(f"computer has chosen {computers_choice} , computer won")
            computers_score = computers_score + 1
        else:
            print(f"computer has chosen {computers_choice} , you win")
            users_score = users_score + 1
    if users_score == game_point:
        print("you have won the game")
    else:
        print("computer has won the game")

def winner(user , computer):
    if (user == 'p' and computer == 'r') or (user == 's' and computer == 'p') or (user == 'r' and computer == 's'):
        return "computer"
    elif (user == 'r' and computer == 'p') or (user == 'p' and computer == 's') or (user == 's' and computer == 'r'):
        return "user"

game(1)