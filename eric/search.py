def linear_search(list, element): 
    for i in range(len(list)):
        if list[i] == element:
            return i
            
        
    return -1 



coole_liste = ["Hund", "KAtze", "Maus"]


print(linear_search(coole_liste, "Maus"))