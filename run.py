"""
Section containing imports
"""
from questions import get_questions_dict


def welcome():
    """
    Welcome to the QuizMaster Game
    """
    print("--------------------------------------------------")
    print("+                                                +")
    print("+          Welcome to QuizMaster                 +")
    print("+                                                +")
    print("--------------------------------------------------")


def play_quiz(q_and_a):
    """
    Iterates through quiz questions with answers
    """
    score = 0
    for question_dict in q_and_a:
        player_answer = ''
        print("--------------------------------------------------")
        while player_answer not in ['a', 'b', 'c']:
            print(f"{question_dict['question']}")

            for key, value in question_dict['answers'].items():
                print(f"\t{key}: {value}")

            player_answer = input("Enter a, b, or c:\n")
            player_answer = player_answer.lower()

            while player_answer not in ['a', 'b', 'c']:
                player_answer = input("Please enter a, b or c only:\n").lower()

        if player_answer == question_dict['correct_answer']:
            print("Correct\n")
            score += 1
            print(f"Your score is {score}")
        else:
            print("Incorrect\n")
            print(f"Your score is {score}")
    total_score(score, len(q_and_a))


def total_score(score, num_questions):
    """
    Provide the player with their total score results out of the total
    number of questions asked.
    """
    if score <= 5:
        print("--------------------------------------------------")
        print("Better luck next time.")
        print(f"You have scored {score} out of {num_questions}.")
        print("--------------------------------------------------")
    elif score <= 15:
        print("---------------------------------------------------")
        print("Great answers. ")
        print(f"you have scored {score} out of {num_questions}.")
        print("---------------------------------------------------")
    elif score > 15:
        print("---------------------------------------------------")
        print("Congratulations Quizmaster!")
        print(f"you have scored {score} out of {num_questions}.")
        print("---------------------------------------------------")


def play_again():
    """
    Ask player if they would like to play again
    """
    response = input("Would you like to play again? (y/n):\n").lower()
    while response != "y" and response != "n":
        response = input("Please enter y or n only:\n").lower()
    if response == "y":
        return True
    else:
        return False


def main():
    """
    Main area to run functions
    """
    welcome()

    play_quiz(get_questions_dict())

    while play_again():
        play_quiz(get_questions_dict())
    print("Thank you for playing, come back soon!")


if __name__ == '__main__':
    main()
