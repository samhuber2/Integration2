# Sam Huber
# Basic 4 Function calculator
#Help from POGIL 2/3/6/7/8/9

print("4 function calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
choice = int(input("Enter your choice: "))
if 1 <= choice <= 4:
    print("Enter two numbers: ")
    num1 = int(input())
    num2 = int(input())
    if choice == 1:
        res = num1 + num2
        print("Result = ", res)
    elif choice == 2:
        res = num1 - num2
        print("Result = ", res)
    elif choice == 3:
        res = num1 * num2
        print("Result = ", res)
    else:
        res = num1 / num2
        print("Result = ", res)
elif choice == 5:
    exit()
else:
    print("Wrong input..!!")

    # Trivia Game
    # Help from Pogil 1/2/3/6/13
question1 = "Who is the Bengals starting quarterback? "
question2 = "What country won the very first World Cup? "
question3 = "Is Java a type of OS? "
question4 = "What was twitter's original name? "
question5 = "Who was the leading rusher of the AFC in 2018? "
question6 = "Where is the first ever Slicers located?"
question7 = "What is Lil Uzi Vert's biggest hit? "
question8 = "Did Ohio State beat Alabama in the 2014 Playoffs? "

# This is the list questions

questions = [question1, question2, question3, question4, question5, question6,
             question7, question8]

# ANSWERS
# here are all variables of the answers.
#Help from Pogil 2

answer1 = "Andy Dalton"
answer2 = "Uruguay"
answer3 = "No"
answer4 = "twttr"
answer5 = "Joe Mixon"
answer6 = "Naples, Florida"
answer7 = "XO Tour Life"
answer8 = "Yes"

# this is the list answers

answers = [answer1, answer2, answer3, answer4, answer5, answer6, answer7,
           answer8]

# GLOBAL GAME SETTINGS
# Help from Hackerrank

points = 0
name = None
yes = ['Yes', 'yes', 'YES']
no = ['No', 'no', 'NO']


# RESET ZONE
# Help from Hackerrank 


def game_reset():
    """
    Reset all variables of the whole game for a new play
    """

    global points
    global name

    points = 0
    name = None


# end-function#


# GAME INTRO ZONE


def game_intro():
    """
    Welcome the player and ask him for his name as long as he thinks is 
    correct. 
    """

    print("\n       ------ !! Welcome to the QuizGame !! ------\n")

    global name

    while name is None:
        name = input("What's your name? ")
        print("Your name is", name)
        correct = input("Is that correct? ")
        if yes.count(correct):
            print("Good, let's go on!\n")
        else:
            print("Mh? Try again and confirm with Yes!")
            name = None


# end-function#


# GAME PLAY ZONE 


def print_play_status(x):
    """
    just print out the current score and the current challenge number.
    """

    global points
    print("At the moment your total points are", points)
    print("Challenge", x + 1, "\n")


# end-function#


def play_quest(x):
    """int -> int this functions asks the player question X, checks if 
    player's answer is right and eventually changes the variable points. no 
    examples needed 
    """

    global points
    answer_Player = input(questions[x])
    if answer_Player == answers[x]:
        print("Well done,",
              name + ", 10 points gained! Let's move to the next question.\n")
        points += 10
    else:
        print("Wrong! 0 points gained, the correct answer was:", answers[x],
              ". Next question...\n")


# end-function#


def game_play():
    """
    first : tell the player his current score and the current challenge 
    number second: tell the play_quest-function how many and which questions 
    it must asks the player. 
    """

    for x in range(len(questions)):
        print_play_status(x)
        play_quest(x)


# end-function#


# GAME END ZONE 


def game_end():
    print(' ')


# GAME CONTROL ZONE


def game_control():
    """
    Control the whole game with the single steps.
    """
    game_reset()
    game_intro()
    game_play()
    game_end()


# end-function#


game_control()
