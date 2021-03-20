from Question import Question
import cryptocompare


name = input("Wie heißt du? ")

print("Hallo " + name + "!")

print("Wie geht es dir " + name + "?")

gefühl = input()

gut = ["gut", "schön", "super"]
schlecht = ["scheiße", "schlecht", "nicht gut"]

if gefühl.lower() in gut:
    print("Das ist ja schön")

elif gefühl.lower() in schlecht:
    print("Oh man :(")

else:
    print("Bruh")


print("Und was machst du heute so? ")

tätigkeit = input()

print("Oh cool, meine Aufgabe ist es dir zu antworten, den ganzen Tag... ")


print("Zum Beispiel kann ich Zahlen für dich sortieren. Gib einfach ein paar ein. Drücke -e um deine Zahlen zu sortieren ")


def bubble_sort(list):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True


ia = True

coole_liste = []

while ia:
    user_input = input("Deine Zahl: ")

    if user_input == "e":
        ia = False
        break

    try:
        coole_liste.append(int(user_input))
    except:
        print("Ungültige Eingabe")


bubble_sort(coole_liste)


print(coole_liste)


print("Cool, oder? Ich kann dir aber auch den Bitcoinpreis anzeigen lassen und Zahlen für dich Faktorisieren. Was soll ich für dich machen?  ")
print("Gebe entweder ´Bitcoin´ oder ´Faktorisieren´ ein. ")


def factorial(n):
    if n == 1:
        return 1

    else:
        return n * factorial(n-1)


bitcoin = str(cryptocompare.get_price("BTC"))

bitcoin = bitcoin.replace("{'BTC': {'EUR': ", "")
bitcoin = bitcoin.replace("}}", "")


wassollichtun = input()


if wassollichtun.lower() == "faktorisieren":
    print("Okay warte... ")
    user_input = int(input("Deine Zahl: "))
    print(factorial(user_input))


if wassollichtun.lower() == "bitcoin":
    print("Moment... ")

    print(bitcoin + " EUR")


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

if str(score) == "3":
    print("Das hast du sehr gut gemacht!")
elif str(score) == "2":
    print("Du bist schon ganz solide!")
elif str(score) == "1":
    print("Es ist inordnung.")
else:
    print("Du hast komplett verkackt und wirst dich auf dieser Welt wahrscheinlich gar nicht zurechtfinden. Dein Wisse ist so schlecht wie ein 5-jähriger abgelaufener Joghurt")
