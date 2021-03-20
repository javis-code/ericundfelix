from Question import Question


question_prompts = [
    "Welche Farbe haben Äpfel?\n(a) Rot/Grün\n(b) Lila\n(c) Orange\n\n",
    "Welche Farbe haben Bananen?\n(a) Gelb\n(b) rosa\n(c) blau\n\n",
    "Welche Farbe hat der Regenbogen NICHT?\n(a) blau\n(b) braun\n(c) gelb\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Du hast " + str(score) + "/" + str(len(questions)) + " richtig")


run_test(questions)
