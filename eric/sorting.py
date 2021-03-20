def bubble_sort(list):
    swapped = True

    while swapped: 
        swapped = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i +1], list[i]
                swapped = True

ia = True

coole_liste = []

while ia: 
    user_input = input("Deine Zahl (e für exit): ")

    if user_input == "e":
        ia = False 
        break

    try:
        coole_liste.append(int(user_input))
    except:
        print("Ungültige Eingabe")
                

bubble_sort(coole_liste)


print (coole_liste)