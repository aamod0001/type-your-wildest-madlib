from random import randint
 
def main():
    min = int(input("what is the minimum number you want to guess: "))
    max = int(input("ehat is the maximum number you want to guess: "))
    game = input("which game do you want to play h or c")
    if game == "h":
        guess(min, max)
    elif game == "c":
        computer_guess(min, max)

def guess(minimum, maximum):
    random_number = randint(minimum, maximum)
    guess_number = minimum - 1
    while guess_number != random_number:
        guess_number = int(input("input your guessed number: "))
        if guess_number > random_number:
            print("the guessed number is too high")
        elif guess_number < random_number:
            print("your guessed number is too low")
    print("you have successfully guessed the correct number")

def computer_guess(low, high):
    minimum = low
    maximum = high
    feedback = ""
    while feedback != "t":
        guess = randint(minimum , maximum)
        feedback = input(f"is {guess} low high or true: ")
        if feedback == "l":
            minimum = guess + 1
        elif feedback == "h":
            maximum = guess - 1
    print(f"I have guessed the {guess} correctly!!")

