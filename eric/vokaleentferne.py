def disemvowel(string):
    
    v = ["a", "e", "i", "o", "u"]
    ret = ""
    
    for i in string :
        if i.lower () in v:
            ret += ""
            
        else: 
            ret += i
            
        
    return ret


print(disemvowel("Mein Name ist Eric"))