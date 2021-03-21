a = 0

##########Frage 1##########

print("Welche Farbe haben Bananen?")
List_1 = ["Blau", "Grün", "Gelb", "Rot"]
for item in List_1:
    print(item)
Antwort = input("Ihre Antwort hier: ")

if Antwort.lower().strip() == "blau":
    a+=0
elif Antwort.lower().strip() == "gelb":
    a+=1
elif Antwort.lower().strip() == "grün":
    a+=0
elif Antwort.lower().strip() == "rot":
    a+=0
else:
    print("Bitte überprüfen sie Ihre eingabe!")

##########Frage 2##########

print("Wie heiß ist die Sonnenoberfläche?")
List_2 = ["1600°C","6000°C","24000°C","100000°C"]
for item in List_2:
    print(item)
Antwort_2 = input("Ihre Antwort hier (Nur in Zahlen angeben zB 1000): ")

if Antwort_2.lower().strip() == "1600":
    a+=0
elif Antwort_2.lower().strip() == "6000":
    a+=1
elif Antwort_2.lower().strip() == "24000":
    a+=0
elif Antwort_2.lower().strip() == "100000":
    a+=0
else:
    print("Bitte überprüfen sie Ihre eingabe!")

##########Frage 3##########

print("Wie hoch ist der Mount Everest?")
List_3 = ["8849 Meter","8953 Meter","8603 Meter","7973 Meter"]
for item in List_3:
    print(item)
Antwort_3 = input("Ihre Antwort hier (Nur in Zahlen angeben zB 1000): ")

if Antwort_3.lower().strip() == "8849":
    a+=1
elif Antwort_3.lower().strip() == "8953":
    a+=0
elif Antwort_3.lower().strip() == "8603":
    a+=0
elif Antwort_3.lower().strip() == "7973":
    a+=0
else:
    print("Bitte überprüfen sie Ihre eingabe!")

##########Frage 4##########

print("")
##########Ergebnis##########

if a > 1:
    print("Glückwunsch! Sie haben 2 von 2 Fragen richtig beantwortet!")
elif 2 > a > 0  :
    print("Fürs erste nicht schlecht. Sie haben 1 von 2 Fragen richtig beantwortet!")
elif a < 1:
    print("Sie haben 0 von 2 Fragen richtig beantwortet. Probieren sie es doch nochmal!")
else:
    print("Ups... Es ist ein Fehler aufgetreten!")