# guessing a number game:
# choosing a random number between 1 to 100:
# make a function to set difficulty:
# lets the user's guess the number:
# function to gets user's guess number against the answer:
# track the number of turns if the user's get it wrong and reduced by -1:
# repeate the guessing number functionality if they get it wrong:


from random import randint
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5
# function to check user guess against user answer:
def check_answer(guess,answer,turns):
    """ check answer against guess. returns the number of turns remaining """
    if guess > answer:
        print("too high")
        return turns-1
    elif guess < answer:
        print("too low")
        return turns-1
    else:
        print(f"Congratulation ! you got it, your answer was {answer}")

# make function for difficulty:
def set_difficulty():
    level = input("choose the level of difficulty: type 'easy' or 'hard:'")
    if level == "easy":
        global turns
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN

def game():
    print("Welcome to the number guessing game:")
    print("Ranjeet is thinking a number in between 1 to 100")
    # choosing a random number from 1 to 100
    answer = randint(1,100)
    #print(f"passt the correct answer is {answer}")
    turns = set_difficulty()

# repeate the functionality if they guess it wrong:
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempt to the remaining the guess number")
        # lets the user guess the number
        guess = int(input("make a guess: "))

        # track the numbers of turns and reduced  it -1 if they get it wrong.
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print(f"you have run out of guess , you loose, actually the answer was {answer}")
            return
        elif guess != answer:
            print("guess again:")
game()