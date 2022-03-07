questions = {
    "Who sang the title song for the latest Bond film, No Time to Die?: ": "c",
    "What Italian city is famous for its system of canals?: ": "c"
}

answer_choice = [
    ["a. Adele", "b. Sam Smith", "c. Billie Eilish"],
    ["a. Rome", "b. Naples", "c. Venice"],
    ]

def new_game():
    """
    Call questions and mutiple choice answers to display to user
    """

    answers = []
    correct_answers = 0
    question_num = 1

    for key in questions:
        print("----------------------------------------------")
        print(key)
        for i in answer_choice[question_num-1]:
            print(i)
        
        answer = input("Enter a, b, or c:\n")
        answer = answer.lower()
        while answer != "a" and answer != "b" and answer != "c":
            answer = input("Please enter a, b or c only:\n").lower()
        answers.append(answer)

        correct_answers += check_answer(questions.get(key), answer)
        question_num += 1
        print(f"Your score is {correct_answers}")

def check_answer(player_answer, answer):
    """
    Check player's answer against correct answer
    """
    if player_answer == answer:
        print("\nCorrect!")
        return 1
    else:
        print("\nIncorrect!")
        return 0

def display_score(correct_answers):
    """
    Display score total to player
    """
    #print(f"Your score is {correct_answers}")

def play_again():
    """
    Ask player if they would like to play again
    """
    response = input("Would you like to play again? (y/n):\n")
    response = response.lower()
    while response != "y" and response != "n":
        response = input("Please enter y or n only:\n").lower()

    if response == "y":
        return True
    else:
        return False

new_game()

while play_again():
    new_game()

print("Thank you for playing, come back again soon!")