print("Welche Farbe haben Bananen?")
List_1 = ["Blau", "Gelb", "Grün", "Rot"]
for item in List_1:
    print(item)
Antwort = input("Ihre Antwort hier: ")

if Antwort.lower().strip() == "blau":
    print("Nein, Blau ist falsch! Niemand mag dich")
elif Antwort.lower().strip() == "gelb":
    print("Gelb ist Richtig")
elif Antwort.lower().strip() == "grün":
    print("Grün ist falsch du Fisch")
elif Antwort.lower().strip() == "rot":
    print("Rot ist falsch du Schwanznase")
else:
    print("DU BIST DER HÄSSLICHSTE MENSCH DEN ICH JE GESEHEN HABE!!!!!!!!")
