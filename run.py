from questions import q_and_a


def count_question(q_and_a):
    """
    Counts the number of questions in the quiz. It will be used to provide a
    final score to the player of their results
    """
    q_count = 0
    for i in enumerate(q_and_a):
        q_count += 1
    return q_count


num_questions = (count_question(q_and_a))


def play_quiz(q_and_a):
    """
    Iterates through quiz
    """
    score = 0
    for q in q_and_a:
        player_answer = ''
        print("--------------------------------------------------")      
        while player_answer not in ['a', 'b', 'c']:
            print(f"{q['question']}")

            for key, value in q['answers'].items():
                print(f"\t{key}: {value}")

            player_answer = input("Enter a, b, or c:\n")
            player_answer = player_answer.lower()

            while player_answer != "a" and player_answer != "b" and player_answer != "c":
                player_answer = input("Please enter a, b or c only:\n").lower()

        if player_answer == q['correct_answer']:
            print("Correct\n")
            score += 1
            print(f"Your score is {score}")
        else:
            print("Incorrect\n")
            print(f"Your score is {score}")
    
    total_score(score)


def total_score(score):
    """
    Provide the player with their total score results out of the total
    number of questions asked.
    """
    if score <= 5:
        print("--------------------------------------------------")
        print(f"Better luck next time. You have scored {score} out "
            "of {num_questions}.")
        print("--------------------------------------------------")
    elif score <= 15:
        print("---------------------------------------------------")
        print(f"Great answers, you have scored {score} out "
            "of {num_questions}.")
        print("---------------------------------------------------")
    elif score > 15:
        print("---------------------------------------------------")
        print(f"Congratulations Quizmaster!, you have "
            "scored {score} out of {num_questions}.")
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


play_quiz(q_and_a)

while play_again():
    play_quiz(q_and_a)
print("Thank you for playing, come back soon!")
