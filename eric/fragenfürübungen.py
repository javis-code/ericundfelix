from Question import Question
print("Ich habe ein kleines Quiz für dich vorbreitet, schau mal :):")


question_prompts = [
    "Wie schwer ist die Erde ungefähr?\n(a) 4x10^22kg\n(b) 8x10^25kg\n(c) 6x10^24kg\n\n",
    "Welche Farbe hat der Regenbogen NICHT?\n(a) braun\n(b) indigo\n(c) gelb\n\n",
    "Was ist 5x5x5?\n(a) 350\n(b) 125\n(c) 250\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b")
]


def run_test(question):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("Du hast " + str(score) + "/" + str(len(questions)) + " richtig")
    return score


score = run_test(questions)

if str(score) == "2":
    print("Das hast du sher gut gemacht!")
if str(score) == "1":
    print("Du bist schon ganz solide!")
if str(score) == "0":
    print("Du hast komplett verkackt und wirst dich auf dieser Welt wahrscheinlich gar nicht zurechtfinden. Dein Wisse ist so schlecht wie ein 5-jähriger abgelaufener Joghurt")
