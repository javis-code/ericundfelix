def linear_search(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return i
    return -1

eingabe_erlaubt = True

coole_liste = []

while eingabe_erlaubt:
    user_input = input("Objekte: (e für exit): ")

    if user_input == "e":
        eingabe_erlaubt = False
        break
    
    try:
        coole_liste.append(user_input)
    except:
        print("Invalide Eingabe!")

element = input("Das Element: ")

print(linear_search(coole_liste, element))