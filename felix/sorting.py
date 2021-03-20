# bubble sort
# quick sort

# 3, 2, 5, 1, 7, 8 => 6 -1  = 5

def bubble_sort(list):
    swapped = True

    while swapped:
        swapped = False

        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True

eingabe_erlaubt = True

coole_liste = []

while eingabe_erlaubt:
    user_input = input("Deine Zahl (e für exit): ")

    if user_input == "e":
        eingabe_erlaubt = False
        break
    
    try:
        coole_liste.append(int(user_input))
    except:
        print("Invalide Eingabe!")

bubble_sort(coole_liste)

print(coole_liste)