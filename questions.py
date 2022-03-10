"""
Import random to randomise questions with answers to player
"""
import random


__ques_dict__ = [
    {"question": "Who sang the title song for the latest Bond film, "
        "No Time to Die?: ",
     "answers": {"a": "Adele", "b": "Sam Smith", "c": "Billie Eilish"},
     "correct_answer": "c"},
    {"question": "What Italian city is famous for its system of canals?: ",
     "answers": {"a": "Rome", "b": "Naples", "c": "Venice"},
     "correct_answer": "c"},
    {"question": "What company makes the Xperia model of smartphone?: ",
     "answers": {"a": "Samsung", "b": "Sony", "c": "Nokia"},
     "correct_answer": "b"},
    {"question": "Which city is home to the Brandenburg Gate?: ",
     "answers": {"a": "Vienna", "b": "Zurich", "c": "Berlin"},
     "correct_answer": "c"},
    {"question": "Which of the following is NOT a fruit?: ",
     "answers": {"a": "Rhubarb", "b": "Tomatoes", "c": "Avocados"},
     "correct_answer": "a"},
    {"question": "Where was the first example of paper money used?: ",
     "answers": {"a": "China", "b": "Turkey", "c": "Greece"},
     "correct_answer": "a"},
    {"question": "Who is generally considered the inventor of the "
        "motor car?: ",
     "answers": {"a": "Henry Ford", "b": "Karl Benz", "c": "Henry M. Leland"},
     "correct_answer": "b"},
    {"question": "If you were looking at Iguazu Falls, on what continent "
        "would you be?: ",
     "answers": {"a": "Asia", "b": "Africa", "c": "South America"},
     "correct_answer": "c"},
    {"question": "What number was the Apollo mission that successfully put a "
        "man on the moon for the first time in human history?: ",
     "answers": {"a": "Apollo 11", "b": "Apollo 12", "c": "Apollo 13"},
     "correct_answer": "a"},
    {"question": "Which of the following languages has the longest "
        "alphabet?: ",
     "answers": {"a": "Greek", "b": "Russian", "c": "Arabic"},
     "correct_answer": "b"},
    {"question": "Who was the lead singer of the band The Who?: ",
     "answers": {"a": "Roger Daltrey", "b": "Don Henley", "c": "Robert Plant"},
     "correct_answer": "a"},
    {"question": "What spirit is used in making a Tom Collins?: ",
     "answers": {"a": "Vodka", "b": "Rum", "c": "Gin"},
     "correct_answer": "c"},
    {"question": "Where was the earliest documented case of Spanish flu?: ",
     "answers": {"a": "USA", "b": "Spain", "c": "Mexico"},
     "correct_answer": "a"},
    {"question": "Where was tea invented?: ",
     "answers": {"a": "England", "b": "USA", "c": "China"},
     "correct_answer": "c"},
    {"question": "Which horoscope sign is a fish?: ",
     "answers": {"a": "Aquarius", "b": "Cancer", "c": "Pisces"},
     "correct_answer": "c"},
    {"question": "What is the largest US state (by landmass)?: ",
     "answers": {"a": "Texas", "b": "Alaska", "c": "California"},
     "correct_answer": "b"},
    {"question": "Which app has the most total users?: ",
     "answers": {"a": "TikTok", "b": "Snapchat", "c": "Instagram"},
     "correct_answer": "c"},
    {"question": "Which Game of Thrones character is known as the "
        "Young Wolf: ",
     "answers": {"a": "Robb Stark", "b": "Arya Stark", "c": "Sansa Stark"},
     "correct_answer": "a"},
    {"question": "What city hosted the 2002 Olympic Games?: ",
     "answers": {"a": "Tokyo", "b": "Beijing", "c": "Sydney"},
     "correct_answer": "c"},
    {"question": "How many plays do people (generally) believe that "
        "Shakespeare wrote?: ",
     "answers": {"a": "27", "b": "37", "c": "47"},
     "correct_answer": "b"},
]


def get_questions_dict():
    """
    Create a shuffle of questions with answers before importing to quiz
    """
    random.shuffle(__ques_dict__)
    return __ques_dict__
