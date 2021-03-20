def disenvowel(string):
    v = ["a", "e", "i", "o", "u"]
    ret = ""

    for i in string:
        if i.lower() in v:
            ret += ""
        else:
            ret += i

    return ret


print(disenvowel("My name is jeff"))
