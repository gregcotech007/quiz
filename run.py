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


new_game()