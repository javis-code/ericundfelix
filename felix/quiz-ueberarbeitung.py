a = 0
q_count = 0

##########Frage 1##########

while True:
    q_count += 1

    print(" ")
    print("Frage 1")
    print(" ")

    print("Welche Farbe haben Bananen?")
    List_1 = ["(A) Blau", "(B) Grün", "(C) Gelb", "(D) Rot"]
    for item in List_1:
        print(item)
    Antwort = input("Ihre Antwort hier (A, B, C oder D): ")

    if Antwort.lower().strip() == "a":
        a += 0
        break
    elif Antwort.lower().strip() == "b":
        a += 0
        break
    elif Antwort.lower().strip() == "c":
        a += 1
        break
    elif Antwort.lower().strip() == "d":
        a += 0
        break
    else:
        print("")
        print("Bitte überprüfen sie Ihre eingabe und versuchen es nochmal!")

##########Frage 2##########

while True:
    q_count += 1

    print(" ")
    print("Frage 2")
    print(" ")

    print("Wie heiß ist die Sonnenoberfläche?")
    List_2 = ["(A) 1.600°C", "(B) 6.000°C", "(C) 24.000°C", "(D) 100.000°C"]
    for item in List_2:
        print(item)
    Antwort_2 = input("Ihre Antwort hier (A, B, C oder D): ")

    if Antwort_2.lower().strip() == "a":
        a += 0
        break
    elif Antwort_2.lower().strip() == "b":
        a += 1
        break
    elif Antwort_2.lower().strip() == "c":
        a += 0
        break
    elif Antwort_2.lower().strip() == "d":
        a += 0
        break
    else:
        print("")
        print("Bitte überprüfen sie Ihre eingabe und versuchen es nochmal!")

##########Frage 3##########

while True:
    q_count += 1

    print(" ")
    print("Frage 3")
    print(" ")

    print("Wie hoch ist der Mount Everest?")
    List_3 = ["(A) 8849 Meter", "(B) 8953 Meter",
              "(C) 8603 Meter", "(D) 7973 Meter"]
    for item in List_3:
        print(item)
    Antwort_3 = input("Ihre Antwort hier (A, B, C oder D): ")

    if Antwort_3.lower().strip() == "a":
        a += 1
        break
    elif Antwort_3.lower().strip() == "b":
        a += 0
        break
    elif Antwort_3.lower().strip() == "c":
        a += 0
        break
    elif Antwort_3.lower().strip() == "d":
        a += 0
        break
    else:
        print("")
        print("Bitte überprüfen sie Ihre eingabe und versuchen es nochmal!")

##########Frage 4##########

while True:
    q_count += 1

    print(" ")
    print("Frage 4")
    print(" ")

    print("Wie viele Kubikkilometer Wasser sind im Pazifik?(Gerundet")
    List_4 = ["(A) 600 Millionen km³", "(B) 700 Millionen km³",
              "(C) 800 Millionen km³", "(D) 900 Millionen km³"]
    for item in List_4:
        print(item)
    Antwort_4 = input("Ihre Antwort hier (A, B, C oder D): ")

    if Antwort_4.lower().strip() == "a":
        a += 0
        break
    elif Antwort_4.lower().strip() == "b":
        a += 1
        break
    elif Antwort_4.lower().strip() == "c":
        a += 0
        break
    elif Antwort_4.lower().strip() == "d":
        a += 0
        break
    else:
        print("")
        print("Bitte überprüfen sie Ihre eingabe und versuchen es nochmal!")

##########Ergebnis##########

print(" ")
print("Ihr Ergebnis")
print(" ")

print("Du hast {} von {} Fragen richtig beantwortet".format(a, q_count))
