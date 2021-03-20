Antwort = input("Ihre Antwort hier: ")

blau = ["blau"]
gelb = ["gelb"]
rot = ["Rot"]
grün = ["Grün"]

if Antwort.lower().strip() in blau:
    print("Nein, Blau ist falsch! Niemand mag dich")
elif Antwort.lower().strip() in gelb:
    print("Gelb ist Richtig....-Geheime Bodschaft-")
elif Antwort.lower().strip() in grün:
    print("Grün ist falsch du Fisch")
elif Antwort.lower().strip() in rot:
    print("Rot ist falsch du Schwanznase")
else: 
    print("Falsch")