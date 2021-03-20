print("Welche Farbe haben Bananen?")
List_1 = ["Blau","Gelb","Grün","Rot"]
for item in List_1:
    print(item)
Antwort = input("Ihre Antwort hier: ")

blau = ["blau"]
gelb = ["gelb"]
rot = ["Rot"]
grün = ["Grün"]

if Antwort.lower().strip() in blau:
    print("Nein, Blau ist falsch! Niemand mag dich")
elif Antwort.lower().strip() in gelb:
    print("Gelb ist Richtig")
elif Antwort.lower().strip() in grün:
    print("Grün ist falsch du Fisch")
elif Antwort.lower().strip() in rot:
    print("Rot ist falsch du Schwanznase")
else: 
    print("DU BIST DER HÄSSLICHSTE MENSCH DEN ICH JE GESEHEN HABE!!!!!!!!")