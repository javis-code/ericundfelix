#######################################################################
# Variablen
#######################################################################

a = 6  # Integer
b = "Hallo"  # String
c = True´  # Boolean

#######################################################################
# Rechnen
#######################################################################

a += 1  # Erhöht "a" um 1

#######################################################################
# Listen
#######################################################################

liste_eins = ["Micky Maus", "Goofy", "Kater Karlo"]  # Liste aus Strings
liste_zwei = [6, 8, 10, 15, 14, 2, 3]  # Liste aus Integern

liste_zwei.append(5)  # Fügt eine Zahl hinten an die Liste 2 hinzu
liste_zwei.pop()  # entfernt das letzte Item der Liste

#######################################################################
# Output
#######################################################################

print("Hallo Welt")  # einfacher Output
print(b)  # Output einer Variable

#######################################################################
# Input
#######################################################################

name = input("Wie ist dein Name? ")
# Zahlen müssen in den Variablentypen Integer konvertiert werden
zahl = int(input("Eine Zahl bitte: "))

#######################################################################
# Variablen in Strings
#######################################################################

print("Hallo {}".format(name))
print(f"Hallo {name}")

#######################################################################
# Funktionen
#######################################################################


def Square(a):
    return a * a


def Multiply(a, b):
    return a * b


print(Multiply(4, 8))

#######################################################################
# Klassen
#######################################################################


class Mathematik:
    def Square(a):
    return a * a

    def Multiply(a, b):
        return a * b


print(Mathematik.Multiply(6, 18))

#######################################################################
# Verzweigungen
#######################################################################

if 1 > 2:
    print("Eins ist größer als zwei.")
elif 1 < 2:
    print("Eins ist kleiner als zwei.")
else:
    print("Eins und zwei sind gleich groß.")

#######################################################################
# Schleifen
#######################################################################

d = 0

while d < 10:
    print(d)

#######################################################################
# Endlosschleifen
#######################################################################

while True:
    print("Ich bin hier für immer (fast)")
    break  # mit break "brichst" du aus einer schleife aus

# solltest du mal in deiner Endlosschleife gefangen sein, kannst du immer mit STRG + C entkommen

#######################################################################
# Über Listen loopen
#######################################################################

for item in liste_zwei:
    print(item)

# Hier wird jedes Item in der Liste ausgegeben
