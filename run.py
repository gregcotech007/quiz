questions = {
    "Who sang the title song for the latest Bond film, No Time to Die?: ": "c",
    "What Italian city is famous for its system of canals?: ": "c"
}

answer_choice = [
    ["a. Adele", "c. Sam Smith", "c. Billie Eilish"],
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
        print(key)
        for i in answer_choice[question_num-1]:
            print(i)
        
        answer = input("Enter a, b, or c: ")
        answer = answer.lower()
        answers.append(answer)

new_game()