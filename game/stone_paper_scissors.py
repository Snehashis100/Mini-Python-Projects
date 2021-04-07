def game(bot, user):
    user = user.lower()
    if (user == "rock" and bot == "scissor") or (user == "scissor" and bot == "papper") or (
            user == "paper" and bot == "rock"):
        return "user"
    elif (bot == "rock" and bot == "rock") or (user == "scissor" and bot == "scissor") or (
            user == "paper" and bot == "paper"):
        return "draw"
    else:
        return "bot"


if __name__ == '__main__':
    import random

    lst = ['rock', 'paper', 'scissor']
    print("10 rounds game...win the most rounds to win the game")
    print("Welcome to the Rock-Paper_Scissor game")
    i = 10
    computer, user = 0, 0
    while i != 0:
        comp = random.choice(lst)
        user_input = input("Enter your move...")
        status = game(comp, user_input)
        if status == "user":
            print("Win")
            print(f"The computer's move was {comp}")
            user += 1
            print(f"Current score--->COMP::{computer}  YOU::{user}")
            i -= 1
        elif status == "bot":
            print("Loss")
            print(f"The computer move was {comp}")
            computer += 1
            print(f"Current Score--->COMP::{computer}  YOU::{user}")
            i -= 1
        else:
            print("Draw")
            print("The computer's move was also the same")
            i -= 1
    if user > computer:
        print("Congratulations You won the game!!!")
    elif user < computer:
        print("Oops!!You lost")
    else:
        print("No Result")
